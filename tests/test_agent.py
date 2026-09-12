import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1]

class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root/'scripts').mkdir()
        shutil.copy(SOURCE/'scripts/agent.py', self.root/'scripts/agent.py')
        self.channel = 'linkedin'
        self.configure()

    def tearDown(self):
        self.temp.cleanup()

    def configure(self):
        (self.root/'agent.json').write_text(json.dumps({'channel': self.channel}))

    def run_cli(self, *args, ok=True):
        p = subprocess.run([sys.executable, str(self.root/'scripts/agent.py'), *args], capture_output=True, text=True)
        if ok:
            self.assertEqual(p.returncode, 0, p.stderr)
            return json.loads(p.stdout)
        self.assertNotEqual(p.returncode, 0)
        return p.stderr

    def fixture(self, name, data):
        p = self.root/name
        p.write_text(json.dumps(data))
        return str(p)

    def contact(self):
        return self.run_cli('contact', self.fixture('contact.json', {'name': 'Testperson', 'destination': 'https://www.linkedin.com/in/example/' if self.channel=='linkedin' else 'person@example.com', 'source': 'https://example.com'}))['id']

    def draft(self, c, text='Guten Tag'):
        return self.run_cli('draft', self.fixture('batch.json', {'title':'Test', 'sender':'sender@example.com', 'items':[{'contact_id':c,'kind':'connect' if self.channel=='linkedin' else 'email','subject':'Test','text':text}]}))['batch']

    def approve(self, b):
        h=self.run_cli('review', b)['digest']
        if self.channel=='coldmail':
            self.run_cli('test-confirm', b, '--digest',h,'--recipient','sender@example.com','--evidence','Nutzer bestätigt Eingang der Testmail')
        self.run_cli('approve',b,'--digest',h,'--by','Testnutzer','--evidence','Ausdrückliche Zustimmung im Test')
        return h

    def test_cancel_persists_and_keeps_started_for_reconciliation(self):
        c=self.contact();b=self.draft(c);self.approve(b)
        self.run_cli('cancel',b,'--reason','Nutzer widerruft')
        self.run_cli('claim',b,'A-1',ok=False)
        self.assertEqual(self.run_cli('status')['batches'][b]['items'][0]['status'],'cancelled')
        b2=self.draft(c,'Zweiter Text');self.approve(b2)
        self.run_cli('claim',b2,'A-1')
        self.run_cli('cancel',b2,'--reason','Stop')
        self.run_cli('record',b2,'A-1','--result','unknown','--evidence','Extern prüfen')

    def test_block_only_cancels_affected_recipient(self):
        c=self.contact()
        other=self.run_cli('contact',self.fixture('other.json',{'name':'Zweite Person','destination':'https://www.linkedin.com/in/second/','source':'https://example.com'}))['id']
        b=self.run_cli('draft',self.fixture('two.json',{'title':'Zwei','sender':'Eigenes Konto','items':[{'contact_id':i,'kind':'message','text':'Hallo'} for i in [c,other]]}))['batch']
        self.approve(b)
        self.run_cli('block',c,'--reason','Abmeldung')
        self.run_cli('claim',b,'A-1',ok=False)
        self.run_cli('claim',b,'A-2')

    def test_same_reply_does_not_cancel_new_response(self):
        c=self.contact()
        self.run_cli('reply',c,'--text','Frage','--evidence','message-123')
        b=self.draft(c,'Antwort');self.approve(b)
        result=self.run_cli('reply',c,'--text','Frage','--evidence','message-123')
        self.assertTrue(result['already_processed'])
        self.run_cli('claim',b,'A-1')

    def test_persistence_and_duplicate_contact(self):
        c=self.contact()
        self.assertIn(c,self.run_cli('status')['contacts'])
        self.run_cli('contact',str(self.root/'contact.json'),ok=False)
        self.assertIn('Testperson',(self.root/'data/kontakte.csv').read_text())

    def test_digest_and_changed_text_revoke_approval(self):
        c=self.contact();b=self.draft(c)
        self.run_cli('claim',b,'A-1',ok=False)
        h=self.run_cli('review',b)['digest']
        self.run_cli('approve',b,'--digest','wrong','--by','Test','--evidence','yes',ok=False)
        self.approve(b)
        self.run_cli('amend',b,'A-1',self.fixture('change.json',{'text':'Anderer Text'}))
        self.run_cli('claim',b,'A-1',ok=False)
        self.run_cli('approve',b,'--digest',h,'--by','Test','--evidence','yes',ok=False)
        self.approve(b)
        self.run_cli('claim',b,'A-1')

    def test_interruption_no_repeat_and_reconcile(self):
        c=self.contact();b=self.draft(c);self.approve(b)
        self.run_cli('claim',b,'A-1')
        self.run_cli('recover')
        self.run_cli('claim',b,'A-1',ok=False)
        self.run_cli('record',b,'A-1','--result','sent','--evidence','Extern bestätigt')
        self.run_cli('claim',b,'A-1',ok=False)
        self.run_cli('draft',str(self.root/'batch.json'),ok=False)

    def test_stop_and_reply_cancel_pending(self):
        c=self.contact();b=self.draft(c);self.approve(b)
        self.run_cli('reply',c,'--text','Danke','--evidence','Antwort im Postfach')
        self.run_cli('claim',b,'A-1',ok=False)
        b2=self.draft(c,'Neue Antwort');self.approve(b2)
        self.run_cli('block',c,'--reason','Keine weitere Ansprache')
        self.run_cli('claim',b2,'A-1',ok=False)
        self.run_cli('note',c,'--text','Test','--next-action','Anschreiben',ok=False)

    def test_coldmail_test_and_verification_required(self):
        self.channel='coldmail';self.configure()
        c=self.contact();b=self.draft(c);h=self.run_cli('review',b)['digest']
        self.run_cli('approve',b,'--digest',h,'--by','Test','--evidence','yes',ok=False)
        self.run_cli('test-confirm',b,'--digest',h,'--recipient','other@example.com','--evidence','Test',ok=False)
        self.approve(b)
        self.run_cli('claim',b,'A-1',ok=False)
        self.run_cli('verify',c,'--result','catch_all','--evidence','Providerprüfung')
        self.run_cli('claim',b,'A-1',ok=False)
        self.run_cli('verify',c,'--result','valid','--evidence','Providerprüfung')
        self.run_cli('claim',b,'A-1')

    def test_separate_channel_and_atomic_error(self):
        c=self.contact()
        self.channel='coldmail';self.configure()
        self.run_cli('status',ok=False)
        self.channel='linkedin';self.configure()
        self.run_cli('note',c,'--text','Notiz','--next-at','invalid',ok=False)
        self.assertEqual(self.run_cli('status')['contacts'][c]['next_at'],'')

    def test_duplicate_batches_claim_once(self):
        c=self.contact();b=self.draft(c);b2=self.draft(c)
        self.approve(b);self.approve(b2)
        self.run_cli('claim',b,'A-1')
        self.run_cli('claim',b2,'A-1',ok=False)

    def test_concurrent_claim_only_one_succeeds(self):
        c=self.contact();b=self.draft(c);self.approve(b)
        cmd=[sys.executable,str(self.root/'scripts/agent.py'),'claim',b,'A-1']
        procs=[subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE) for _ in range(2)]
        codes=[]
        for p in procs:
            p.communicate();codes.append(p.returncode)
        self.assertEqual(sorted(codes),[0,2])

    def test_comment_needs_specific_post(self):
        c=self.contact()
        f=self.fixture('comment.json',{'title':'Kommentar','sender':'Testkonto','items':[{'contact_id':c,'kind':'comment','text':'Beitrag','target':'https://evil.example/post'}]})
        self.run_cli('draft',f,ok=False)

if __name__ == '__main__':
    unittest.main()

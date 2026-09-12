import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]

class SkillInstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.base=Path(self.temp.name)
        self.project=self.base/'project'
        shutil.copytree(ROOT,self.project,ignore=shutil.ignore_patterns('.git','data','__pycache__'))
        self.target=self.base/'global'
        self.manifest=json.loads((self.project/'skills-manifest.json').read_text())

    def tearDown(self):
        self.temp.cleanup()

    def run_install(self,*args,ok=True):
        result=subprocess.run([sys.executable,str(self.project/'scripts/install_skills.py'),*args],cwd=self.base,capture_output=True,text=True)
        self.assertEqual(result.returncode==0,ok,result.stderr)
        return result

    def test_global_complete_and_bound_from_other_directory(self):
        self.run_install('--scope','global','--target-root',str(self.target))
        for runtime in ['.claude','.agents']:
            for name in self.manifest['skills']:
                folder=self.target/runtime/'skills'/name
                self.assertEqual((folder/'PROJECT_ROOT').read_text().strip(),str(self.project.resolve()))
                self.assertTrue((folder/'references/register-und-freigabe.md').exists())
                self.assertEqual((folder/'SKILL.md').read_bytes(),(self.project/'.agents/skills'/name/'SKILL.md').read_bytes())
        self.run_install('--scope','global','--target-root',str(self.target))
        self.assertFalse((self.project/'data').exists())

    def test_conflict_preflight_preserves_existing_and_no_partial_install(self):
        name=self.manifest['skills'][-1]
        folder=self.target/'.claude/skills'/name
        folder.mkdir(parents=True)
        (folder/'SKILL.md').write_text('Mein vorhandener Skill')
        self.run_install('--scope','global','--target-root',str(self.target),ok=False)
        self.assertEqual((folder/'SKILL.md').read_text(),'Mein vorhandener Skill')
        self.assertEqual(len(list((self.target/'.claude/skills').iterdir())),1)
        self.assertFalse((self.target/'.agents').exists())
        self.run_install('--scope','global','--target-root',str(self.target),'--replace')
        self.assertNotEqual((folder/'SKILL.md').read_text(),'Mein vorhandener Skill')

    def test_project_can_restore_missing_claude_entry(self):
        name=self.manifest['skills'][0]
        folder=self.project/'.claude/skills'/name
        shutil.rmtree(folder)
        self.run_install('--runtime','claude')
        self.assertTrue((folder/'SKILL.md').exists())
        self.assertFalse((folder/'PROJECT_ROOT').exists())
        self.assertEqual(folder.parents[2],self.project)

    def test_symlink_target_is_not_followed(self):
        name=self.manifest['skills'][0]
        victim=self.base/'unrelated';victim.mkdir();(victim/'important').write_text('behalten')
        folder=self.target/'.claude/skills'/name;folder.parent.mkdir(parents=True)
        folder.symlink_to(victim,target_is_directory=True)
        self.run_install('--scope','global','--target-root',str(self.target),'--replace',ok=False)
        self.assertEqual((victim/'important').read_text(),'behalten')

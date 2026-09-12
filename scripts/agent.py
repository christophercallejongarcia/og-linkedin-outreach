#!/usr/bin/env python3
"""Lokaler Kontakt- und Freigabestatus. Führt keine Netzwerkaktionen aus."""
import argparse
import csv
import hashlib
import io
import json
import os
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def read_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def atomic(path, content):
    tmp = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    try:
        with open(tmp, 'x', encoding='utf-8', newline='') as f:
            os.chmod(tmp, 0o600)
            f.write(content)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def cell(value):
    text = str(value if value is not None else '')
    return "'" + text if text.lstrip().startswith(('=', '+', '-', '@')) else text


def csv_text(rows, fields):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=fields)
    writer.writeheader()
    for row in rows:
        writer.writerow({k: cell(row.get(k, '')) for k in fields})
    return out.getvalue()


def export_state(folder, state):
    atomic(folder / 'kontakte.csv', csv_text(state['contacts'].values(), ['id', 'name', 'company', 'destination', 'source', 'status', 'last_action', 'next_action', 'next_at', 'verification', 'verified_at', 'blocked']))
    rows = []
    for batch in state['batches'].values():
        for item in batch['items']:
            rows.append(dict(item, batch=batch['id']))
    atomic(folder / 'aktionen.csv', csv_text(rows, ['batch', 'id', 'contact_id', 'kind', 'target', 'subject', 'text', 'status', 'at', 'evidence']))
    atomic(folder / 'verlauf.jsonl', ''.join(json.dumps(e, ensure_ascii=False) + '\n' for e in state['events']))
    atomic(folder / 'stand.json', json.dumps(state, ensure_ascii=False, indent=2) + '\n')


def contact_identity(channel, destination):
    destination = destination.strip()
    if channel == 'linkedin':
        from urllib.parse import urlsplit
        url = urlsplit(destination)
        require(url.scheme == 'https' and url.hostname in ('linkedin.com', 'www.linkedin.com') and url.path.startswith('/in/') and len(url.path.strip('/').split('/')) == 2, 'Erwartet wird eine LinkedIn-Profil-URL https://www.linkedin.com/in/name/.')
        return 'https://www.linkedin.com' + url.path.rstrip('/') + '/'
    require('@' in destination and not any(c.isspace() for c in destination) and len(destination.split('@')) == 2 and all(destination.split('@')), 'Eine einzelne E-Mail-Adresse ist erforderlich.')
    return destination.lower()


def batch_content(state, batch):
    # Freigabe bindet aktuelle Ziele, Texte, Absender und Aktionen. Laufstatus ist separat.
    return {'channel': state['channel'], 'sender': batch['sender'], 'title': batch['title'], 'items': [
        {k: item[k] for k in ('id', 'contact_id', 'kind', 'target', 'subject', 'text')} for item in batch['items']]}


def event(state, action, **data):
    state['events'].append(dict(at=now(), action=action, **data))


def find_item(state, batch_id, item_id):
    batch = state['batches'].get(batch_id)
    require(batch is not None, 'Paket nicht gefunden.')
    matches = [i for i in batch['items'] if i['id'] == item_id]
    require(len(matches) == 1, 'Aktion nicht gefunden.')
    return batch, matches[0]


def check_batch(state, batch):
    for item in batch['items']:
        c = state['contacts'][item['contact_id']]
        if item['kind'] != 'comment':
            require(item['target'] == c['destination'], 'Kontaktziel geändert. Neues Paket erstellen.')
    return digest(batch_content(state, batch))


def operate(state, op, a):
    if op == 'init':
        return {'channel': state['channel'], 'message': 'Lokales Register bereit. Einrichtung über workflows/einrichtung.md fortsetzen.'}
    if op == 'contact':
        d = read_json(a.file)
        for field in ('name', 'destination', 'source'):
            require(isinstance(d.get(field), str) and d[field].strip(), 'Kontaktfeld fehlt: ' + field)
        dest = contact_identity(state['channel'], d['destination'])
        existing = [c for c in state['contacts'].values() if c['destination'] == dest]
        require(not existing, 'Kontakt bereits vorhanden: ' + (existing[0]['id'] if existing else ''))
        ident = 'K-' + uuid.uuid4().hex[:10]
        c = dict(id=ident, name=d['name'].strip(), company=d.get('company', ''), destination=dest, source=d['source'], status='recherchiert', last_action='', next_action='', next_at='', verification='ungeprüft', verified_at='', blocked=False)
        state['contacts'][ident] = c
        event(state, 'kontakt_angelegt', contact_id=ident)
        return c
    if op == 'verify':
        c = state['contacts'][a.contact]
        require(state['channel'] == 'coldmail', 'Adressprüfung gehört zum Coldmail-Paket.')
        require(a.evidence.strip(), 'Prüfbeleg fehlt.')
        c.update(verification=a.result, verified_at=now())
        event(state, 'adresse_geprüft', contact_id=c['id'], result=a.result, evidence=a.evidence)
        return c
    if op == 'block':
        c = state['contacts'][a.contact]
        c.update(blocked=True, status='gesperrt', next_action='', next_at='')
        for batch in state['batches'].values():
            for item in batch['items']:
                if item['contact_id'] == c['id'] and item['status'] == 'pending':
                    item['status'] = 'cancelled'
        event(state, 'kontakt_gesperrt', contact_id=c['id'], reason=a.reason)
        return c
    if op == 'note':
        c = state['contacts'][a.contact]
        require(not (c['blocked'] and (a.next_action or a.next_at)), 'Gesperrter Kontakt bekommt keine Nachfassaktion.')
        if a.next_at:
            datetime.fromisoformat(a.next_at)
        c.update(next_action=a.next_action, next_at=a.next_at)
        event(state, 'notiz', contact_id=c['id'], text=a.text, next_action=a.next_action, next_at=a.next_at)
        return c
    if op == 'reply':
        c = state['contacts'][a.contact]
        require(a.evidence.strip(), 'Stabiler eindeutiger Antwortbeleg fehlt.')
        if any(e['action'] == 'antwort' and e.get('contact_id') == a.contact and e.get('evidence') == a.evidence for e in state['events']):
            return dict(c, already_processed=True)
        c.update(status='antwort_erhalten', next_action='', next_at='')
        # Antworten stoppen alle noch nicht begonnenen Aktionen an diese Person.
        for batch in state['batches'].values():
            for item in batch['items']:
                if item['contact_id'] == c['id'] and item['status'] == 'pending':
                    item['status'] = 'cancelled'
        event(state, 'antwort', contact_id=c['id'], text=a.text, evidence=a.evidence)
        return c
    if op == 'draft':
        d = read_json(a.file)
        require(isinstance(d.get('title'), str) and d['title'].strip(), 'Pakettitel fehlt.')
        require(isinstance(d.get('sender'), str) and d['sender'].strip(), 'Absenderkonto fehlt.')
        if state['channel'] == 'coldmail':
            contact_identity('coldmail', d['sender'])
        require(isinstance(d.get('items'), list) and d['items'], 'Paket enthält keine Aktionen.')
        items, seen = [], set()
        allowed = ('email',) if state['channel'] == 'coldmail' else ('connect', 'message', 'comment')
        for index, raw in enumerate(d['items'], 1):
            c = state['contacts'].get(raw.get('contact_id'))
            require(c is not None, 'Unbekannte Kontakt-ID.')
            require(not c['blocked'], 'Kontakt ist gesperrt: ' + c['id'])
            require(raw.get('kind') in allowed, 'Aktion passt nicht zum Kanal.')
            text = raw.get('text', '')
            subject = raw.get('subject', '')
            require(isinstance(text, str) and isinstance(subject, str), 'Text und Betreff müssen Zeichenketten sein.')
            require(text.strip() or raw['kind'] == 'connect', 'Nachrichtentext fehlt.')
            require(state['channel'] != 'coldmail' or subject.strip(), 'Betreff fehlt.')
            target = c['destination']
            if raw['kind'] == 'comment':
                from urllib.parse import urlsplit
                target = raw.get('target', '')
                url = urlsplit(target)
                require(url.scheme == 'https' and url.hostname in ('www.linkedin.com', 'linkedin.com') and url.path.startswith(('/posts/', '/feed/update/')), 'Für Kommentare wird eine konkrete LinkedIn-Beitrags-URL benötigt.')
            key = (c['id'], raw['kind'], target)
            require(key not in seen, 'Doppelte Aktion im Paket.')
            seen.add(key)
            # Identischen Text nicht über neue Pakete versehentlich erneut senden.
            for old in state['batches'].values():
                for previous in old['items']:
                    same = all(previous[k] == v for k, v in [('contact_id', c['id']), ('kind', raw['kind']), ('target', target), ('subject', subject), ('text', text)])
                    require(not (same and previous['status'] in ('sending', 'sent', 'unknown')), 'Identische Aktion wurde begonnen oder gesendet. Zuerst bisherigen Status prüfen.')
            items.append(dict(id='A-' + str(index), contact_id=c['id'], kind=raw['kind'], target=target, subject=subject, text=text, status='pending', at='', evidence=''))
        ident = 'P-' + uuid.uuid4().hex[:10]
        batch = dict(id=ident, title=d['title'], sender=d['sender'], created=now(), items=items, reviewed='', approval=None, test=None)
        state['batches'][ident] = batch
        event(state, 'paket_entworfen', batch=ident)
        return dict(batch=ident, actions=len(items), next='review')
    if op == 'review':
        batch = state['batches'][a.batch]
        sha = check_batch(state, batch)
        batch['reviewed'] = sha
        return dict(batch=a.batch, digest=sha, content=batch_content(state, batch), statuses={i['id']: i['status'] for i in batch['items']}, instruction='Nutzer muss genau dieses vollständige Paket prüfen und freigeben.')
    if op == 'amend':
        batch, item = find_item(state, a.batch, a.item)
        require(all(i['status'] == 'pending' for i in batch['items']), 'Begonnenes Paket bleibt unverändert. Für neue Inhalte neues Paket anlegen.')
        d = read_json(a.file)
        require(set(d) <= {'text', 'subject'} and d, 'Änderung darf nur text und subject enthalten.')
        for k, v in d.items():
            require(isinstance(v, str), 'Änderungswerte müssen Text sein.')
            item[k] = v
        require(item['text'].strip() or item['kind'] == 'connect', 'Text fehlt.')
        require(item['kind'] != 'email' or item['subject'].strip(), 'Betreff fehlt.')
        batch.update(reviewed='', approval=None, test=None)
        event(state, 'paket_geändert', batch=a.batch, item=a.item)
        return {'batch': a.batch, 'next': 'review'}
    if op == 'test-confirm':
        batch = state['batches'][a.batch]
        require(state['channel'] == 'coldmail', 'Nur Coldmail benötigt einen Mailtest.')
        sha = check_batch(state, batch)
        require(a.digest == sha == batch['reviewed'], 'Zuerst aktuelle Paketfassung prüfen.')
        require(contact_identity('coldmail', a.recipient) == contact_identity('coldmail', batch['sender']), 'Test muss an das eigene Absenderkonto gehen.')
        require(a.evidence.strip(), 'Beleg der bestätigten Testmail fehlt.')
        batch['test'] = dict(digest=sha, at=now(), evidence=a.evidence, recipient=a.recipient)
        event(state, 'testmail_bestätigt', batch=a.batch)
        return batch['test']
    if op == 'approve':
        batch = state['batches'][a.batch]
        sha = check_batch(state, batch)
        require(a.digest == sha == batch['reviewed'], 'Freigabe passt nicht zur vollständig geprüften Fassung.')
        require(a.by.strip() and a.evidence.strip(), 'Name und ausdrückliche Nutzerzustimmung als Beleg erforderlich.')
        if state['channel'] == 'coldmail':
            require(batch['test'] and batch['test']['digest'] == sha, 'Bestätigte Testmail für aktuelle Fassung fehlt.')
        batch['approval'] = dict(digest=sha, by=a.by, evidence=a.evidence, at=now())
        event(state, 'paket_freigegeben', batch=a.batch, digest=sha, by=a.by, evidence=a.evidence)
        return batch['approval']
    if op == 'cancel':
        batch = state['batches'][a.batch]
        require(a.reason.strip(), 'Widerrufsgrund fehlt.')
        batch['approval'] = None
        for item in batch['items']:
            if item['status'] == 'pending':
                item['status'] = 'cancelled'
        event(state, 'paket_storniert', batch=a.batch, reason=a.reason)
        return batch
    if op == 'claim':
        batch, item = find_item(state, a.batch, a.item)
        sha = check_batch(state, batch)
        require(batch['approval'] and batch['approval']['digest'] == sha, 'Passende Paketfreigabe fehlt.')
        require(item['status'] == 'pending', 'Aktion ist nicht ausstehend. Kein automatischer Wiederholungsversuch.')
        c = state['contacts'][item['contact_id']]
        require(not c['blocked'], 'Kontakt ist gesperrt: ' + c['id'])
        if state['channel'] == 'coldmail':
            require(c['verification'] == 'valid', 'Nur als gültig geprüfte E-Mail-Adressen sind sendebereit.')
        for other in state['batches'].values():
            for previous in other['items']:
                if previous is item:
                    continue
                same = all(previous[k] == item[k] for k in ('contact_id', 'kind', 'target', 'subject', 'text'))
                require(not (same and previous['status'] in ('sending', 'sent', 'unknown')), 'Identische Aktion bereits begonnen. Status zuerst abgleichen.')
        item.update(status='sending', at=now())
        event(state, 'aktion_reserviert', batch=a.batch, item=a.item)
        return dict(item, sender=batch['sender'], digest=sha, instruction='Jetzt genau diese Aktion einmal über das eingerichtete Tool ausführen; Ergebnis mit record dokumentieren.')
    if op == 'record':
        batch, item = find_item(state, a.batch, a.item)
        require(item['status'] in ('sending', 'unknown'), 'Nur begonnene oder unklare Aktionen können abgeglichen werden.')
        require(a.evidence.strip(), 'Ergebnisbeleg fehlt.')
        item.update(status=a.result, at=now(), evidence=a.evidence)
        c = state['contacts'][item['contact_id']]
        if a.result == 'sent':
            c.update(status='kontaktiert', last_action=item['at'])
        event(state, 'aktion_ergebnis', batch=a.batch, item=a.item, result=a.result, evidence=a.evidence)
        return item
    if op == 'recover':
        recovered = []
        for batch in state['batches'].values():
            for item in batch['items']:
                if item['status'] == 'sending':
                    item['status'] = 'unknown'
                    recovered.append([batch['id'], item['id']])
        event(state, 'unterbrechung_abgeglichen', actions=recovered)
        return {'unknown': recovered, 'instruction': 'Am Anbieter/Browser prüfen; nicht erneut senden. Danach record mit Beleg.'}
    if op in ('status', 'export'):
        return state
    raise ValueError('Unbekannter Befehl.')


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    s = p.add_subparsers(dest='op', required=True)
    for name in ('init', 'status', 'export', 'recover'):
        s.add_parser(name)
    for name in ('contact', 'draft'):
        s.add_parser(name).add_argument('file')
    q = s.add_parser('verify'); q.add_argument('contact'); q.add_argument('--result', choices=['valid', 'invalid', 'catch_all', 'unknown'], required=True); q.add_argument('--evidence', required=True)
    q = s.add_parser('block'); q.add_argument('contact'); q.add_argument('--reason', required=True)
    q = s.add_parser('note'); q.add_argument('contact'); q.add_argument('--text', required=True); q.add_argument('--next-action', default=''); q.add_argument('--next-at', default='')
    q = s.add_parser('reply'); q.add_argument('contact'); q.add_argument('--text', required=True); q.add_argument('--evidence', required=True)
    q = s.add_parser('cancel'); q.add_argument('batch'); q.add_argument('--reason', required=True)
    q = s.add_parser('review'); q.add_argument('batch')
    q = s.add_parser('amend'); q.add_argument('batch'); q.add_argument('item'); q.add_argument('file')
    q = s.add_parser('test-confirm'); q.add_argument('batch'); q.add_argument('--digest', required=True); q.add_argument('--recipient', required=True); q.add_argument('--evidence', required=True)
    q = s.add_parser('approve'); q.add_argument('batch'); q.add_argument('--digest', required=True); q.add_argument('--by', required=True); q.add_argument('--evidence', required=True)
    q = s.add_parser('claim'); q.add_argument('batch'); q.add_argument('item')
    q = s.add_parser('record'); q.add_argument('batch'); q.add_argument('item'); q.add_argument('--result', choices=['sent', 'failed', 'unknown'], required=True); q.add_argument('--evidence', required=True)
    return p


def main():
    a = parser().parse_args()
    root = Path(__file__).resolve().parent.parent
    cfg = read_json(root / 'agent.json')
    folder = root / 'data'
    folder.mkdir(mode=0o700, exist_ok=True)
    dbpath = folder / 'register.sqlite3'
    con = sqlite3.connect(dbpath, timeout=30)
    os.chmod(dbpath, 0o600)
    try:
        con.execute('CREATE TABLE IF NOT EXISTS register (id INTEGER PRIMARY KEY CHECK (id=1), value TEXT NOT NULL)')
        con.execute('BEGIN IMMEDIATE')
        row = con.execute('SELECT value FROM register WHERE id=1').fetchone()
        state = json.loads(row[0]) if row else dict(version=1, channel=cfg['channel'], contacts={}, batches={}, events=[])
        require(state['channel'] == cfg['channel'], 'Register gehört zu einem anderen Kanal. Datenverzeichnisse getrennt halten.')
        result = operate(state, a.op, a)
        con.execute('INSERT OR REPLACE INTO register VALUES (1, ?)', (json.dumps(state, ensure_ascii=False),))
        # Export ist eine Lesekopie; SQLite bleibt maßgeblich. Änderungen niemals per CSV importieren.
        export_state(folder, state)
        con.commit()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError, sqlite3.Error) as exc:
        con.rollback()
        print('Fehler: ' + str(exc), file=sys.stderr)
        return 2
    finally:
        con.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())

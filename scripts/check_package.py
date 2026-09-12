#!/usr/bin/env python3
"""Prüft veröffentlichbare Paketstruktur ohne Laufzeitdaten."""
import ast
import json
import re
from pathlib import Path
root = Path(__file__).resolve().parent.parent
name = json.loads((root / 'agent.json').read_text())['name']
errors = []
for required in ['README.md', 'AGENTS.md', 'CLAUDE.md', 'LICENSE', 'docs/werkzeuge.md', 'workflows/start.md', 'templates/profil.json']:
    if not (root / required).is_file(): errors.append('Fehlt: ' + required)
a = root / '.agents/skills' / name / 'SKILL.md'
b = root / '.claude/skills' / name / 'SKILL.md'
if not a.exists() or not b.exists() or a.read_text() != b.read_text(): errors.append('Skill-Einstiege fehlen oder weichen ab.')
for path in root.rglob('*.md'):
    if '.git' in path.parts or 'data' in path.relative_to(root).parts: continue
    text = path.read_text()
    for link in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in link and not link.startswith('#') and not (path.parent / link.split('#')[0]).exists(): errors.append(str(path.relative_to(root)) + ': Link fehlt ' + link)
    for route in re.findall(r'`(workflows/[^`]+\.md)`', text):
        if not (root / route).is_file(): errors.append('Route fehlt: ' + route)
for path in (root / 'templates').glob('*.json'): json.loads(path.read_text())
for path in (root / 'scripts').glob('*.py'): ast.parse(path.read_text())
manifest = json.loads((root / 'skills-manifest.json').read_text())
for name in manifest['skills']:
    a = root / '.agents/skills' / name / 'SKILL.md'
    b = root / '.claude/skills' / name / 'SKILL.md'
    if not a.exists() or not b.exists() or a.read_bytes() != b.read_bytes(): errors.append('Fachskill fehlt oder weicht ab: ' + name)
    for runtime in ['.agents', '.claude']:
        if not (root / runtime / 'skills' / name / 'references/register-und-freigabe.md').exists(): errors.append('Skill-Referenz fehlt: ' + name)
if errors:
    raise SystemExit('\n'.join(errors))
print('Paketstruktur, Skill-Einstiege, Verweise, JSON und Python-Syntax geprüft: ' + manifest['project'])

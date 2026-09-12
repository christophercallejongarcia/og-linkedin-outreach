#!/usr/bin/env python3
"""Native OG-Skills prüfen, projektlokal synchronisieren oder global installieren."""
import argparse
import json
import shutil
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime', choices=['claude', 'codex', 'both'], default='both')
    parser.add_argument('--scope', choices=['project', 'global'], default='project')
    parser.add_argument('--replace', action='store_true', help='Vorhandene abweichende Skill-Ordner ausdrücklich ersetzen.')
    parser.add_argument('--target-root', type=Path, help='Alternativer Basisordner für globale Installation, etwa für einen isolierten Test.')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root/'skills-manifest.json').read_text())
    config = json.loads((root/'agent.json').read_text())
    if config['name'] != manifest['project']:
        raise ValueError('Projekt und Skill-Manifest passen nicht zusammen.')
    runtimes = ['.claude', '.agents'] if args.runtime == 'both' else ['.claude' if args.runtime == 'claude' else '.agents']
    if args.target_root and args.scope != 'global':
        raise ValueError('--target-root gehört zur globalen Installation.')
    base = (args.target_root or Path.home()).expanduser().resolve() if args.scope == 'global' else root
    plan = []
    for name in manifest['skills']:
        source = root/'.agents/skills'/name
        if not (source/'SKILL.md').is_file() or not (source/'references/register-und-freigabe.md').is_file():
            raise ValueError('Unvollständiger Skill: '+name)
        for runtime in runtimes:
            target = base/runtime/'skills'/name
            if target == source:
                continue
            if target.is_symlink():
                raise ValueError('Ziel ist ein Symlink, bleibt unverändert: '+str(target))
            if target.exists() and not target.is_dir():
                raise ValueError('Ziel ist kein Verzeichnis: '+str(target))
            expected = {p.relative_to(source).as_posix():p.read_bytes() for p in source.rglob('*') if p.is_file()}
            if args.scope == 'global':
                expected['PROJECT_ROOT'] = (str(root)+'\n').encode()
            if target.exists():
                actual = {p.relative_to(target).as_posix():p.read_bytes() for p in target.rglob('*') if p.is_file()}
                if actual == expected:
                    continue
                if not args.replace:
                    raise ValueError('Abweichender Skill existiert; nichts installiert. Prüfen und ggf. --replace verwenden: '+str(target))
            plan.append((source,target,expected))
    # Erst alle Konflikte prüfen, bevor irgendein Ziel verändert wird.
    for source,target,expected in plan:
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)
        for relative,content in expected.items():
            path = target/relative
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(content)
    print(f"{len(manifest['skills'])} Skills geprüft; {len(plan)} Ordner installiert/aktualisiert ({args.scope}, {args.runtime}).")
    print('Neue Sitzung öffnen. Claude Code: /skillname. Codex: $skillname.')
    if args.scope == 'global':
        print('Projektbindung: '+str(root))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as exc:
        print('Fehler: '+str(exc),file=sys.stderr)
        sys.exit(2)

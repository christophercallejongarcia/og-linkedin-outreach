# Skills in Claude Code und Codex verwenden

## Im Projekt

Repo klonen oder ZIP entpacken, diesen Ordner in Claude Code oder Codex öffnen und die Sitzung neu starten. Die vollständigen Skill-Ordner sind bereits enthalten. Du musst keine Workflow-Dateien manuell laden. Wähle einen der in der README aufgeführten Skills.

Claude Code verwendet `/skillname`; Codex `$skillname`. Jeder Fachskill enthält seine eigene Beschreibung für die automatische Auswahl. Die Kanäle haben getrennte Namen und getrennte Daten.

`python3 scripts/install_skills.py --runtime both` prüft die enthaltenen Skills und synchronisiert fehlende Claude-Einstiege aus `.agents/skills/`. Abweichende vorhandene Dateien werden ohne `--replace` nicht überschrieben. `sh install.sh` ruft dasselbe Werkzeug auf.

## Optional global

```sh
python3 scripts/install_skills.py --runtime claude --scope global
python3 scripts/install_skills.py --runtime codex --scope global
```

Claude-Ziel ist `~/.claude/skills/`, Codex-Ziel `~/.agents/skills/`. Mit `--runtime both` beide installieren. Die globale Installation kopiert vollständige Skills samt Referenzen und legt je Skill eine PROJECT_ROOT-Datei an. Sie bindet den Skill an dieses Repo, dessen Werkzeuge und dessen eigenes Register. Das Repo muss lokal erhalten bleiben. Aus einem anderen Arbeitsordner wechselt der Agent für Registerbefehle zur gebundenen Projektwurzel.

Vorhandene identische Installationen werden übersprungen. Bei Konflikt bricht das Werkzeug vor Änderungen ab. Erst nach Prüfung `--replace` verwenden. Das entfernt den betroffenen bisherigen Skill-Ordner und ersetzt ihn vollständig. Andere Skills und persönliche Daten werden nicht angefasst. Nach Verschieben des Repos erneut mit dem neuen Pfad installieren.

`--target-root /pfad` schreibt eine globale Testinstallation in einen eigenen Basisordner. Das ist für Prüfungen gedacht und wird von Claude/Codex nicht automatisch geladen.

## Bearbeiten und aktualisieren

`.agents/skills/` ist die Quelle für den Installer. Nach eigenen Änderungen dort `python3 scripts/install_skills.py --runtime claude --replace` ausführen und beide Laufzeiteinstiege gemeinsam versionieren. Für ein globales Update denselben Installationsbefehl mit `--scope global --replace` nutzen, nachdem eigene Änderungen gesichert wurden.

## Voraussetzungen

Skills sind Anweisungen für die Agentenlaufzeit. Browser-/Computer-Use-Zugang, Recherche- und Maildienste müssen eingerichtet sein. Setup prüft sie einzeln. Der lokale Installer meldet keine externen Verbindungen als funktionsfähig und sendet keine Nachrichten. Die Tabellen entstehen unter ignoriertem data/.

## Geprüfter Stand

Je Paket bestehen 16 lokale Tests: zwölf Registertests und vier Installationstests. Geprüft sind vollständige globale Kopien mit Projektbindung, wiederholte Installation, Konfliktabbruch vor Änderungen, ausdrücklicher Ersatz, Wiederherstellung eines fehlenden Projekteinstiegs und Schutz vor einem Symlink-Ziel. Die Skill-Frontmatter und internen Referenzen wurden validiert. Das belegt Struktur und Installation, keinen Live-Test von Browser- oder Mailaktionen.

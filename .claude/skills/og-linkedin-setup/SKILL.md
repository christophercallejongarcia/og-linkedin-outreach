---
name: og-linkedin-setup
description: "Dieses linkedin-Paket mit eigenem Profil und passenden Werkzeugzugängen einrichten oder fehlende Verbindungen prüfen."
---

# Geführte Einrichtung

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Bei fehlendem Profil beginne direkt mit der geführten Einrichtung unten. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Geführte Einrichtung

1. Prüfe Python 3.10 oder neuer und starte `python3 scripts/agent.py init` im geprüften Projektordner. Das legt ausschließlich lokale Daten an.
2. Lies `templates/profil.json`. Frage in kurzen Runden nach Name, Angebot, Zielgruppe, Ausschlusskriterien, Absenderkonto und Schreibproben. Vorhandene Angaben übernehmen, keine fiktive Beispielperson als eingerichtet markieren.
3. Speichere das bestätigte Profil in `data/profil.json`. Kontaktlisten gehören in dieses Projekt; kein anderes OG-Register einlesen.
4. Prüfe die Fähigkeiten der aktuellen Laufzeit. LinkedIn benötigt lesenden Browserzugang und für Kontaktaktionen Eingabe/Klick. Claude Code: dokumentierte Chrome-Verbindung; Codex: vorhandene Browser-/Computer-Use-Werkzeuge. Login erledigt der Nutzer.
5. Lies `docs/werkzeuge.md` sowie `docs/claude-code.md` oder `docs/codex.md`. Verbinde nur beauftragte Dienste nach deren tatsächlicher Anleitung. Keine Schlüssel in Projektdateien schreiben.
6. Führe eine kleine lesende Probe aus. Speichere Dienst, getestete Fähigkeit, Datum und Einschränkung in `data/verbindungen.json`. Nicht getestete Funktionen bleiben offen.
7. Zeige funktionierende Zugänge und fehlende Schritte. Bereite auf Wunsch den ersten Recherchelauf mit echten Nutzerkriterien vor. Einrichtung erlaubt noch keinen Versand.

## Skills finden

Die README listet jeden einzelnen Skill und seinen Aufruf. In Claude Code `/<skillname>`, in Codex `$<skillname>`. Bei neu installierten Skills die Sitzung im Projekt neu starten. Mit `python3 scripts/install_skills.py --runtime both` lassen sich die Projekt-Einstiege prüfen und synchronisieren. Globale Installation ist optional und wird nur auf entsprechenden Nutzerauftrag ausgeführt.

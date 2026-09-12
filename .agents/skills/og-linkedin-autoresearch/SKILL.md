---
name: og-linkedin-autoresearch
description: "Vorhandene Kampagnendaten auswerten, eine Text- oder Zielgruppenhypothese testen und Varianten nachvollziehbar vergleichen."
---

# Ansprache mit kontrollierten Tests verbessern

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Ziel und Basis

Vereinbare eine Messgröße, etwa Antwortquote oder positive Antworten. LinkedIn-Annahmen nur zählen, wenn sie extern bestätigt wurden. Nutze Register und vorhandene Anbieterberichte; fehlende Öffnungs- oder Annahmedaten sind unbekannt. Eine abgesendete Kontaktanfrage ist keine angenommene Verbindung.

Lies bisherige Experimente in `data/experimente/`, aktuelle Texte und Kontaktgruppen. Speichere Ausgangswerte samt Zähler, Nenner, Beobachtungszeit und Datenquelle. Keine ausgedachten Branchen-Benchmarks. Bei wenig Daten eine Hypothese vorbereiten und die Aussagekraft begrenzen.

## Experiment planen

1. Formuliere eine konkrete Änderung und erwartete Wirkung. Ändere eine Variable, zum Beispiel den Einstieg oder die Länge der Einladung. Absenderidentität bleibt gleich.
2. Zeige Ausgangsfassung und Variante vollständig. Speichere beide unverändert mit Experiment-ID.
3. Lege vergleichbare Empfängergruppen, Zeitraum, Auswertungszeit und eine zur Situation passende Stichprobe fest. Dieselbe Person nicht für beide Varianten anschreiben.
4. Ordne Kontakt- und Paket-IDs vor Versand in `data/experimente/EXPERIMENT_ID.json` zu. Die ursprüngliche Zuordnung bleibt zur späteren Auswertung erhalten.
5. Bereite beide Varianten als konkrete Pakete vor. Neue Texte benötigen eigene Freigaben; das Experiment ist keine allgemeine Erlaubnis zum Versenden. Für Einladungen og-linkedin-connect, für Nachrichten og-linkedin verwenden.

## Auswerten

Warte die vereinbarte Beobachtungszeit ab. Aktualisiere Antworten und tatsächliche Versandresultate. Zähle eindeutige Empfänger; Wiederholungen einer Antwort nicht mehrfach werten. Lege positive Antworten nachvollziehbar fest und zeige unklare Klassifizierungen.

Vergleiche Quoten mit ihren Nennern und Bedingungen. Ein Unterschied von 3 zu 2 Antworten belegt keinen Gewinner. Keine pauschale Signifikanz aus zwanzig Kontakten oder einer Prozentgrenze ableiten. Bei kleiner oder verzerrter Stichprobe als offen einstufen.

Dokumentiere `beibehalten`, `verwerfen` oder `weiter prüfen` mit Begründung. Bewahre die alte Ausgangsfassung. Eine neue bevorzugte Vorlage verändert keine bereits freigegebenen Pakete.

## Weiterer Durchlauf

Schlage eine nächste Hypothese vor. Auf ausdrücklichen Wunsch kann og-linkedin-agent-teams regelmäßige Auswertung oder Erinnerung einrichten. Kein unbegrenzter Versandloop; neue Kontaktpakete bleiben freigabepflichtig. Speichere jedes Ergebnis, auch erfolglose Tests, in `data/experimente/protokoll.md`.

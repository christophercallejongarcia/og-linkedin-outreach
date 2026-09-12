# Sitzung beginnen

1. Lies `agent.json`. Prüfe mit `python3 scripts/agent.py status` den lokalen Stand. Beim ersten Start legt das Werkzeug das Register an.
2. Fehlt `data/profil.json`, folge `workflows/einrichtung.md`. Ohne definierten Absender und Zielgruppe keine Ansprache planen.
3. Zeige kurz ausstehende Aufgaben, gesperrte Kontakte und Aktionen mit Status `sending` oder `unknown`. Ein altes `sending` nach Sitzungsabbruch wird über `recover` zu `unknown`. Bei einer gleichzeitig laufenden anderen Sitzung nicht pauschal recover aufrufen.
4. Prüfe unklare externe Ergebnisse durch Lesen am Anbieter. Dokumentiere nur belegte Zustände. Eine neue Sitzung ist kein Anlass, alte Nachrichten erneut zu senden.
5. Wähle den Ablauf aus dem Einstiegsskill. Lies Antworten vor dem Erstellen weiterer Nachrichten an bereits kontaktierte Personen.

Am Ende den Kontaktstand und nächste Schritte über das Werkzeug speichern. Berichte tatsächliche Resultate und offene Punkte. Ein laufender Prozess oder Cronjob wird durch eine Aufgaben-Datei nicht automatisch gestartet.

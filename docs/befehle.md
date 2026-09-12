# Lokale Befehle

Python 3.10 oder neuer genügt. Keine Python-Pakete installieren. Alle Befehle im Repo-Ordner ausführen. IDs und Werte kommen aus den tatsächlichen Ergebnissen.

```sh
python3 scripts/agent.py init
python3 scripts/agent.py status
python3 scripts/agent.py contact data/kontakt.json
python3 scripts/agent.py draft data/paket.json
python3 scripts/agent.py review PAKET_ID
python3 scripts/agent.py approve PAKET_ID --digest HASH --by NAME --evidence ZUSTIMMUNG
python3 scripts/agent.py claim PAKET_ID AKTION_ID
python3 scripts/agent.py record PAKET_ID AKTION_ID --result sent --evidence BELEG
python3 scripts/agent.py recover
python3 scripts/agent.py export
```

Die Vorlage für `kontakt.json` ist templates/kontakt.json; die Paketvorlage steht in templates/paket.json. Der Agent ersetzt Beispielwerte durch bestätigte Nutzerdaten. Kontakt-IDs erzeugt das Werkzeug selbst.

`amend` ändert Texte noch unbegonnener Pakete und verwirft ihre Freigabe. `reply` dokumentiert Antworten und storniert ausstehende Aktionen an die Person. `block` sperrt Kontakte. `note` speichert Notizen und nächste Schritte. `verify` und `test-confirm` gehören nur zum Coldmail-Ablauf. Details: `python3 scripts/agent.py BEFEHL --help`.

Das Werkzeug sendet keine Nachricht. Zwischen claim und record führt der Agent die konkrete Aktion über das eingerichtete externe Tool aus. Bei Exitcode 2 abbrechen und den Fehler beheben. Keine Reservierung umgehen, um trotzdem zu senden.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
```

Die Tests arbeiten in temporären Verzeichnissen ohne externe Konten. Sie prüfen lokale Zustandsübergänge, keine wirklichen Provider- oder Browseraktionen.

Mit `cancel PAKET_ID --reason GRUND` einen Widerruf dauerhaft speichern. Reservierte oder unklare Aktionen weiterhin extern abgleichen. Für `reply --evidence` eine stabile Nachrichten-ID oder Gesprächs-URL mit Nachrichtenzeit und Text verwenden; identische Belege pro Kontakt werden nur einmal verarbeitet.

# Kontakte und Tabellen

Jedes Paket speichert seine eigene SQLite-Datei in `data/register.sqlite3`. Ein Kanalwechsel mit derselben Datenbank wird abgelehnt. Es gibt keinen Abgleich mit dem anderen OG-Paket.

Lesbare Tabellen entstehen automatisch: `data/kontakte.csv` enthält Kontakt-ID, Person, Unternehmen, Ziel, Quelle, Status, letzte und nächste Aktion, Prüfergebnis und Sperrstatus. `data/aktionen.csv` zeigt Pakete und einzelne Aktionen mit Text und Ergebnis. `data/verlauf.jsonl` enthält die Ereignisse. `data/stand.json` ist ein vollständiger Leseexport. SQLite bleibt die einzige maßgebliche Datenquelle.

Lege Kontakte über eine JSON-Datei mit `name`, `company`, `destination` und `source` an: `python3 scripts/agent.py contact data/neuer-kontakt.json`. LinkedIn verwendet Profil-URLs, Coldmail E-Mail-Adressen. Das Werkzeug normalisiert Ziele und lehnt Dubletten ab. Namen allein sind keine eindeutige Identität.

Status der Aktionen: `pending` wartet, `sending` wurde reserviert, `sent` ist extern bestätigt, `failed` ist nachweislich fehlgeschlagen, `unknown` muss abgeglichen werden, `cancelled` wurde durch eine Antwort gestoppt. Das System speichert keine garantierte Zustellung oder Zustimmung eines Empfängers.

SQLite-Transaktionen verhindern parallele Doppelreservierungen. Die Freigabe bindet den Paketinhalt per Hash. Wer lokale Dateien oder Skripte absichtlich manipuliert, kann diese Kontrollen umgehen; das Paket ist keine isolierte Sicherheitsplattform.

CSV-Formeln werden in Exporten als Text behandelt. Persönliche Daten und Tokens dürfen nicht eingecheckt werden. Die mitgelieferte `.gitignore` schließt data, Secrets und Browserprofile aus.

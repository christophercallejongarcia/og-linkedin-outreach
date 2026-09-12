# Register und Freigabe im jeweiligen Projekt

Alle Befehle im zuvor geprüften Projektordner ausführen. Python 3.10 oder neuer, keine zusätzlichen Python-Pakete erforderlich. Werte sicher als Argumente übergeben; Nutzertexte nicht in Shell-Code interpolieren. JSON-Dateien mit einem Dateischreibwerkzeug erzeugen.

## Lesen und Kontaktanlage

`python3 scripts/agent.py init` legt das Register an. `python3 scripts/agent.py status` liest Kontakte, Pakete und Ereignisse. Die maßgebliche Quelle ist `data/register.sqlite3`. CSV- und JSON-Exporte sind Lesekopien; nicht manuell als Datenquelle verändern.

Kontaktdatei unter `data/` nach `templates/kontakt.json` anlegen:

```json
{"name":"Anna Beispiel","company":"Beispielfirma","destination":"https://www.linkedin.com/in/beispiel/","source":"https://example.com/quelle"}
```

Bei Coldmailing steht in `destination` die bestätigte E-Mail-Adresse. Beispielwerte durch geprüfte Nutzerdaten ersetzen. `python3 scripts/agent.py contact data/kontakt.json` liefert eine Kontakt-ID. Bereits vorhandene Ziele werden abgelehnt: bestehende ID aus status verwenden, keine zweite Person erfinden. Beleg und nächste Aufgabe speichern:

```sh
python3 scripts/agent.py note KONTAKT_ID --text BELEG_UND_BEGRÜNDUNG --next-action AUFGABE --next-at YYYY-MM-DD
```

IDs und Texte sind Platzhalter und müssen durch tatsächliche Ergebnisse ersetzt werden. `note` ist die Notizhistorie, kein Termin-Scheduler. Die jeweils übergebenen nächsten Schritte ersetzen den vorherigen nächsten Schritt.

Coldmail-Verifizierung:

```sh
python3 scripts/agent.py verify KONTAKT_ID --result valid --evidence PRÜFBELEG
```

Nur ein bestätigtes gültiges Ergebnis erhält `valid`; andere mögliche Werte sind `invalid`, `catch_all`, `unknown`. Frische Ergebnisse vor Versand prüfen. Der lokale Status erzwingt keine Ablauffrist. Ein vom Provider angenommener Prüfauftrag gilt noch nicht als Verifizierung.

## Ein konkretes Aktionspaket

Erstelle nach `templates/paket.json` eine Datei unter `data/`:

```json
{
  "title": "Konkreter Kontaktlauf",
  "sender": "EIGENES_KONTO",
  "items": [
    {"contact_id":"KONTAKT_ID","kind":"message","text":"VOLLSTÄNDIGER_GEPRÜFTER_TEXT"}
  ]
}
```

LinkedIn unterstützt `connect`, `message`, `comment`. Bei `comment` zusätzlich `target` mit konkreter Beitrags-URL angeben. Einladungen ohne Notiz dürfen leeren Text haben; andere Aktionen nicht. Absender ist das tatsächliche LinkedIn-Konto.

Coldmail verwendet `kind: email`, zusätzlich `subject` und die tatsächliche Absenderadresse in `sender`. Der Empfänger kommt aus dem Kontakt. Keine Platzhalter erst nach der Freigabe ersetzen. Anhänge sind nicht Teil dieses Textpaket-Hashes und benötigen einen gesonderten konkreten Auftrag.

```sh
python3 scripts/agent.py draft data/paket.json
python3 scripts/agent.py review PAKET_ID
```

`review` liefert vollständiges Paket und Hash. Zeige dem Nutzer alle Empfänger, Aktionstypen, Ziele und endgültigen Texte einschließlich Absender und Betreff. Die reine Anzahl genügt nicht.

## Eigener Test bei Coldmailing

Vor Kontaktversand konkrete Testmail zeigen und den Auftrag zum Senden an das eigene Absenderkonto einholen. Sende genau diese Testmail über das verbundene Tool. Nach bestätigtem Empfang und Darstellung:

```sh
python3 scripts/agent.py test-confirm PAKET_ID --digest HASH --recipient EIGENE_ABSENDERADRESSE --evidence TATSÄCHLICHE_BESTÄTIGUNG
```

Das Werkzeug bestätigt nur den lokalen Teststatus, es versendet selbst nichts. Der Test gilt für die geprüfte Paketfassung. Noch keine Kontaktmails senden.

## Freigabe und Ausführung

Erst nach wirklicher ausdrücklicher Nutzerzustimmung zu genau diesem Paket:

```sh
python3 scripts/agent.py approve PAKET_ID --digest HASH --by NUTZERNAME --evidence NUTZERWORTLAUT
python3 scripts/agent.py claim PAKET_ID AKTION_ID
```

`claim` reserviert nur lokal. Bei Fehler stoppen. Bei Erfolg genau die zurückgegebene Aktion über Browser oder verbundenen Versanddienst einmal ausführen. Sofort danach:

```sh
python3 scripts/agent.py record PAKET_ID AKTION_ID --result sent --evidence EXTERNER_BELEG
```

`sent` nur bei bestätigtem Versandauftrag beziehungsweise erfolgreicher Browseraktion; keine garantierte Zustellung behaupten. Belegter Nichtversand ist `failed`, ein Timeout oder unklarer Ausgang `unknown`. Nie durch Umgehen des Registers wiederholen. Diese Regeln binden die Agentenarbeit, sind keine systemweite Toolsperre.

Änderungen an unbegonnenen Paketen:

```sh
python3 scripts/agent.py amend PAKET_ID AKTION_ID data/aenderung.json
```

Änderungsdatei enthält `text` und/oder `subject`. Prüfung, Test und Freigabe werden verworfen. Bei geändertem Empfänger/Absender oder schon begonnenem Paket neues Paket für tatsächlich noch benötigte Aktionen erstellen.

## Widerruf, Antworten und Unterbrechung

```sh
python3 scripts/agent.py cancel PAKET_ID --reason NUTZERWIDERRUF
python3 scripts/agent.py reply KONTAKT_ID --text ANTWORT --evidence STABILE_NACHRICHTEN_ID
python3 scripts/agent.py block KONTAKT_ID --reason ABMELDEWUNSCH
```

Widerruf storniert offene Aktionen und löscht die Freigabe. Antworten stoppen ausstehende Aktionen an diese Person. Ein identischer Antwortbeleg wird nur einmal verarbeitet. Beim Browser Gesprächs-URL, Nachrichtenzeit und Text als stabilen Beleg verwenden. Sperren stoppen nur die betroffene Person. Extern bereits geplante Sendungen zusätzlich beim Versanddienst prüfen; die lokale Sperre ruft keine fremde Warteschlange zurück.

Nach unterbrochener Sitzung nur dann `python3 scripts/agent.py recover` ausführen, wenn kein anderer Lauf dieselben Aktionen noch bearbeitet. Das setzt reservierte Aktionen auf unklar. Im Zielkonto prüfen und anschließend `record` mit Ergebnisbeleg verwenden. Keine bereits ausgeführte Nachricht erneut senden.

`python3 scripts/agent.py export` erneuert Lesetabellen. `kontakte.csv` zeigt Kontakte und nächste Schritte, `aktionen.csv` Pakete und Aktionen, `verlauf.jsonl` die Ereignisse. Private Dateien bleiben unter ignoriertem `data/`. Das zweite OG-Repo hat sein vollständig getrenntes Register.

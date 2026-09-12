# Antworten und nächste Schritte

Lies die Inbox oder die angebotenen Antwort-Tools nur für die beauftragten Kontakte. Ordne Antworten anhand des tatsächlichen Threads oder Profils zu. Bei zweifelhafter Zuordnung nachfragen.

`reply KONTAKT_ID --text ANTWORT --evidence THREAD_ODER_BELEG` speichert die Antwort und storniert ausstehende Aktionen an diesen Kontakt. Anschließend eine passende neue Reaktion vorbereiten. Bei „nicht mehr kontaktieren“ mit `block KONTAKT_ID --reason GRUND` sperren. Sperren sind absichtlich nicht per Komfortbefehl rückgängig zu machen.

Mit `note KONTAKT_ID --text NOTIZ --next-action AUFGABE --next-at YYYY-MM-DD` den nächsten Schritt speichern. Ein Datum ist eine Erinnerung, kein gestarteter Scheduler. Bei einem neuen Durchlauf fällige Einträge aus `status` filtern, Antworten aktualisieren und erst danach neue Pakete vorbereiten.

Der Verlauf und die CSV-Dateien werden bei jedem erfolgreichen Befehl erneuert. Falls Lesekopien nach einem Absturz abweichen: `export` erzeugt sie aus SQLite neu. Keine Daten manuell in den Exporten ändern. Sichere den gesamten privaten data-Ordner bei beendeten Schreibvorgängen.

Antworten mit einem stabilen eindeutigen Beleg einlesen: Nachrichten-ID des Dienstes, beim Browser Profil-/Gesprächs-URL plus Nachrichtenzeit und Text. Beim erneuten Einlesen denselben Beleg verwenden. Identische Antwortbelege pro Kontakt werden ohne weitere Stornierungen übersprungen. Neue Antworten brauchen neue Belege.

# Ein geprüftes Paket ausführen

Erstelle eine JSON-Datei in `data/` nach `templates/paket.json`. Ein Eintrag bezeichnet genau einen Empfänger, Aktionstyp, Ziel und endgültigen Text. Kommentarziele sind konkrete Beitrags-URLs. Als Absender die eigene Profil-URL festhalten.

1. `python3 scripts/agent.py draft data/paket.json` erzeugt eine Paket-ID.
2. `python3 scripts/agent.py review PAKET_ID` gibt alle Inhalte und den SHA-256-Hash aus. Zeige dem Nutzer die vollständigen Inhalte, nicht nur die Anzahl. Die Platzhalter in diesen Befehlen ersetzt du durch die tatsächlichen IDs.
3. Frage nach Freigabe dieser Fassung. Erst nach ausdrücklichem Ja `approve PAKET_ID --digest HASH --by NAME --evidence NUTZERWORTLAUT` aufrufen. Bei Verwendung der Shell Werte sicher als einzelne Argumente übergeben; Nutzertexte nicht als Shell-Code zusammensetzen.
4. Für jeden Eintrag `claim PAKET_ID AKTION_ID`. Nur bei Exitcode 0 genau die zurückgegebene Aktion über das passende Tool ausführen. Der Aufruf reserviert lokal, er sendet noch nichts.
5. Unmittelbar danach `record PAKET_ID AKTION_ID --result sent|failed|unknown --evidence BELEG`. `sent` nur bei bestätigtem Erfolg. Ein Timeout ist `unknown`, nicht `failed`.

`amend PAKET_ID AKTION_ID data/aenderung.json` ändert Text/Betreff eines noch nicht begonnenen Pakets. Das löscht Prüfung, Testbestätigung und Freigabe. Für Änderungen nach Beginn ein neues Paket mit ausschließlich neuen/geänderten, tatsächlich noch benötigten Aktionen erstellen.

Abgelehnte oder fehlgeschlagene Aktionen nicht automatisch wiederholen. Erst Ursache prüfen. Ein neuer Versuch benötigt einen belegten Nichtversand und ein neu geprüftes Paket. Ein `unknown` wird mit `record` nach externer Kontrolle aufgelöst. Identische bereits begonnene Aktionen werden auch über Paketgrenzen erkannt.

Eine Plattformgrenze, Kontosperre, CAPTCHA oder unklare Identität beendet die betroffene Ausführung. Keine Umgehung über andere Konten oder versteckte Browser. Die Paketfreigabe ersetzt keine zusätzlichen Berechtigungsdialoge der Laufzeit.

Bei Nutzerwiderruf sofort `cancel PAKET_ID --reason GRUND` aufrufen. Das löscht die Freigabe und storniert offene Aktionen dauerhaft. Bereits reservierte oder unklare Aktionen extern abgleichen; ein lokaler Widerruf ruft keinen fremden Versandauftrag zurück.

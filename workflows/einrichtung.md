# Geführter Erststart

Führe den Nutzer in kleinen Runden durch den Start. Prüfe bereits Vorhandenes, statt alles erneut abzufragen.

## Profil

Frage nach Name, Angebot, Zielgruppe mit Ein-/Ausschlusskriterien, Absenderkonto und gewünschtem Schreibstil. Bitte um zwei eigene Schreibproben, wenn der Ton noch unklar ist. Kopiere `templates/profil.json` nach `data/profil.json` und trage die Antworten ein. Beispiele sind keine echten Kontaktdaten. Bestehende Profile nicht überschreiben.

## Verbindungen

Bestimme zuerst die laufende Umgebung: Claude Code oder Codex. Lies die passende Doku. Erfasse pro benötigter Fähigkeit den gewählten Dienst, den tatsächlich sichtbaren Tool-Namen, dessen Schema und den Verbindungsstatus in `data/verbindungen.json`. Die Vorlage liegt in `templates/verbindungen.json`.

Zeige verfügbare Dienste aus `docs/werkzeuge.md`. Der Nutzer wählt seine vorhandenen Konten. Verbinde nur gewählte Anbieter. Unterstützt die Umgebung den jeweiligen MCP nicht, nenne den dokumentierten Einrichtungsweg und prüfe nach dem Neustart erneut. Ein API-Key allein ist noch keine eingerichtete Verbindung. Geheimnisse gehören in die Secret-/OAuth-Verwaltung der Laufzeit, nicht in diese Dateien.

## Funktionsprobe

Prüfe zunächst eine kleine Leseaufgabe. Halte Dienst, Tool, Datum und beobachtetes Ergebnis fest. Für Coldmail ist der getrennt freigegebene Testversand an das eigene Postfach im Versandablauf vorgesehen. Für LinkedIn reicht beim Erststart das Lesen des eigenen Profils. Keine fremden Personen für einen Setup-Test anschreiben.

Schließe den Erststart mit dem ersten konkreten Nutzerauftrag ab. Benenne verbleibende fehlende Fähigkeiten. Ein teilweise eingerichtetes Paket darf bereits recherchieren oder schreiben, soweit seine Werkzeuge dafür reichen; den Versand nicht als bereit markieren.

---
name: og-linkedin-deck
description: "Eine deutschsprachige Präsentation zu einem konkreten Angebot oder Kundengespräch erstellen und bei vorhandenem Renderer als PDF ausgeben."
---

# Angebotspräsentation vorbereiten

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Briefing

Lies Angebot und Identität aus dem Nutzerprofil. Frage nur fehlende Zielgruppe, Anlass, Kernpunkte und gewünschte Gestaltung ab. Nutzen und Zahlen müssen aus bestätigten Angaben stammen. Keine fremden Namen, Signaturen oder Portfoliounterlagen übernehmen.

## Inhalt

Entwirf eine kurze Folge mit Titel, konkretem Ausgangsproblem, vorgeschlagenem Ablauf, benötigten Voraussetzungen und nächstem Schritt. Ergebnisse, Preise oder Referenzen nur aufnehmen, wenn vom Nutzer belegt. Form und Seitenzahl nach Inhalt wählen, etwa fünf bis acht Seiten als Ausgangspunkt.

## Erstellen

Speichere die bearbeitbare Fassung unter `data/praesentationen/`. Mit einem vorhandenen Präsentationswerkzeug dessen Format verwenden. Alternativ ein eigenständiges HTML mit eingebettetem CSS und Drucklayout erstellen. Für PDF im Querformat Seitenumbrüche je Folie, ausreichende Ränder und lesbare Schrift setzen. Den bestätigten Nutzerstil verwenden, sonst eine schlichte sachliche Gestaltung.

Prüfe lokal, ob ein PDF-Renderer vorhanden ist. Beispielsweise kann ein eingerichteter Chromium-Druckweg oder WeasyPrint HTML umwandeln. Keine Software als installiert behaupten. Fehlt ein Renderer, HTML liefern und die konkrete fehlende Voraussetzung nennen.

## Prüfen

Lies jede gerenderte Seite. Prüfe Überläufe, Schriftgröße, Umlaute, Reihenfolge und Linkziele. Öffne die resultierende PDF und kontrolliere Seitenzahl. Ein erfolgreicher Export allein genügt nicht. Dokumentiere, was tatsächlich visuell geprüft wurde.

## Material verwenden

Das Deck kann als Material für ein beauftragtes LinkedIn-Gespräch dienen. Der aktuelle Textaktions-Tracker erfasst keine Datei-Anhänge. Bei angefragtem Dateiversand dafür einen konkreten Auftrag samt Empfänger und Datei prüfen; keine Anhangsfunktion vortäuschen.

Zeige bearbeitbare Datei und PDF, soweit erstellt. Anhänge nicht ohne Auftrag an echte Kontakte oder an das eigene Postfach senden. Dateiupload-IDs und deren Gültigkeit sind vom verwendeten Dienst abhängig; keine festen Cloud-Schlüssel voraussetzen.

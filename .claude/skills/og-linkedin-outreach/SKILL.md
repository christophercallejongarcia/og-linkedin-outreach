---
name: og-linkedin-outreach
description: "Einrichtung und passende einzelne LinkedIn-Skills auswählen; bei einem konkreten Auftrag den zutreffenden Skill vollständig ausführen."
---

# LinkedIn-Outreach starten

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Auftrag zuordnen

Bei erstem Start `og-linkedin-setup` ausführen. Bei konkretem Auftrag den passenden einzelnen Skill unter `.claude/skills/` oder `.agents/skills/` lesen und ausführen. Diese Dateien enthalten jeweils den vollständigen Ablauf.

- `og-linkedin`: Profile recherchieren, Kontakte suchen, Nachrichten und Benachrichtigungen lesen oder freigegebene LinkedIn-Aktionen ausführen.
- `og-linkedin-connect`: Eine konkrete Liste von LinkedIn-Profilen mit geprüften Notizen zur Vernetzung vorbereiten und nach Paketfreigabe im Browser ausführen.
- `og-lead-borrow`: Kommentierende und reagierende Personen eines fremden LinkedIn-Beitrags recherchieren, nach eigener Zielgruppe qualifizieren und Kontaktentwürfe vorbereiten.
- `og-leadthunder`: Kommentierende eines LinkedIn-Beitrags direkt über die verfügbare Browseransicht erfassen und eine personalisierte Vernetzungskampagne vorbereiten.
- `og-daily-icp-feed`: Aktuelle LinkedIn-Beiträge zur eigenen Zielgruppe sammeln, bewerten und konkrete Kommentarentwürfe als prüfbare Auswahl liefern.
- `og-qualify-audience`: Personen aus Kommentaren und Reaktionen auf eigene LinkedIn-Beiträge nach den eigenen Kundenkriterien bewerten.
- `og-content-reflect`: Eigene Beiträge anhand verfügbarer Inhalts- und Leistungsdaten vergleichen und daraus konkrete nächste Themen ableiten.
- `og-content-compare`: Ausgewählte LinkedIn-Profile und Beiträge auf Themen, Formate, sichtbare Resonanz und passende eigene Themenansätze untersuchen.
- `og-content-source`: Aktuelle Branchen- oder KI-Geschichten mit Quellen finden und daraus einen eigenen deutschen Postentwurf samt Bildbriefing entwickeln.
- `og-linkedin-signal-monitor`: Finanzierungs-, Stellen-, Beitrags- oder Bewertungssignale zur eigenen Zielgruppe recherchieren und begründete Kontaktentwürfe vorbereiten.
- `og-linkedin-autoresearch`: Vorhandene Kampagnendaten auswerten, eine Text- oder Zielgruppenhypothese testen und Varianten nachvollziehbar vergleichen.
- `og-linkedin-agent-teams`: Einen beauftragten Outreach-Arbeitsauftrag in konkrete Teilaufgaben mit Zuständigkeiten, Übergaben und optionaler Wiederholung übersetzen.
- `og-linkedin-apify-skills`: Passende Apify-Actors für Leadquellen, Beiträge, Wettbewerber oder Signale auswählen, lesend testen und Ergebnisse in die Kontaktarbeit übernehmen.
- `og-linkedin-deck`: Eine deutschsprachige Präsentation zu einem konkreten Angebot oder Kundengespräch erstellen und bei vorhandenem Renderer als PDF ausgeben.

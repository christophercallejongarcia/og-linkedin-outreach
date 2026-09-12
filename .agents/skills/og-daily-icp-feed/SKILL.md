---
name: og-daily-icp-feed
description: "Aktuelle LinkedIn-Beiträge zur eigenen Zielgruppe sammeln, bewerten und konkrete Kommentarentwürfe als prüfbare Auswahl liefern."
---

# Täglicher Themenfeed mit Kommentarentwürfen

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Einrichtung

Lies Zielgruppe und Schreibproben. Frage nur fehlende Suchbegriffe, Zeitraum und gewünschte Anzahl ab. Speichere sie in `data/icp-feed-kriterien.json`. Prüfe vorhandene Websuche, Apify oder Browserzugriff mit einer kleinen Leseaufgabe.

## Beiträge sammeln und ordnen

Suche nach den vereinbarten Begriffen und öffne die Beiträge. Erfasse Autor, Profil-URL, Beitrags-URL, Datum, vollständigen relevanten Inhalt und tatsächlich sichtbare Reaktionszahlen. Dedupliziere nach Beitrags-URL. Prüfe im Aktionsregister, ob dort bereits ein Kommentar ausgeführt, reserviert oder ungeklärt ist.

Ordne zuerst nach Zielgruppenbezug und Aktualität. Sichtbare Interaktionen dürfen ergänzend sortieren; fehlende Zahlen bleiben unbekannt. Eine optionale Gewichtung von Kommentaren und Reaktionen ist eine Sortierhilfe, keine gemessene Reichweite.

## Entwürfe

Schreibe pro ausgewähltem Beitrag einen kurzen Kommentar, der einen konkreten Gedanken aufgreift. Ergänze eine begründete Beobachtung oder echte Frage. Persönliche Erfahrung nur verwenden, wenn sie aus dem Nutzerprofil belegt ist. Kein pauschales Lob und keine automatische Eigenwerbung.

Speichere `data/feeds/YYYY-MM-DD.md` mit Suchumfang, Quellen, Auswahlgrund und vollständigem Entwurf je Beitrag. Zeige die Auswahl. Ein Feed ist noch kein Versandpaket.

## Ausführung und Wiederholung

Für die vom Nutzer ausgewählten Kommentare Kontakte zuordnen und `comment`-Aktionen mit konkreten Beitrags-URLs erstellen. Vollständiges Paket freigeben lassen und über og-linkedin ausführen. Ergebnisse gehen ins Aktionsregister.

Bei Wunsch nach Wiederholung nutze og-linkedin-agent-teams für eine ausdrücklich beauftragte Planung. Ohne vorhandenen Scheduler bleibt es ein manuell aufrufbarer Tagesfeed. Zeitpläne dürfen Recherche und Entwürfe erneuern; neue Kommentare brauchen weiterhin die Freigabe ihres Pakets.

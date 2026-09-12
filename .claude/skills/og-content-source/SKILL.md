---
name: og-content-source
description: "Aktuelle Branchen- oder KI-Geschichten mit Quellen finden und daraus einen eigenen deutschen Postentwurf samt Bildbriefing entwickeln."
---

# Belegte Geschichten für LinkedIn recherchieren

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Rechercheauftrag

Lies Nutzerprofil und Themeninteressen. Verwende die genannten Themen; ohne Vorgabe an den beruflichen Themen des Profils orientieren. Suche in Primärquellen wie Produktankündigungen, Projekt-Repositories, Unternehmensberichten oder Originalbeiträgen. Datum des Ereignisses und der Veröffentlichung getrennt prüfen.

## Auswahl

Sammle einige geeignete Geschichten. Beurteile Bezug zur Zielgruppe, konkrete beobachtbare Arbeit, nachvollziehbare Quellen und Aktualität. Eine namentlich belegte Person oder messbare Änderung kann die Geschichte greifbarer machen. Fehlen Zahlen, erfinde keine und suche nicht nur nach spektakulären Behauptungen.

Öffne die Primärquelle. Halte fest, wer was mit welchen Werkzeugen gemacht hat, welche Schritte belegt sind und welche Grenzen die Quelle nennt. Prüfe auffällige Resultate anhand des ursprünglichen Berichts.

## Entwurf

Schreibe einen deutschen Beitrag, der die konkrete Geschichte erklärt. Trenne Bericht, eigene Einordnung und offene Fragen. Erzähle fremde Resultate nicht als Nutzererfahrung. Eigene Angebote nur bei sachlichem Bezug und bestätigtem Wunsch einbauen. Der CTA darf nur verfügbare oder wirklich beauftragte Materialien versprechen.

Erstelle ein Bildbriefing, das denselben Ablauf oder Vergleich erklärt. Nutze die vom Nutzer bestätigten Farben und Formate. Namen, Zahlen und Werkzeugzuordnung müssen zur Quelle passen. Kein fremdes Branding oder eine feste fremde Signatur übernehmen.

## Speichern und Wiederaufnahme

Schreibe Recherche, ausgewählten Entwurf und Bildbriefing in `data/content/`. Bewahre ungenutzte Themen mit Quelle und Datum in `data/content/backlog.md` auf. Prüfe vor neuer Recherche vorhandene Entwürfe und bereits veröffentlichte Themen, soweit deren Status bekannt ist.

Zeige Quelllinks und den vollständigen Entwurf. Dieser Skill veröffentlicht keinen eigenen Feedbeitrag automatisch. Ein Veröffentlichungstool oder Bildgenerator ist nur nutzbar, wenn in der Sitzung tatsächlich vorhanden. Fehlende Werkzeuge konkret benennen.

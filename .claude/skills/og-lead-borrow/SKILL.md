---
name: og-lead-borrow
description: "Kommentierende und reagierende Personen eines fremden LinkedIn-Beitrags recherchieren, nach eigener Zielgruppe qualifizieren und Kontaktentwürfe vorbereiten."
---

# Passende Kontakte aus fremden Beiträgen

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Eingaben und erster Zugriff

Nutze die genannte Beitrags-URL. Fehlt sie, frage nach Autor und Thema und identifiziere den Beitrag. Lies Zielgruppe und Ausschlusskriterien aus dem Nutzerprofil. Prüfe einen vorhandenen Apify-Zugang für lesende Erfassung; alternativ den angemeldeten Browser. Ohne Browser lassen sich Recherche und Entwürfe erledigen, aber keine Einladungen ausführen.

## Personen erfassen

Lies den gesamten Beitrag. Erfasse Kommentare und Reaktionen mit Name, Profil-URL, Rolle, Firma, Interaktionstyp und gegebenenfalls Kommentartext. Bei Apify vor dem Lauf Actor, Eingabeschema, Kosten und Umfang prüfen. Bei Browsererfassung „Weitere Kommentare“ und Reaktionslisten nur im vereinbarten Umfang nachladen. Dokumentiere unvollständig sichtbare Listen ausdrücklich; eine Anzahl auf der Seite ist keine Garantie, alle Personen erfasst zu haben.

Speichere die Erhebung mit Datum und Beitrags-URL in `data/lead-borrow/`. Gleiche Personen anhand der Profil-URL ab. Ein Like allein ist kein Kaufinteresse und kein Einverständnis für Nachrichten.

## Qualifizieren

Prüfe Rolle, Unternehmen und beobachteten Anlass gegen die eigenen Kriterien. Begründe für jede Person `passend`, `prüfen` oder `ausschließen`. Übernimm keine vorgegebene Sales-Zielgruppe aus Beispielen. Erfasse passende Kontakte mit `contact`, Gründe und Quellen mit `note`. Bereits vorhandene Kontakte behalten ihre ID und ihren Verlauf.

## Kontaktaufnahme und Gespräch

Entwirf eine Einladung, die sich korrekt auf Kommentar oder Reaktion bezieht. Behaupte bei einem Like keinen gelesenen Kommentar. Nutze nur das tatsächliche Angebot des Nutzers. Erstelle zusätzlich einen möglichen Gesprächseinstieg nach Annahme und einen optionalen Nachfassentwurf, jeweils getrennt vom aktuellen Versandpaket.

Zeige Qualifizierung und die konkrete Einladungsliste. Für freigegebene Einladungen verwende og-linkedin-connect mit Kontakt-IDs. Weitere Gesprächsschritte übernimmt og-linkedin. Ein fertig recherchierter Kontakt wird niemals während der Recherche ungeprüft angeschrieben.

## Ergebnis

Erhebung, begründete Auswahl, Paket-ID und noch offene Gesprächsentwürfe in `data/lead-borrow/` ablegen. Der Kontakt- und Aktionsstatus bleibt im Register. Keine E-Mail-Anreicherung oder Übertragung in ein anderes Repo ohne eigenen Auftrag.

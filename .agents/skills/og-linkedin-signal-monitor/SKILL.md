---
name: og-linkedin-signal-monitor
description: "Finanzierungs-, Stellen-, Beitrags- oder Bewertungssignale zur eigenen Zielgruppe recherchieren und begründete Kontaktentwürfe vorbereiten."
---

# Relevante Unternehmenssignale finden

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Kriterien und Datenquellen

Lies Nutzerprofil, vorhandene Verbindungen und den letzten Signalbericht. Definiere Branchen, Region, relevante Rollen, beobachtete Ereignisse und Zeitraum. Frage nur offene Kriterien ab und speichere sie in `data/signal-kriterien.json`. Suche über vorhandene Websuche, Browser oder geprüfte Apify-Actors; konkrete Dienste sind austauschbar.

## Signale prüfen

- Finanzierung: Originalankündigung, Firma, Datum, Runde und genannte Beteiligte erfassen. Eine Finanzierung beweist weder Budget für das Angebot noch Kaufabsicht.
- Stellen: Unternehmensseite oder Originalausschreibung öffnen, Rolle und Aktualität prüfen. Der Bedarf muss zum Angebot passen.
- Beiträge: vollständigen Text, Person, Datum und Beitrags-URL lesen. Aussagen im tatsächlichen Zusammenhang verwenden.
- Bewertungen oder Produktänderungen: Quelle und Zeitpunkt sichern. Einzelne negative Bewertungen nicht als belegtes Unternehmensproblem ausgeben.

Dedupliziere Firmen und Ereignisse. Priorisiere nach belegtem Bezug zum Nutzerangebot und Aktualität, nicht pauschal nach Finanzierungsbetrag. Speichere unklare Fälle getrennt. Erfasse Quelle, Ereignis, Begründung und vorgesehenen Ansprechpartner in `data/signale/YYYY-MM-DD.md`.

## Kanalbezogene Übergabe

Erstelle Kontaktentwürfe für passende LinkedIn-Profile. Übergib Einladungen an og-linkedin-connect und Nachrichten oder Kommentare an og-linkedin. Keine Mailanbieter voraussetzen.

Ein Signalbericht sendet keine Nachrichten. Jede ausgewählte Aktion braucht Empfänger, finalen Text und konkrete Freigabe. Ohne geeigneten Anlass keinen Gratulations- oder Problempitch erfinden.

## Wiederholung und Bericht

Bei erneutem Aufruf nur neue oder geänderte Ereignisse hervorheben. Kontaktstatus und Antworten aus dem Register berücksichtigen. Wiederkehrende Recherche kann og-linkedin-agent-teams auf ausdrücklichen Wunsch einrichten. Ohne Scheduler bleibt der Skill manuell. Bericht mit Anzahl geprüfter Quellen, passender Ereignisse, bereits bekannter Kontakte und vorbereitetem Paket beenden.

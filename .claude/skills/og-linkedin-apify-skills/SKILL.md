---
name: og-linkedin-apify-skills
description: "Passende Apify-Actors für Leadquellen, Beiträge, Wettbewerber oder Signale auswählen, lesend testen und Ergebnisse in die Kontaktarbeit übernehmen."
---

# Apify-Recherche für Outreach nutzen

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Verbindung und Auswahl

Prüfe eine vorhandene Apify-MCP- oder CLI/API-Anbindung. Nutze das wirkliche Tool-Inventar und die offiziellen Actor-Beschreibungen. Wenn keine Verbindung besteht, leite zur Anbieter-Einrichtung in `docs/werkzeuge.md` und zur aktuellen offiziellen Apify-Dokumentation. Schlüssel im Secret-Speicher halten. Keine Drittanbieter-Skills als installiert behaupten.

Ordne den Auftrag einem Recherchebereich zu:

| Bereich | Ergebnis für Outreach |
|---|---|
| Leadquellen | Firmen, Webseiten und öffentlich verfügbare Ansprechpartner aus passenden Verzeichnissen. |
| Wettbewerber | Belegte Inhalte, Preise und Positionierung der ausgewählten Unternehmen. |
| Reputation | Datierte Bewertungen und Erwähnungen als zu prüfende Signale. |
| E-Commerce | Verkäufer, Produkte oder Kategorien für eine konkrete Zielgruppe. |
| Creator-Suche | Personen mit relevantem Themenpublikum und öffentlich belegten Beiträgen. |
| Content-Analyse | Tatsächlich verfügbare Beitragsdaten und Interaktionen. |
| Trends | Datierte Themenentwicklung als Recherchehinweis. |
| Individuelle Webseiten | Strukturierte Daten aus den beauftragten Seiten. |

## Actor-Lauf

1. Suche einen passenden Actor. Prüfe Eigentümer, Beschreibung, Eingabeschema, Ausgabeformat, Preis und Zugriffsvoraussetzungen. Kein Actor garantiert jede Plattform oder vollständige Daten.
2. Begrenze Quellen, Felder und Ergebnismenge auf den Auftrag. Bestätige kostenpflichtigen Umfang, wenn er nicht bereits beauftragt ist.
3. Starte einen kleinen lesenden Lauf über das tatsächliche Tool. Speichere Run-ID. Warte auf den Abschlussstatus; ein gestarteter Job hat noch keine fertigen Ergebnisse.
4. Lies die Dataset-Ergebnisse einschließlich nötiger Seiten/Paginierung. Halte Abdeckung, Fehler und Zeitpunkt fest. Keine erneute kostenpflichtige Ausführung allein wegen verzögerter Ausgabe.
5. Prüfe Stichproben gegen Quellen, normalisiere Firmen und Profil-URLs beziehungsweise Adressen, erkenne Dubletten. Speichere Rohdaten und Laufbeleg unter `data/apify/`.

## Übergabe

Beiträge und Personen an og-lead-borrow oder og-daily-icp-feed übergeben; Auswertungen an og-content-compare.

Ein gescraptes Postfach oder ein öffentliches Profil ist noch kein geprüfter Versandempfänger. Kontaktanlage, Adressprüfung und Freigabe folgen dem jeweiligen Kanal. Der Skill sammelt Daten und startet keine Kontaktkampagne nebenbei.

## Fehler

Bei Zugriffssperre, unklarer Quelle oder fehlenden Rechten stoppen. Kein CAPTCHA- oder Login-Umgehen. Teilresultate mit Einschränkungen liefern. Nutze dokumentierte Actor-Schemas anstelle veralteter fester IDs oder eines ungeprüften Universal-Scrapers.

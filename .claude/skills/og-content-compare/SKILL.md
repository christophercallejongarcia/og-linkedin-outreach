---
name: og-content-compare
description: "Ausgewählte LinkedIn-Profile und Beiträge auf Themen, Formate, sichtbare Resonanz und passende eigene Themenansätze untersuchen."
---

# Wettbewerber-Inhalte vergleichen

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Umfang festlegen

Übernimm genannte Profil-URLs. Falls sie fehlen, frage nach den zu vergleichenden Personen oder Unternehmen und dem Zeitraum. Speichere die Auswahl in `data/wettbewerber.json`. Prüfe Websuche, Browser oder verbundenen Datenanbieter lesend.

## Vergleichbare Stichprobe

Erfasse pro Profil die verfügbaren Beiträge im vereinbarten Zeitraum, beispielsweise die letzten fünf. Notiere URL, Datum, Text, Format und sichtbare Interaktionen. Bei Teilabdeckung keine exakte Veröffentlichungsfrequenz behaupten. Fehlende Reichweite bleibt unbekannt.

Untersuche Einstiege, Themen, Beispiele, CTA und erkennbare Diskussionspunkte. Ordne sichtbare Kommentierende nur anhand belegter Rollen ein; keine Käuferquote ableiten.

## Chancen ableiten

Erstelle eine Themenmatrix: in vielen untersuchten Beiträgen vertreten, vereinzelt vertreten, in dieser Stichprobe nicht gefunden. „Nicht gefunden“ bedeutet nicht, dass niemand darüber spricht. Vergleiche bei vorhandenen Daten mit `data/content-analyse.md` aus og-content-reflect.

Schlage eigene Perspektiven vor, die zum Nutzerprofil passen. Erkläre pro Vorschlag die konkrete Beobachtung und die mögliche Ergänzung. Kopiere keine fremden Hooks oder Geschichten in die Stimme des Nutzers.

## Ergebnis

Schreibe `data/wettbewerber-analyse.md` mit Quelltabellen, Stichprobenumfang, Mustern und konkreten Themenideen. Fremde Leistungsdaten werden nicht zu eigenen Erfolgsaussagen. Recherche und Entwürfe sind das Ende dieses Skills; Veröffentlichung benötigt einen separaten Auftrag.

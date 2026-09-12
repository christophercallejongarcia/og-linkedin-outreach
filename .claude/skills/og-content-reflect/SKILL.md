---
name: og-content-reflect
description: "Eigene Beiträge anhand verfügbarer Inhalts- und Leistungsdaten vergleichen und daraus konkrete nächste Themen ableiten."
---

# Eigene LinkedIn-Inhalte auswerten

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Datenbasis

Nutze das eigene Profil aus der Einrichtung und den gewünschten Zeitraum. Über Browser, bereitgestellte Exporte oder einen verbundenen lesenden Anbieter die erreichbaren Beiträge erfassen. Ziel sind etwa zehn Beiträge, sofern vorhanden; tatsächliche Stichprobe und Lücken dokumentieren.

Erfasse je Beitrag URL, Datum, vollständigen Text oder nachvollziehbaren Auszug, Format, Länge, Thema, Einstieg und CTA. Reaktionen, Kommentare, Reposts und Impressionen nur speichern, wenn sie tatsächlich verfügbar sind. Keine Reichweite schätzen und als gemessen ausgeben.

## Auswertung

1. Vergleiche Beiträge mit hoher und geringer sichtbarer Resonanz innerhalb desselben Zeitraums. Junge Beiträge haben weniger Beobachtungszeit; weise darauf hin.
2. Untersuche Einstieg, Beispiel, Format, Länge, Thema und Veröffentlichungstermin. Zeige konkrete Textstellen als Belege für deine Beobachtung.
3. Berechne Quoten nur mit vorhandenem Nenner. Kommentar-zu-Reaktions-Verhältnis ist nicht Reichweite oder Conversion. Eine gewichtete Interaktionssumme muss als eigene Sortierhilfe bezeichnet werden.
4. Suche wiederkehrende Muster und Gegenbeispiele. Trenne Beobachtung und mögliche Erklärung. Einzelne erfolgreiche Beiträge beweisen keinen kausalen Effekt.

## Ausgabe

Schreibe `data/content-analyse.md` mit Zeitraum, Stichprobe, Quelltabellen, stärkeren und schwächeren Beispielen sowie drei begründeten Ideen für nächste Beiträge. Jede Idee verbindet ein beobachtetes Muster mit dem Angebot oder Wissen des Nutzers. Keine fremden Erfolge als eigene ausgeben.

Vergleiche auf Wunsch mit og-content-compare. Dieser Skill veröffentlicht nichts. Video- oder YouTube-Daten nur bei eigenem Auftrag und vorhandenen Quellen auswerten; keine unsichtbare CTR oder Watchtime behaupten.

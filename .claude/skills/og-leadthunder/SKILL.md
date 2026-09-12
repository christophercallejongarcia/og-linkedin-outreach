---
name: og-leadthunder
description: "Kommentierende eines LinkedIn-Beitrags direkt über die verfügbare Browseransicht erfassen und eine personalisierte Vernetzungskampagne vorbereiten."
---

# Kommentarbasierte Kontaktkampagne im Browser

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Browserbasierter Durchlauf

Dieser Skill ist der direkte Browserweg für Kommentarlisten. og-lead-borrow kann zusätzlich Reaktionen und externe Datenanbieter einbeziehen. Benötigt werden die Beitrags-URL, eigene Auswahlkriterien und ein angemeldeter Browser.

1. Öffne den Beitrag und lies seinen Inhalt. Lade Kommentare schrittweise nach, bis der vereinbarte Umfang erreicht ist oder keine weiteren sichtbar werden. Halte die tatsächliche Abdeckung fest.
2. Ermittle aus den aktuell sichtbaren Kommentarbereichen Name, Rolle, Profil-Link und Text. Wenn DOM-Lesen verfügbar ist, begrenze es auf den Kommentarcontainer und `/in/`-Links. Keine aus einer älteren Website übernommene CSS-Klasse ungeprüft voraussetzen.
3. Normalisiere Profil-URLs und erkenne Dubletten über die URL, nicht über den Namen. Zweifelhafte oder unvollständige Treffer prüfen; fehlende Profil-URLs nicht erfinden.
4. Vergleiche Rolle und Firma mit den Nutzerkriterien. Ein Schlüsselwort in der Headline ist nur ein erster Filter. Prüfe relevante Profile, bevor du sie qualifizierst.
5. Schreibe die Auswahltabelle mit Quelle, Kontakt-ID und Begründung in `data/leadthunder/`. Lege neue Kontakte über `contact` an und ergänze Notizen.

## Vernetzung

Schreibe pro Person eine kurze Notiz anhand ihres tatsächlichen Kommentars. Vorhandene Angebote oder Materialien nur nennen, wenn der Nutzer sie wirklich bereitstellt. Zeige die komplette Kontaktliste samt Texten als Paket.

Nach Paketfreigabe über og-linkedin-connect ausführen. Der Browser prüft den profilbezogenen Button oder das aktuelle Mehr-Menü, den Inhalt des Notizdialogs und eine erkennbare Versandbestätigung. Keine fest codierte Menüposition, keine automatischen JS-Schleifen zum Massensenden und keine Erfolgsmeldung allein aus dem Schließen eines Dialogs.

## Wiederaufnahme

Vor weiteren Aktionen Register und Inbox lesen. Bereits begonnene oder unklare Aktionen zuerst abgleichen. Speichere bestätigte Ergebnisse sofort. Eine spätere Gesprächsnachricht bleibt ein neues Paket. Beende mit Anzahl erfasster, qualifizierter, vorbereiteter und ausgeführter Kontakte sowie offenen Fehlern.

---
name: og-linkedin
description: "Profile recherchieren, Kontakte suchen, Nachrichten und Benachrichtigungen lesen oder freigegebene LinkedIn-Aktionen ausführen."
---

# LinkedIn im Browser bedienen

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Einstieg und Browserprüfung

Übernimm konkrete Profil-URLs und die gewünschte Aktion aus dem Auftrag. Prüfe im Tool-Inventar, ob du Tabs auflisten, navigieren, Seiten lesen, Eingaben machen und klicken kannst. Lies die tatsächlichen Parameter. Claude Code kann seine eingerichtete Chrome-Verbindung nutzen; Codex seine verfügbare Browser-/Computer-Use-Anbindung. Prüfe lesend das angemeldete eigene Konto. Bei fehlendem Login übernimmt der Nutzer die Anmeldung.

## Profile und Personen suchen

1. Verwende eine vorhandene LinkedIn-Registerkarte oder öffne eine. Suche mit Rolle, Firma, Region und Kriterien aus dem Nutzerprofil.
2. Öffne jeden relevanten Treffer. Erfasse Name, Profil-URL, Firma, Rolle, Beschreibung und relevante belegte Erfahrung. Unbekannte Angaben bleiben offen.
3. Gleiche Profil-URL und Register ab. Lege neue passende Kontakte über `contact` an; speichere Fundstelle und Qualifizierung über `note`.
4. Liefere eine Tabelle mit Kontakt-ID, Profil, Kriterium, Quelle und vorgeschlagenem nächsten Schritt.

## Einladungen, Nachrichten und Kommentare

Für eine Einladung verwende den vollständigen Skill og-linkedin-connect. Bei Nachrichten prüfe zuerst die bestehende Verbindung und den Gesprächsverlauf. Für Kommentare lies den ganzen Beitrag und verwende dessen konkrete URL als Ziel.

Schreibe die endgültigen Texte aus dem Nutzerangebot und dem tatsächlichen Anlass. Erstelle ein Freigabepaket mit `connect`, `message` oder `comment`. Nach dessen Freigabe reserviere die einzelne Aktion. Öffne das richtige Ziel, prüfe Empfänger und Eingabefeld, trage den freigegebenen Text ein und sende einmal. Lies danach die Bestätigung. Ein geschlossenes Fenster allein belegt keinen Erfolg.

## Inbox und Benachrichtigungen

Öffne die Nachrichtenansicht, ordne neue Antworten anhand der Profil-URL zu und dokumentiere sie mit `reply`. Verwende einen stabilen Beleg aus Gesprächs-URL, Nachrichtenzeit und Text oder einer Nachrichten-ID. Bereits erfasste Antworten nicht als neu behandeln. Bei Abmeldewunsch zusätzlich `block`. Antworten als neues Paket entwerfen und prüfen lassen. Benachrichtigungen lesen erlaubt keine beiläufigen Likes oder Annahme neuer Einladungen.

## Abschluss

Berichte getrennt recherchierte Profile, vorbereitete Aktionen, bestätigte Ausführungen und unklare Fälle. Auf Wunsch kann eine vorhandene Recording-Funktion Bildschirmmaterial aufzeichnen; vorher Ausschnitt und sichtbare Kontaktdaten mit dem Nutzer klären. Keine Recording-Funktion behaupten, die im Tool-Inventar fehlt.

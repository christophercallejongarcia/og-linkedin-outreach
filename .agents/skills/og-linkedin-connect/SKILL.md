---
name: og-linkedin-connect
description: "Eine konkrete Liste von LinkedIn-Profilen mit geprüften Notizen zur Vernetzung vorbereiten und nach Paketfreigabe im Browser ausführen."
---

# Personalisierte Vernetzungsanfragen

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Eingaben

Benötigt werden Profil-URLs oder vorhandene Kontakt-IDs, das eigene Konto und pro Person ein belegter Anlass. Lies Profil und bisherigen Kontaktstand. Bereits verbundene Personen, ausstehende Einladungen und gesperrte Kontakte nicht erneut einladen. Erstelle eine Notiz in der Sprache und Stimme des Nutzerprofils. Lies die aktuell sichtbare Zeichengrenze der Oberfläche und prüfe den endgültigen Text vor der Freigabe.

## Paket erstellen

Erfasse Kontakte mit Quelle und erstelle je Empfänger genau eine `connect`-Aktion. Das Ziel ist seine Profil-URL. Für eine Einladung ohne Notiz ist `text` leer. Zeige die vollständige Liste samt Notizen und eigenem Absenderkonto. Nach ausdrücklicher Paketfreigabe jede Aktion einzeln reservieren.

## Browserablauf je Profil

1. Navigiere zum Profil. Lies den aktuellen Seitenzustand und vergleiche den Namen samt Firma mit dem beauftragten Kontakt.
2. Suche den profilbezogenen Button „Vernetzen“/„Connect“. Vermeide gleichnamige Buttons in Empfehlungen oder Seitenleisten.
3. Wenn er unter „Mehr“/„More“ liegt, öffne das Menü und identifiziere den Eintrag anhand seines aktuellen Texts. Keine festen Menüindizes oder Bildschirmkoordinaten übernehmen.
4. Manche Oberflächen senden beim ersten Klick direkt eine Einladung. Wenn eine Notiz beauftragt ist und der Weg keinen prüfbaren Notizdialog bietet, stoppe diese Aktion. Nicht stillschweigend ohne Notiz senden.
5. Öffne „Notiz hinzufügen“, trage den freigegebenen Text über das verfügbare Eingabewerkzeug ein und lies den Feldinhalt zurück. Bei React-Feldern muss der Wert auch im UI-Zustand ankommen; bevorzuge die dokumentierte Eingabefunktion. DOM-Eingriffe nur, wenn die Laufzeit sie unterstützt und die aktuelle Seite geprüft ist.
6. Klicke auf den eindeutig zugeordneten Versandbutton. Prüfe eine ausdrückliche Versandbestätigung oder den neuen Einladungsstatus. Dokumentiere Erfolg, belegten Fehler oder Unklarheit.

## Sonderfälle

Kein Vernetzen-Eintrag: als nicht ausführbar melden. Deaktivierter Versandbutton: Inhalt und Begrenzung prüfen, keine schnelle Klickfolge. Timeout nach Klick: `unknown`, im Konto abgleichen und nicht erneut senden. Plattformgrenze oder Sicherheitsabfrage: stoppen und den Nutzer informieren.

Speichere Folgeideen mit `note`, etwa Annahme prüfen. Eine spätere Nachricht nach Annahme benötigt ihr eigenes geprüftes Paket. Der Skill startet keinen automatischen Versandplan.

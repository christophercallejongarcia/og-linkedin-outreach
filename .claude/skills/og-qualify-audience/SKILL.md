---
name: og-qualify-audience
description: "Personen aus Kommentaren und Reaktionen auf eigene LinkedIn-Beiträge nach den eigenen Kundenkriterien bewerten."
---

# Reaktionen auf eigene Beiträge qualifizieren

## Projekt und erster Aufruf

Dieser Skill gehört zu `og-linkedin-outreach`. Wenn neben dieser SKILL.md eine `PROJECT_ROOT`-Datei liegt, lies daraus den gebundenen Projektpfad. Sonst liegt die Projektwurzel drei Verzeichnisse über diesem Skill-Ordner. Prüfe dort `agent.json` auf den Namen `og-linkedin-outreach`; verwende kein anderes Kontaktregister. Alle folgenden Projektpfade sind relativ zu dieser geprüften Wurzel, alle Shell-Befehle laufen dort.

Lies `AGENTS.md`, Nutzerprofil und Registerstand. Fehlt `data/profil.json`, führe zuerst `og-linkedin-setup` aus. Der vollständige Kanalablauf dieses Skills steht unten. Gemeinsame Registerbefehle und Freigaben stehen in [references/register-und-freigabe.md](references/register-und-freigabe.md); vor Kontaktänderungen oder externen Aktionen lesen. Werkzeugzugänge werden bei Bedarf anhand `docs/werkzeuge.md` geprüft.

## Eingaben und Kriterien

Prüfe, dass die angegebene URL ein eigener Beitrag ist; falls nicht, nutze og-lead-borrow. Lies Zielgruppenprofil und Ausschlusskriterien. Falls ein Punktesystem gewünscht ist, vereinbare Kriterien und Schwellen vor der Bewertung und speichere sie in `data/audience-kriterien.json`. Keine fremden Rollen, Umsätze oder Standardpunkte als Nutzerkriterien übernehmen.

## Erfassen und bewerten

Lies den Beitrag sowie erreichbare Kommentare und Reaktionen über Browser oder einen geprüften lesenden Datenanbieter. Halte Begrenzungen bei Nachladen oder Datenzugriff fest. Speichere Name, Profil-URL, Rolle, Firma, Interaktion, Kommentartext und Quelle in `data/audience/`.

Prüfe jeden Treffer anhand der Kriterien. Liefere pro Person Belege und eine Entscheidung `passend`, `unklar` oder `ausschließen`. Bei vereinbartem Scoring jede Punktevergabe ausweisen. Eine Reaktion ist ein Anlass für Prüfung, keine behauptete Kaufabsicht. Fehlende Felder werden nicht zugunsten eines hohen Scores ergänzt.

## Übergabe an die Kontaktarbeit

Lege passende neue Kontakte im Register an. Notiere Beitragsbezug, Kriterien und Ergebnis; behalte bestehende Kontakt-IDs. Zeige auch unklare und ausgeschlossene Treffer mit Gründen.

Für passende Kontakte bereite eine Vernetzungsnotiz oder bei bestehender Verbindung eine Nachricht vor. og-linkedin-connect führt freigegebene Einladungen aus, og-linkedin Nachrichten. Die Bezugnahme auf den eigenen Beitrag muss zur tatsächlichen Interaktion passen.

Dieses LinkedIn-Paket hält seine eigene Zielgruppe und sein eigenes Register. Die E-Mail-Route gehört zum getrennten Coldmailing-Paket und ist kein automatischer Folgeschritt. Keine Kontakte oder Daten dorthin kopieren.

## Ergebnis

Speichere Quellen, Bewertung, Auswahl und Paketverweise in `data/audience/`. Liefere keine unbelegten Conversion-Versprechen. Offene Kontaktaktionen bleiben bis zur Paketfreigabe Entwürfe.

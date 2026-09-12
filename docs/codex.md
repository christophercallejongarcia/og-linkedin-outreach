# Start mit Codex

Öffne diesen Repo-Ordner als Arbeitsordner in Codex oder starte im Terminal `codex` darin. Codex liest AGENTS.md und findet den Einstieg unter `.agents/skills/`. Der Skill heißt wie das Repo; rufe ihn mit `$` und seinem Namen auf oder schreibe: „Richte diesen OG-Agenten mit mir ein.“

In der Codex-CLI können HTTP-MCPs mit `codex mcp add NAME --url URL` hinzugefügt werden. OAuth wird bei unterstützten Servern über `codex mcp login NAME` eingerichtet. Prüfe die aktuelle Laufzeit und Anbieteranleitung, bevor du Einstellungen änderst. API-Key-Header gehören in die Secret-/Umgebungsverwaltung, nicht in veröffentlichte Projektdateien.

Für LinkedIn braucht deine Codex-Umgebung zusätzlich Browser-/Computer-Use-Werkzeuge. Eine reine CLI-Sitzung hat nicht durch das Klonen dieses Repos Zugriff auf deinen angemeldeten Chrome. Nutze die Browserintegration deiner Desktop-/IDE-Umgebung oder richte eine passende unterstützte Verbindung ein. Lass den Agenten das Tool-Inventar und eine Leseaufgabe prüfen. Das Paket verwendet keine fest erfundenen Tool-Namen und installiert keine fremde Browserintegration heimlich.

In einer Umgebung mit sichtbarem Chrome-Zugriff öffnest du LinkedIn und meldest dich selbst an. Erst nach erfolgreichem Lesetest ist dieser Weg bereit. Falls nur Recherchetools verfügbar sind, kann der Agent recherchieren und Entwürfe vorbereiten, aber keine Browseraktionen behaupten.

Quellen: https://learn.chatgpt.com/docs/build-skills · https://learn.chatgpt.com/docs/agent-configuration/agents-md · https://learn.chatgpt.com/docs/browser?surface=app · https://developers.openai.com/codex/mcp

# Start mit Claude Code

Installiere Claude Code nach der offiziellen Anleitung und melde dich an. Öffne den entpackten oder geklonten Repo-Ordner mit `claude`. Bestätige nur ein Projekt, dessen Inhalt du geprüft hast.

Schreibe: „Richte diesen OG-Agenten mit mir ein. Prüfe vorhandene Verbindungen und beginne mit einer Leseaufgabe.“ Das Repo lädt gemeinsame Regeln über CLAUDE.md und stellt seinen Einstieg unter `.claude/skills/` bereit. Der Skill heißt wie das Repo und kann mit `/` aufgerufen werden.

Für MCP-Verbindungen unterstützt Claude Code HTTP-Server: `claude mcp add --transport http NAME URL`. Nutze die konkrete Anbieter-Dokumentation in werkzeuge.md. Authentifiziere OAuth-Verbindungen in `/mcp`. API-Key-Verbindungen entsprechend der Anbieteranleitung einrichten; Geheimnisse nicht in dieses Repo schreiben.

Für LinkedIn: Claude-in-Chrome-Erweiterung, unterstützter Chromium-Browser und ein geeigneter direkter Anthropic-Zugang sind nötig. Starte `claude --chrome` und prüfe `/chrome`. API-Key-/Drittanbieter-Zugang allein ersetzt diese Chrome-Anmeldung nicht. Login und CAPTCHA führst du selbst aus. Siehe die aktuellen Voraussetzungen der Chrome-Doku.

Quellen: https://code.claude.com/docs/en/setup · https://code.claude.com/docs/en/skills · https://code.claude.com/docs/en/mcp · https://code.claude.com/docs/en/chrome

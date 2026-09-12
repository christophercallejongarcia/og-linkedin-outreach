# Browser und Recherche verbinden

Für LinkedIn brauchst du ein eigenes angemeldetes Konto und eine Browser-Anbindung, die Seiten lesen, Eingaben machen und Klicks ausführen kann. Prüfe die vorhandenen Funktionen zuerst. Dieses Repo installiert keinen Browser-Server und übernimmt keinen Login.

- Claude Code: docs/claude-code.md beschreibt die offizielle Chrome-Anbindung.
- Codex: docs/codex.md beschreibt die Prüfung der verfügbaren Browser-/Computer-Use-Funktionen. Ein CLI ohne Browserwerkzeug kann recherchierte Daten verarbeiten und Texte erstellen, aber keine LinkedIn-Oberfläche bedienen.
- Recherche: vorhandene Websuche oder Browser nutzen. Optional [Tavily MCP](https://docs.tavily.com/documentation/mcp) unter https://mcp.tavily.com/mcp/ per OAuth/API-Key verbinden. Tavily ist Recherche, kein LinkedIn-Versandwerkzeug.

Lass den Nutzer Login und Sicherheitsabfragen selbst abschließen. Prüfe danach lesend das eigene Profil und speichere in data/verbindungen.json Kontoreferenz, vorhandene Fähigkeiten und Testdatum, ohne Cookies oder Tokens. Ein Lesezugriff beweist keine Schreibfähigkeit. Den ersten freigegebenen Schreibschritt einzeln durchführen und sein Ergebnis kontrollieren.

Bei fehlendem Zugriff Entwürfe und Register weiterbearbeiten, die externe Ausführung als offen melden. Keine Klicks auf Verdacht. Nach Seitenwechseln den aktuellen Zustand neu lesen. Wenn LinkedIn die Aktion einschränkt, stoppen. Keine festen angeblich sicheren Tageslimits oder Umgehungen verwenden.

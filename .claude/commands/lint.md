---
description: Run a health check on the wiki
---

Perform a comprehensive health check on the wiki/ directory:
1. Scan for broken [[wiki-links]] (links pointing to non-existent pages).
2. Identify orphan pages (pages not linked to by any other page).
3. Check for pages missing the required YAML frontmatter (title, type, sources, related, created, last-updated).
4. Identify stale pages (those not modified in the last 30 days).
5. Detect potential contradictions between pages.

Report the findings as a structured list. Do not make any fixes; instead, present the issues and ask for permission to address them.

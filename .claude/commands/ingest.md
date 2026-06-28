---
description: Ingest new files from raw/ into wiki/
---

For each unread file in raw/ (skipping any that have already been summarized into a source-summary page in wiki/):
1. Read the file thoroughly.
2. Write a new source-summary page in wiki/ following the project guidelines.
3. Create or update relevant concept, project, or person pages in wiki/ based on the information.
4. Cross-link new and existing pages using [[wiki-links]].
5. Update wiki/index.md to reflect new pages.
6. Append a timestamped entry to wiki/log.md noting the ingestion.

Process 5-10 sources per run. If $ARGUMENTS is provided, limit the number of sources processed to that number.

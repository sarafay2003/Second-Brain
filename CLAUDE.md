# Project Guidelines: Second Brain Vault

## Project Structure
- `raw/`: Storage for raw imports and exports from external systems.
    - `claude-exports/`: Exports from Claude conversations.
    - `granola-exports/`: Exports from Granola.
    - `notion-exports/`: Exports from Notion.
- `wiki/`: The curated, structured knowledge base.
    - `concepts/`: Atomic notes on specific concepts.
    - `people/`: Information and notes regarding specific people.
    - `projects/`: Documentation and tracking for various projects.
    - `index.md`: The central map and entry point for the wiki.
    - `log.md`: A chronological record of notes and vault activity.

## Page Conventions
Every wiki page must include YAML frontmatter with the following fields:
- `title`: The name of the page.
- `type`: One of: `concept`, `entity`, `source-summary`, `comparison`, `project`, `person`.
- `sources`: List of origin sources for the information.
- `related`: Links to related pages.
- `created`: Date of creation.
- `last-updated`: Date of last modification.

General requirements:
- Use `[[wiki-links]]` for internal navigation.
- Maintain atomicity: one idea per page.
- Use a consistent heading structure across all pages.

## Style Guide
- Use clear and concise prose.
- Prefer bullet points over long paragraphs for readability.
- Attribute every claim explicitly to its source.
- Explicitly note any contradictions found between sources.

## Domain Context
This vault supports a final semester student focused on software and tech, specifically AI, AWS, Docker, Kubernetes, Cloud, and DevOps, alongside growth and marketing. The user is currently creating projects for growth and seeking internships or jobs. The primary goal is to track learning over time and document how various topics, technologies, and software link to ideas, real-world projects, and documentation. By mapping these connections, the user aims to get smarter and ensure they do not make the same mistake again.

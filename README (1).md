# 🧠 AI Second Brain with Claude Code

A personal knowledge management system built with Obsidian and Claude Code, following the Andrej Karpathy second brain methodology.

---

## 🚀 Features

- **Knowledge Ingestion** — Import and convert exports from Claude, Notion, and Granola into clean Markdown
- **AI Synthesis** — Claude Code reads your raw notes and builds structured wiki pages automatically
- **Slash Commands** — Four custom commands to ingest, query, lint, and log your knowledge base
- **Obsidian Graph** — Visualize connections between concepts, people, and projects
- **YAML Frontmatter** — Every wiki page is structured with metadata for consistency and queryability

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Knowledge Base | Obsidian |
| AI Assistant | Claude Code |
| Scripting | Python |
| Source Tools | Claude.ai, Notion, Granola |

---

## 📁 Vault Structure

```
second-brain/
├── raw/                  # Raw imports from external tools
│   ├── claude-exports/
│   ├── granola-exports/
│   └── notion-exports/
├── wiki/                 # Curated, synthesized knowledge base
│   ├── concepts/
│   ├── people/
│   └── projects/
├── content/
├── journal/
├── CLAUDE.md             # Claude Code context and slash command definitions
└── convert_json.py       # Converts JSON exports to Markdown
```

---

## ⚡ Slash Commands

| Command | What It Does |
|---------|--------------|
| `/ingest` | Processes new files from `raw/` and creates wiki pages |
| `/query` | Synthesizes an answer from across the wiki |
| `/lint` | Health check — finds broken links, orphan pages, missing frontmatter |
| `/log` | Appends a timestamped entry to `wiki/log.md` |

---

## ⚙️ Getting Started

### Prerequisites
- [Obsidian](https://obsidian.md) installed
- [Claude Code](https://claude.ai/code) installed and authenticated

### 1. Clone the repository

```bash
git clone https://github.com/sarafay2003/second-brain.git
cd second-brain
```

### 2. Open in Obsidian

Open the `second-brain/` folder as a vault in Obsidian.

### 3. Open in Claude Code

```bash
claude .
```

Claude will automatically load `CLAUDE.md` and be ready to use slash commands.

### 4. Convert your exports

```bash
python convert_json.py
```

Then run `/ingest` in Claude Code to populate your wiki.

---

## 👤 Author

**Syed Abdul Rafay**
Software Engineering Graduate — Bahria University Karachi
[GitHub](https://github.com/sarafay2003)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

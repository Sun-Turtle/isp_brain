# AGENTS.md

You are an AI agent working with the ISP Brain knowledge graph.

## Graph structure

- `index.md` lives at project root
- 5 domain dirs under `graph/`: `identity/`, `knowledge/`, `decisions/`, `tasks/`, `resources/`
- One level of directories only — no subdirectories within domains
- Files follow prefix naming: `topic-subtopic-descriptor.md` (e.g. `regulatory-ofcom-general-conditions.md`)
- Hub pages sit at `graph/{domain}.md` (e.g. `graph/identity.md`, `graph/knowledge.md`) — one level above their children for visibility
- Child files live inside `graph/{domain}/` (e.g. `graph/identity/company-details.md`)
- "See also" use list-item links (`- [link](path.md)`) — cross-references, not structural
- Config in `.iwe/config.toml` — `refs_extension = ".md"`

## IWE CLI

``` bash
iwe find                         # List all docs
iwe tree                         # Show hierarchy
iwe find -k index                # Get index doc
iwe find --filter 'tags: home'   # Filter by frontmatter
```

## Conventions

- YAML frontmatter with `status`, `priority`, `tags` on every doc
- Links use `.md` extension, relative from source file location
- Split files when they exceed ~10,000 chars or ~300 lines

# AGENTS.md

You are an AI agent working with the ISP Brain knowledge graph.

## Graph structure

- `index.md` lives at project root
- 5 domain dirs under `graph/`: `identity/`, `knowledge/`, `decisions/`, `tasks/`, `resources/`
- Hub pages sit at `graph/{domain}.md` — one level above their children
- Child files live inside `graph/{domain}/`, no subdirectories
- Files follow prefix naming: `topic-subtopic-descriptor.md`
- Inclusion links (bare `[link](path.md)` on own line) = parent-child relationships
- List-item links (`- [link]`) = cross-references only

## Golden rules

- **Proactive modifications** - if taking an action, modify the relevant domains of the Knowledge Graph, even if not prompted to do so.
- **Do not duplicate** resource content into knowledge — add context and labeling instead
- **Link everything** — every file should link back to at least one hub, and link to related content
- **Log decisions that matter** — structural/business choices with trade-offs; skip file edits or git pushes
- **Descriptions short, context generous** — why, when, by whom, what relationships
- **Be opinionated** — point out what looks broken/not optimised

## Conventions

- [Operating conventions](graph/knowledge/graph-conventions.md) — workflows, normalize fixup, split guidelines
- [Frontmatter schema](graph/knowledge/graph-frontmatter-schema.md) — valid status, priority, tag values
- [File naming decision](graph/decisions/flat-file-convention.md) — why we chose this structure

## Personas

Adopt a persona for focused work:

- [**Crystallise**](graph/identity/personas.md) — deduplicate, condense, link instead of duplicate
- [**Maintainer**](graph/identity/personas.md) — fix links, syntax, metadata, IWE feature audit

## Quick CLI

```bash
iwe find                         # List all docs
iwe tree                         # Show hierarchy
iwe find -k index                # Get index doc
iwe find --filter 'tags: home'   # Filter by frontmatter
iwe find -k graph/conventions    # Operating conventions (IWE key = path)
```

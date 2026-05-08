---
status: active
priority: high
tags:
  - knowledge
  - graph
  - schema
created: 2026-05-07
---

# Frontmatter Schema

Valid values for YAML frontmatter fields across all documents.

## created

Date when the document was first created. Format: `YYYY-MM-DD`. Present on all documents.

```yaml
created: 2026-05-07
```

## status

| Value | Meaning |
|---|---|
| `active` | Current, in use |
| `draft` | In progress, not yet ready |
| `deprecated` | No longer current, kept for reference |

## priority

| Value | Meaning |
|---|---|
| `critical` | Blocks other work, must act |
| `high` | Important, should be next |
| `medium` | Useful but not urgent |
| `low` | Nice to have |

## tags

Tags are lowercase, single words or kebab-case. Every doc should have at least one domain tag (`identity`, `knowledge`, `decisions`, `tasks`, `resources`) plus `home` if it's a hub page.

Common tags:
- `home` — hub pages only
- `regulatory`, `technical`, `market`, `policy`, `procedure` — knowledge domains
- `legal`, `financial`, `infrastructure`, `contract`, `people` — resource domains
- `decision`, `architecture`, `log` — decision types
- `risk`, `compliance`, `network`, `assets`, `strategy` — cross-cutting
- `research`, `playbook`, `guide` — reference materials
- `graph`, `cli`, `conventions`, `schema`, `workflow` — graph meta-docs

## Example

```yaml
---
status: active
priority: high
tags:
  - knowledge
  - regulatory
  - compliance
created: 2026-05-07
---
```

## See also

- [Graph Conventions](graph-conventions.md)

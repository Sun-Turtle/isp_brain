---
status: active
priority: high
tags:
  - knowledge
  - graph
  - conventions
  - workflow
created: 2026-05-07
---

# Graph Conventions

Operating conventions for maintaining this IWE knowledge graph.

## Inclusion Links

Bare markdown link on its own line = parent-child relationship in IWE. These build the graph hierarchy.

**The parent page has the link to the child.** The child does NOT link back — IWE infers the reverse relationship (`includedBy`) automatically.

```markdown
# Identity (parent)
[Company Details](company-details.md)   ← child
[Incorporation](incorporation.md)       ← child
```

Hub files use this pattern to list their children. "See also" sections use list-item links (`- [link]`) for cross-references — these do NOT create parent-child relationships.

| Format | IWE treats as | Used for |
|---|---|---|
| `[Link](path)` (bare, own line) | Inclusion link — parent-child | Hub navigation, hierarchy |
| `- [Link](path)` (in a list) | Inline reference | See also, cross-references |

## iwe normalize fixup

`iwe normalize` collapses consecutive bare links onto one line, breaking inclusion links. After running normalize, restore one-link-per-line in hub pages (`graph/{domain}.md`).

## Adding content

1. Create file in the correct domain directory
2. Name it `topic-subtopic-descriptor.md`
3. Add YAML frontmatter with `status`, `priority`, `tags`
4. Add an inclusion link from the hub page (`graph/{domain}.md`)
5. Add relevant cross-references from the content file
6. Verify with `iwe tree`

## When to split a file

Rough guideline — not a hard rule:
- Split at ~10,000 characters or ~300 lines
- Use `topic-aspect.md` pattern (e.g. `product-upc-overview.md`, `product-upc-methodology.md`)
- The prefix groups related files together

## What to log as a decision

Log in `graph/decisions/` when:
- Structural choice (how domains are organised, naming conventions)
- Business logic choice (what we do, who we target, how we operate)
- Trade-offs were considered and rejected

Do NOT log:
- File edits or git pushes
- Routine updates (dates changing, typos fixed)
- Information that should just go in knowledge

## What goes in knowledge vs resources

| Domain | What lives here |
|---|---|
| knowledge | Facts, rules, context — regulatory, technical, market, policies, procedures, meta-graph docs, research context |
| resources | Raw assets — full documents, files, tools, people, money, contracts, CLI references |

Never duplicate resource content into knowledge. Instead, provide context: what is this resource? In which context is it useful? How is it labelled/tagged? Time relevance?

[Frontmatter Schema](graph-frontmatter-schema.md)

## See also

- [File Naming Convention](../decisions/flat-file-convention.md)
- [Graph CLI Reference](../resources/graph.md)

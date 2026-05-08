---
status: active
priority: high
tags:
- decisions
- architecture
- graph-structure
created: 2026-05-07
---

# File Naming Convention: Flat Structure

## Context

After settling on 5 domains (see [Domain Structure: 5 Domains](domain-structure.md)), the graph still had deeply nested directories (up to 4 levels: `graph/knowledge/regulatory/ofcom-general-conditions.md`). Moving files between directories causes noisy git diffs and makes it harder to track changes.

## Problem

Deep nesting creates friction:

- **Git diff noise** — moving a file from `knowledge/regulatory/` to `knowledge/compliance/` shows a delete + add rather than a rename
- **Cognitive overhead** — authors must decide which subdirectory a file goes in, and whether to create a new one
- **Discovery friction** — `iwe tree` and `iwe find --filter` already handle discovery; directory hierarchy adds little value on top

The decision from [Domain Structure: 5 Domains](domain-structure.md) noted: *"Tag-based navigation only — IWE supports this, but directory hierarchy is still useful for human browsing and `iwe tree`"*. With IWE's inclusion links now working properly (bare `[link](path)` on its own line), the graph structure handles hierarchy better than filesystem directories do.

## Decision

Adopt a flat file structure with a prefix-based naming convention:

1.  **`index.md`** lives at project root
2.  **Domain directories** under `graph/` — one level only: `graph/identity/`, `graph/knowledge/`, `graph/decisions/`, `graph/tasks/`, `graph/resources/`
3.  **No subdirectories** within domain dirs
4.  **Naming convention**: `topic-subtopic-descriptor.md`

Examples:

```
graph/knowledge/regulatory.md
graph/knowledge/regulatory-ofcom-general-conditions.md
graph/knowledge/technical-network-topology.md
graph/resources/financial.md
graph/resources/financial-accounts.md
```

### When to split a file

Agents should use judgment, but a rough guideline:

- **Split threshold**: ~10,000 characters or ~300 lines of content
- **Split pattern**: `topic-aspect.md`, e.g. `product-upc-overview.md`, `product-upc-methodology.md`
- The prefix groups related files together in directory listings and `iwe tree`
- This is a guideline, not a hard rule — if a file feels too long or covers two distinct concerns, split it

## Alternatives considered

- **Deep nesting** — old approach; caused git diff noise and placement deliberation
- **All files flat in `graph/`** — loses the 5-domain grouping entirely, making `ls graph/` overwhelming
- **Tag-only organisation** — works for IWE queries but directory listing becomes unusable

## Impact

- Cleaner git diffs (file moves become `git mv` renames)
- No deliberation about subdirectory placement
- `iwe tree` and `iwe find` remain the primary discovery tools
- Domain grouping preserved for human browsing

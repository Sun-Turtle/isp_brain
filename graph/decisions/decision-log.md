---
status: draft
priority: medium
tags:
- decisions
- log
---

# Decision Log

## Format

``` markdown
## YYYY-MM-DD: Title

**Context**: What prompted the decision
**Decision**: What was chosen
**Rationale**: Why
**Alternatives**: What else was considered
```

## 2026-05-05: Flat file naming convention

**Context**: Deep nesting caused git diff noise and placement deliberation. **Decision**: Adopt flat structure — one level of domain dirs, files named `topic-subtopic-descriptor.md`. **Rationale**: Cleaner diffs, no subdirectory decisions, `iwe tree` handles discovery. **Details**: See [File Naming Convention: Flat Structure](flat-file-convention.md).

## 2026-05-04: Collapsed 7 domains to 5

**Context**: Original 7 domains (direction, health, identity, knowledge, operations, relationships, resources) had fuzzy boundaries — many topics fit 2–3 domains. **Decision**: Collapse to identity, knowledge, decisions, tasks, resources. **Rationale**: Mutually exclusive boundaries, less deliberation when placing files. **Details**: See [Domain Structure: 5 Domains](domain-structure.md).

## Format

``` markdown
## YYYY-MM-DD: Title

**Context**: What prompted the decision
**Decision**: What was chosen
**Rationale**: Why
**Alternatives**: What else was considered
```

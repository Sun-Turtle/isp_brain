---
status: active
priority: medium
tags:
  - home
  - graph
  - cli
---

# Graph

CLI reference, setup instructions, and conventions for working with this IWE knowledge graph.

## Docs/Links
```bash
# Docs
https://github.com/iwe-org/iwe
https://iwe.md/docs/

# Project Examples
https://github.com/iwe-org/pkm-demo
https://github.com/iwe-org/seventeen-centuries
```

## Installation
```bash
brew tap iwe-org/iwe
brew install iwe
```


## Setup

```bash
iwe init                    # Initialize project (if not already done)
```

## Creating Documents

```bash
iwe new "Title"                           # Create from default template
iwe new "Title" --content "Body text"     # With inline content
iwe new "Title" --edit                    # Open in $EDITOR
iwe new "Title" --if-exists override      # Overwrite if exists
```

Template variables: `{{title}}`, `{{slug}}`, `{{today}}`, `{{id}}`, `{{content}}`

## Finding Documents

```bash
iwe find                                  # List all docs
iwe find --filter 'status: active'        # Filter by frontmatter
iwe find --filter 'tags: home'            # Filter by array tag
iwe find --filter 'priority: high'        # Filter by priority
iwe find -k graph/index                   # Retrieve by key
iwe find -f keys                          # Output keys for piping
```

## Counting

```bash
iwe count --filter 'status: active'
iwe count --filter 'tags: regulatory'
iwe count --filter '$or: [{tags: risk}, {tags: compliance}]'
```

## Document Tree

```bash
iwe tree                                  # Show full hierarchy
iwe tree -k doc-key                       # Tree from specific doc
iwe tree -d 2                             # Limit depth
```

## Graph Queries

```bash
iwe find --references graph/index         # Docs referenced by index
iwe find --referenced-by graph/index      # Docs that reference index
iwe find --includes graph/direction       # Inclusion links
iwe find --included-by graph/direction    # Reverse inclusion
```

Depth flags: `--max-depth N`, `--max-distance N` (0 = unbounded)

## Refactoring

```bash
iwe extract doc-key --section "Title"     # Extract section to new doc
iwe inline doc-key --reference "ref-key"  # Inline a referenced doc
iwe rename old-key new-key                # Rename + update refs
iwe delete doc-key                        # Delete doc
```

## Maintenance

```bash
iwe normalize                             # Fix formatting
iwe stats                                 # Graph statistics
iwe export dot                            # Export as Graphviz DOT
iwe export dot -k key -d 2 | dot -Tpng -o graph.png
```

## Output Formats

Most commands support `-f markdown | keys | json`.

## Conventions

- Every directory has a `{name}.md` home node
- 5 top-level domains: identity, knowledge, decisions, tasks, resources
- All queries use `--filter` flag for frontmatter — bare positionals don't work
- Links use relative paths (e.g. `regulatory/regulatory.md`)

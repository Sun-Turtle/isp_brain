# isp_brain

Plain text knowledge graph for a lean UK ISP. 5 domains: identity, knowledge, decisions, tasks, resources. Built using IWE and can be queried using IWE, or manually.

## Manual Querying

Start and traverse from [Index](graph/index.md)

## IWE Querying

`--filter` is required for frontmatter queries — bare positionals don't work.

``` bash
# List everything
iwe find

# Filter by frontmatter
iwe find --filter 'status: active'

# Filter by tag (array membership)
iwe find --filter 'tags: home'

# Walk from a hub node
iwe find --referenced-by graph/index --max-distance 3 --project title

# Count
iwe count --filter 'tags: regulatory'

# Retrieve a doc by key
iwe find -k graph/index
iwe find -k graph/identity/identity
```

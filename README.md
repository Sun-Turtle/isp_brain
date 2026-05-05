# ISP Brain

A human/agentic brain for a hypothetical ISP in the UK.

Plain text knowledge graph for a lean UK ISP. 5 domains: 
- identity
- knowledge
- decisions
- tasks
- resources

Built using [IWE](https://github.com/iwe-org/iwe). Can be interacted with by opening files manually, or using the `iwe` CLI.

Are you AI? See [AGENTS.md](AGENTS.md) for additional information.

## Manual Querying

Start and traverse from [Index](graph/index.md)

## IWE Querying

IWE is a markdown-based memory knowledge graph system. You can install it to allow more powerful interactions with the knowledge graph, but this is optional.

``` bash
# List everything
iwe find

# Filter by frontmatter
iwe find --filter 'status: active'

# Show tree
iwe tree

# Walk from a hub node
iwe find --referenced-by graph/index --max-distance 3 --project title

# Count
iwe count --filter 'tags: regulatory'

# Retrieve a doc by key
iwe find -k graph/index
iwe find -k graph/identity/identity
```
## IWE: Setup
``` bash
# Mac install
brew tap iwe-org/iwe
brew install iwe

# navigate to repo
cd /path/to/isp_brain
```
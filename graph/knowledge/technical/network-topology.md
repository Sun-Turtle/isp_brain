---
status: active
priority: high
tags:
- technical
- network
- architecture
source: extract_me.md
---

# Network Topology

## Customer-facing architecture

```
Customer router
    ↓
Openreach line
    ↓
BT Wholesale (aggregation)
    ↓
Internet
```

## What we own vs what the wholesale partner owns

| We own                             | Wholesale partner owns             |
| ---------------------------------- | ---------------------------------- |
| Billing & positioning              | Core network plumbing              |
| Customer support & tone            | Much of provisioning complexity    |
| Brand & trust                      | Scale economics you don't have yet |
| Router choice / logistics strategy | —                                  |


## Network minimalism (you are not BT yet)

If you must add your own IP layer later:

| Building block                             | Notes                                        |
| ------------------------------------------ | -------------------------------------------- |
| Transit (e.g. Cogent, GTT — examples only) | Buy full transit early; peering can wait     |
| IX (e.g. LINX)                             | Nice-to-have once scale justifies complexity |


Many tiny ISPs skip peering entirely at first and just buy transit. Less glory, fewer surprises.

## Fault handling model

Most access faults are Openreach's world — your win is orchestration:

```
detect → diagnose → ticket Openreach → book engineer → nag customer politely → close loop
```

Goal: minimal human touches on routine paths; humans for edge and angry.

## See also

- [Network Assets](../../resources/infrastructure/network-assets)
- [Openreach supplier relationship](../../relationships/suppliers/openreach)

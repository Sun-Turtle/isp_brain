---
status: active
priority: high
tags:
  - knowledge
  - supplier
  - wholesale
  - voip
  - broadband
created: 2026-05-24
---

# ICUK Telecoms Reseller Platform

ICUK Computing Services Ltd — UK wholesale telecoms, connectivity, and hosting provider founded 2001. 800+ resellers. Privately owned, technically-run (90% of staff in development/support, no commission-based sales). Started as a reseller themselves before building their own network and platform.

Full product catalogue, pricing, and technical specs — see [ICUK Research Dump](../resources/research-supplier-icuk.md).

## Platform Tiers

| Tier | Cost/mo (ex VAT) |
|---|---|
| Telecoms & Connectivity Reseller | £20 |
| Reseller Web Hosting | £20 |
| Enterprise (All-in-One) | £50 |
| Leased Line Reseller | Free (requires Ethernet order) |

No minimum spend, no deposits, no growth targets. Customers you win are your customers — no lock-in, take them if you leave.

## What's in the box

- **Broadband**: FTTP/SoGEA/SoADSL via BT Wholesale and CityFibre. Automated ordering, provisioning, fault handling, real-time diagnostics.
- **Ethernet**: Leased lines up to 10Gbps via Openreach, Sky, BT Wholesale, TalkTalk, Virgin Media, COLT. Rebrandable instant quoting.
- **VoIP**: Hosted VoIP + SIP Trunks, auto-provisioning 100+ devices, drag-and-drop call flow designer, PAYG and bundled minutes, fraud prevention.
- **One Touch Switching**: First-to-market integrated OTS — no direct TOTSCo interaction.
- **API**: REST, single API across all platforms, Swagger docs, no extra fee. Multi-user + IP restrictions.
- **White-label**: Full HTML/CSS customisation of customer Control Panel — not just logo swaps. Rebrandable login, status pages, speed tests, invoicing.
- **Network**: Multi-homed, multi-POP UK. Own RADIUS, own IPs. DDoS protected.

## Key Differentiators

1. Ex-reseller DNA — understands reseller pain points
2. Genuine white-label — full HTML/CSS rebranding
3. Technical culture — not a sales-driven org
4. In-house everything — own network, own Control Panel, own dev team
5. No lock-in — you own your customers
6. Single pane of glass — connectivity, VoIP, hosting from one platform

## Relevance to Sun Turtle

ICUK could compress Sun Turtle's go-to-market puzzle into a single vendor relationship:

- **Wholesale aggregation**: BT Wholesale + CityFibre coverage via one contract, instead of negotiating with BT Wholesale, TalkTalk, and others separately
- **OSS/BSS in the box**: Provisioning, billing, CRM, fault handling, diagnostics — replaces the need to buy Splynx/Sonar/CloudBlue and integrate
- **Customer portal ready**: White-label self-service portal with speed tests, line status, fault checker — exactly what the playbook wants to build
- **VoIP day-1 ready**: Hosted VoIP handles emergency services compliance, auto-provisioning, fraud prevention — removes the "VoIP maybe later" hesitation
- **OTS compliance**: Integrated One Touch Switching reduces Ofcom regulatory burden
- **Cost**: £20/mo platform fee is negligible (less than 1 extra customer)

## Risks

- **Single-supplier concentration**: Broadband, voice, portal, and billing all depend on ICUK. Multi-wholesaler resilience is reduced.
- **Another aggregation layer**: ICUK sits on BT Wholesale/CityFibre — not replacing aggregation, just consolidating it. Margins need comparison against direct BT Wholesale.
- **No sustainability DNA**: No green positioning from ICUK. Sun Turtle's values layer sits entirely on top.
- **CLG vs commercial supplier**: Different structural ethos — fine, but no shared mission.

## Next Steps

- Model pricing at 500/2,000/8,000 customer volumes to compare ICUK margins vs direct wholesale + OSS/BSS
- Evaluate API docs and Control Panel for AI integration feasibility
- Compare OTS handling cost/time vs doing it independently through TOTSCo
- Assess VoIP product viability via ICUK vs deferring VoIP to v2

## See also

- [ICUK Research Dump](../resources/research-supplier-icuk.md)
- [Sun Turtle Playbook](../resources/research-sun-turtle-playbook.md)
- [Technical](technical.md)
- [Market Landscape](market-competitive-intelligence.md)
- [Wholesale Pricing Comparison](private_research-wholesale-pricing-comparison.md) (⚠️ private)

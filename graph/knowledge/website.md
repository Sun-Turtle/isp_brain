---
status: active
priority: high
tags:
  - knowledge
  - website
  - brand
  - operations
created: 2026-05-24
---

# Website

The public-facing website is deployed at `suninternet.co.uk`. Source code in `Sun-Turtle/website` on GitHub.

## Stack

Next.js (App Router) with TypeScript and Tailwind CSS. Statically exported (`output: "export"`). Deployed via Docker (Nginx:alpine) behind a host-level Nginx reverse proxy with Let's Encrypt SSL. See [deployment architecture](infrastructure-website-deployment.md) and [stack decision](../decisions/website-stack.md).

## Pages

| Page | Purpose | Regulatory relevance |
|---|---|---|---|---|
| `/` | Homepage — mission, quick action links, why we're different | Company identity (name, number, trading name disclaimer) |
| `/about` | About us — who we are, why we're doing this | Voluntary; trust-building |
| `/complaints` | Complaints procedure — channel, timeframes, ADR, Ofcom obligations | Mandatory under Ofcom General Conditions |
| `/privacy` | Privacy policy — what we collect, why, who we share with, your rights | Mandatory under UK GDPR |
| `/terms` | Terms and conditions — service, contract, fees, liability, ending the contract | Mandatory under Ofcom General Conditions and Consumer Rights Act 2015 |

The `/open` (financial transparency) page was removed — not ready to publish cost figures until supplier relationships are confirmed and operational costs are real.

## Regulatory gaps (pre-launch tasks)

These items are required before serving customers but are not yet on the website:

- **ADR scheme name**: Once joined, must be displayed on complaints page. Currently a placeholder note. — see [ADR Scheme](company-adr-scheme.md)

The registered office address is held in the knowledge graph but not published on the website — it is not a legal requirement under the E-Commerce Regulations (available via Companies House if needed).

## Design philosophy

- Human-centred: no marketing language, no upselling, no "click here" urgency
- Action-oriented from homepage: a person can do everything useful immediately
- Transparent: finances, code, complaints process all public and linked
- Anti-clutter: no hero images, no carousels, no pop-ups, no cookie banners (we don't set cookies)
- CLG structure acknowledged but not preachy: the footer carries the legal identity quietly

## See also

- [Website Stack Decision](../decisions/website-stack.md)
- [Company Details](../identity/company-details.md)
- [Core Admin Stack](company-core-admin-stack.md)
- [Deployment Architecture](infrastructure-website-deployment.md)
- [Privacy Policy](policies-privacy.md)
- [Terms and Conditions](policies-ts-and-cs.md)
- [Complaints Handling Policy](policies-complaints-handling.md)

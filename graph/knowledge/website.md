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

The public-facing website lives at `suninternet.co.uk` (not yet deployed). Source code in `Sun-Turtle/website` on GitHub.

## Stack

Plain HTML + CSS. No JavaScript, no framework, no build step. See [decision](../decisions/website-stack.md).

## Pages

| Page | Purpose | Regulatory relevance |
|---|---|---|
| `index.html` | Homepage — mission, what we offer, action cards (GitHub, open books, ISP Brain, complaints) | Company identity (name, number, jurisdiction) |
| `open.html` | Financial transparency — costs, staff pay, surplus philosophy, monthly archive | Voluntary; trust-building |
| `complaints.html` | Complaints procedure — channel, timeframes, ADR, Ofcom obligations | Mandatory under Ofcom General Conditions |

## Regulatory gaps (pre-launch tasks)

These items are required before serving customers but are not yet on the website:

- **Privacy policy**: Required under UK GDPR. Must be published before collecting any personal data. Cover what we collect, why, retention periods, third-party sharing, customer rights. — see [Core Admin Stack](company-core-admin-stack.md)
- **Terms & conditions**: Consumer contract for broadband services. Must comply with Consumer Rights Act 2015, Ofcom GCs (contract summaries, renewal notices, switching), distance selling regs. — see [Core Admin Stack](company-core-admin-stack.md)
- **ADR scheme name**: Once joined, must be displayed on complaints page. Currently a placeholder note. — see [ADR Scheme](company-adr-scheme.md)
- **Registered office address**: Currently listed as TBD. Must be added once confirmed.

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
- [Complaints Handling Policy](policies-complaints-handling.md)

---
status: active
priority: high
tags:
  - knowledge
  - company
  - operations
  - compliance
created: 2026-05-08
---

# Core Admin Stack

The minimum operational infrastructure a newly incorporated ISP needs before approaching wholesalers or registering with Ofcom. These are the things suppliers and regulators will ask to see.

## What's in the stack

### Business bank account

Separate from personal finances from day one. Required for:
- Accepting customer payments
- Paying wholesale invoices
- Ofcom/ICO registration (they ask for it)
- Credibility with wholesale partners

Chosen provider: **[Tide](https://www.tide.co/)** — see [decision](../../decisions/company-bank-tide.md) and [Tide notes](company-tide.md). Starling and Monzo Business were tried but both rejected the CLG structure; Tide accepts CLGs.

### GitHub org

Official organisation: [Sun-Turtle](https://github.com/Sun-Turtle) — houses all company code, config, and infrastructure-as-code. Created alongside domain registration to match the brand identity.

### Domain & email

Professional domain matching the company name. Email on that domain — Gmail/Hotmail addresses signal hobbyist to suppliers.

Chosen providers:
- **Domain**: [FreeThought](https://www.freethought.uk/about/) (ethical registrar, UK-based) — see [decision](../../decisions/company-domain.md)
- **Email**: TBD (Google Workspace, Microsoft 365, or Fastmail)

Domain registered: `suninternet.co.uk`

### Bookkeeping

From the first transaction. Chosen provider: [QuickFile](https://www.quickfile.co.uk/) (UK-focused, free tier, 1,000 free invoices/year, REST API) — see [decision](../../decisions/company-bookkeeping.md) and [QuickFile notes](company-quickfile.md).

Must track: director's loan (CLG startup capital), incorporation costs, domain/email subscriptions, and later wholesale invoices.

### Privacy policy

Required under UK GDPR. Must be published on the website before collecting any personal data. Cover:
- What data you collect (customer name, address, contact, payment, IP assignment)
- Why you collect it (service provisioning, billing, legal obligation)
- How long you keep it
- Third-party sharing (wholesale partners, payment processors)
- Customer rights (access, rectification, erasure)

Standard generators (ICO template, Termly, GetTerms) produce passable first drafts. Have a solicitor review before going live with customers.

### Terms & conditions

Consumer contract for broadband services. Must comply with:
- Consumer Rights Act 2015 (fairness, transparency)
- Ofcom General Conditions (contract summaries, renewal notices, switching)
- Distance selling regulations (14-day cooling-off for online signups)

Wholesale suppliers will request a copy during onboarding. Keep the first version lean — you'll iterate once wholesale product details are locked.

### Complaints procedure

Published on website. Must include:
- How to complain (channels, contact details)
- Response timeframes (acknowledge within X, resolve within Y)
- Escalation path (internal review → deadlock letter → ADR scheme)
- ADR scheme name (added once joined)

Required by Ofcom General Conditions and checked by wholesalers during due diligence.

## Timeline

| Item | Effort | When |
|---|---|---|
| Bank account | 1-3 days (online) | Immediately after incorporation |
| Domain + email | 30 minutes | Day 1 post-incorporation |
| Bookkeeping | 2 hours setup | Before first transaction |
| Privacy policy | 2-4 hours (draft) | Before website goes live |
| T&Cs | 4-8 hours (draft) | Before customer onboarding |
| Complaints procedure | 1-2 hours | Before Ofcom notification |

## Wholesale supplier lens

Wholesalers evaluate operational readiness through this stack. Missing pieces = higher risk = delayed onboarding or rejection. Having all six items complete signals you're a real business, not a speculative registration.

## See also

- [CLG Incorporation](company-clg-incorporation.md)
- [Policies hub](policies.md)
- [Complaints Handling Policy](policies-complaints-handling.md)
- [ICO Registration](company-ico-registration.md)
- [Ofcom Notification](company-ofcom-notification.md)

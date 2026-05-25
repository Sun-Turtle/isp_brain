---
status: active
priority: high
tags:
  - decisions
  - banking
  - financial
  - operations
created: 2026-05-24
---

# Bank Account: Tide

## Context

Sun Turtle needed a business bank account. Separate from personal finances from day one — required for customer payments, wholesale invoices, Ofcom/ICO registration, and wholesale partner credibility.

CLGs face known friction with high-street banks (they don't understand the structure). The core admin stack originally suggested Starling, Monzo Business, or Tide as fintech alternatives.

## Decision

Open a business account with **[Tide](https://www.tide.co/)**.

## Rationale

- **CLG-compatible**: Starling and Monzo Business both rejected Sun Turtle's Company Limited by Guarantee structure. Neither explicitly supports CLGs in their onboarding flows. Tide is more flexible — multiple CLGs have confirmed successful account opening on Reddit and community forums.
- **Fintech speed**: Online application, no branch visits, fast approval. Incorporation certificate and director ID are the only documents needed.
- **Free tier**: Tide has a free account tier suitable for early-stage businesses with low transaction volumes.
- **UK-focused**: FSCS-protected (via ClearBank), UK Open Banking feeds, integrates with QuickFile for automated reconciliation.
- **No bank lock-in**: Not tied to any particular bookkeeping software (unlike FreeAgent + Mettle/NatWest).

## Alternatives

- **Starling Business**: Rejected — does not support CLG structures. The onboarding flow requires share capital fields that can't be left blank.
- **Monzo Business**: Rejected — same issue. Their business account model expects a standard Ltd share structure.
- **High-street banks (Barclays, NatWest, HSBC)**: Accept CLGs on paper but require in-person branch visits, physical paperwork, and weeks of processing. Contradicts the lean ops philosophy.
- **Mettle (NatWest)**: Free with FreeAgent integration, but also share-structure-dependent and uncertain about CLG support.

## Impact

- Company has a real bank account — prerequisite for Ofcom CP registration, wholesale supplier onboarding, and ICO fee payment
- Director's loan can be deposited and tracked formally
- QuickFile integration via Open Banking feeds enables automated bookkeeping from day one
- Confirms the known CLG banking friction reported in the admin stack — validated the fintech-first approach, just narrowed to Tide specifically

## See also

- [Core Admin Stack](../knowledge/company-core-admin-stack.md)
- [QuickFile Bookkeeping](company-bookkeeping.md)
- [Tide (Knowledge)](../knowledge/company-tide.md)
- [CLG Structure Decision](company-structure-clg.md)

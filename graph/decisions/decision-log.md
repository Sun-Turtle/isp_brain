---
status: active
priority: medium
tags:
- decisions
- log
created: 2026-05-07
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

## 2026-05-06: Company structure — CLG

**Context**: Sun Turtle Internet needed a legal structure. Three models evaluated: standard Ltd, CIC, and CLG. **Decision**: Company Limited by Guarantee — no shares, no shareholders, profits reinvested. **Rationale**: Matches the ethos structurally (not just marketed). Green ISP validates the model — running profitably as a CLG since 2003 on Openreach. **Alternatives**: Ltd (legal duty to maximise shareholder value contradicts mission), CIC (adds CIC Regulator overhead a 5-person team doesn't need). **Details**: See [Company Structure: CLG](company-structure-clg.md).

## 2026-05-05: Flat file naming convention

**Context**: Deep nesting caused git diff noise and placement deliberation. **Decision**: Adopt flat structure — one level of domain dirs, files named `topic-subtopic-descriptor.md`. **Rationale**: Cleaner diffs, no subdirectory decisions, `iwe tree` handles discovery. **Details**: See [File Naming Convention: Flat Structure](flat-file-convention.md).

## 2026-05-04: Collapsed 7 domains to 5

**Context**: Original 7 domains (direction, health, identity, knowledge, operations, relationships, resources) had fuzzy boundaries — many topics fit 2–3 domains. **Decision**: Collapse to identity, knowledge, decisions, tasks, resources. **Rationale**: Mutually exclusive boundaries, less deliberation when placing files. **Details**: See [Domain Structure: 5 Domains](domain-structure.md).

## 2026-05-24: Domain — FreeThought and `suninternet.co.uk`

**Context**: The company needed a domain for email, website, and supplier credibility. Aligning the registrar choice with the CLG's ethical positioning mattered. **Decision**: Register `suninternet.co.uk` at FreeThought, a UK-based ethical registrar. **Rationale**: Ethical alignment with CLG values, UK-based, no upselling/dark patterns, `suninternet` is shorter and more brandable than `sunturtleinternet`. **Alternatives**: GoDaddy/123-Reg (misaligned values), Gandi (no UK advantage), `.uk` TLD (less recognisable than `.co.uk`). **Details**: See [Domain: FreeThought & suninternet.co.uk](company-domain.md).

## 2026-05-24: Bookkeeping — QuickFile

**Context**: Bookkeeping software needed from day one to track director's loan, incorporation costs, and future revenue. **Decision**: Use QuickFile (quickfile.co.uk), a UK-focused free-tier platform. **Rationale**: Free for early-stage, UK MTD/VAT compliant, no bank lock-in (unlike FreeAgent + Mettle), lighter than Xero for a pre-revenue CLG. **Alternatives**: FreeAgent (bank-locked), Xero (££ from day one), Akaunting (self-host overhead), spreadsheet (error-prone). **Details**: See [Bookkeeping: QuickFile](company-bookkeeping.md).

## 2026-05-24: Website — plain HTML/CSS, no framework

**Context**: The company website needs public pages — homepage, financial transparency, complaints procedure. The tech choice reflects the company philosophy of simplicity and transparency. **Decision**: Plain HTML + CSS, no JavaScript framework, no build step, no CMS. **Rationale**: Zero dependencies, instant load, maintainable by one person, git-native editing matches the "everything in public" posture. No cookies = no consent banners. **Alternatives**: Static site generators (Hugo/Jekyll — build step for 3 pages), React/Next.js (JS runtime for text pages), WordPress (database and maintenance for 3 pages), Wix/Squarespace (vendor-locked, closed-source). **Details**: See [Website: Plain HTML/CSS, No Framework](website-stack.md).

## 2026-05-24: T&Cs — no mid-contract price rises, router on loan

**Context**: Terms and conditions needed a pricing model, equipment policy, and liability cap. Studied Green ISP, Andrews & Arnold, and TalkTalk as real-world precedents. **Decision**: Fixed pricing for minimum term (no CPI+ rises), router supplied on loan (not sold), liability capped at 12 months of fees paid rather than a flat £250. **Rationale**: Mid-contract rises are industry standard but consumer-hostile — fixed pricing is a trust differentiator for a new ISP. Router-on-loan keeps upfront customer cost near zero and standardises support. Fee-scaled liability is more defensible under the Consumer Rights Act than a flat cap. **Alternatives**: CPI+ rises (revenue protection but undermines trust positioning), router sold at cost (higher upfront, more support variables), flat £250 liability cap (Green ISP/A&A model but potentially unenforceable at higher-value contracts). **Details**: See [T&Cs: No Mid-Contract Price Rises, Router on Loan](ts-and-cs-structure.md).

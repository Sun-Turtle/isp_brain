---
status: active
priority: medium
tags:
  - resources
  - research
  - regulatory
  - guide
  - isp
created: 2026-05-07
---

# Making a Reseller ISP — Legal & Regulatory Guide

**Source**: `making_a_reseller_isp.pdf`

Comprehensive implementation guide for establishing an ISP in the UK: legal, incorporation, licensing, and regulatory aspects.

**Key points:**
- Incorporating an ISP in the UK requires selecting an appropriate business structure, registering with Companies House, and complying with the Communications Act 2003 and Ofcom's General Conditions of Entitlement.
- No specific ISP license is required under UK law, but registration with Ofcom as a Communications Provider is beneficial for wholesale operations and regulatory compliance.
- Key regulatory frameworks include the Communications Act 2003, Network and Information Systems (NIS) Regulations 2018, Telecommunications Security Act 2021, and Product Security and Telecommunications Infrastructure Act 2022.
- Compliance with consumer protection laws, data protection regulations (UK GDPR and PECR), and telecoms security requirements is mandatory.
- The process involves consultations with legal advisors, engagement with local authorities, meetings with wholesale providers, and adherence to industry best practices outlined by ISPA and Ofcom.

## Introduction

This guide provides a detailed, step-by-step roadmap for implementing the legal, incorporation, licensing, and regulatory requirements to establish an Internet Service Provider (ISP) in the UK, focusing on a reseller-only business model. It covers the full lifecycle from initial business structure selection and incorporation through to regulatory compliance and securing the first client. The guide integrates official government sources, regulatory body guidelines, and industry best practices to ensure a legally sound and operationally compliant market entry.

## Phase 1: Business Structure Selection and Incorporation

### Step 1: Choose the Appropriate Business Structure

Select a business structure that aligns with your operational goals, liability preferences, and tax considerations. Common options include:

- **Private Limited Company (Ltd)**: Offers limited liability, enhanced credibility, and facilitates investment. Recommended for ISPs due to liability protection and corporate governance flexibility.
- **Sole Trader or Partnership**: Simpler but with unlimited liability, generally less suitable for ISPs due to regulatory and financial risks.
- **Company Limited by Guarantee or Community Interest Company**: Suitable for non-profit or community-focused ISPs.

Considerations:
- Liability protection
- Tax implications
- Ability to raise capital
- Governance and reporting requirements

### Step 2: Register the Company with Companies House

Prepare and submit the following documents to Companies House:

- **Memorandum of Association**: Legal statement signed by initial shareholders agreeing to form the company.
- **Articles of Association**: Rules governing the company's operations and management.
- **Incorporation Form (IN01)**: Contains company name, registered office address, director and shareholder details.

Process:
- Choose a unique company name not already registered.
- Provide details of the company's business activities using Standard Industrial Classification (SIC) codes.
- Pay the registration fee (typically £12 for online incorporation).

Outcome: Certificate of Incorporation issued by Companies House, confirming legal existence.

### Step 3: Post-Incorporation Legal and Financial Setup

- Open a company bank account.
- Register for Corporation Tax and PAYE with HMRC within three months of starting business.
- Consider VAT registration if turnover exceeds £90,000 or if beneficial for business.
- Ensure compliance with ongoing legal responsibilities such as annual reports and tax returns.

## Phase 2: Regulatory Compliance and Licensing

### Step 4: Understand and Comply with the Communications Act 2003 and Ofcom's General Conditions

- Familiarize yourself with the Communications Act 2003, the primary legislation governing UK telecommunications.
- Review Ofcom's General Conditions of Entitlement (GCs), which outline the regulatory framework for communications providers.
- Ensure compliance with the GCs, which cover consumer protection, network security, and service provisioning.
- Detailed breakdown: [Ofcom General Conditions](../knowledge/regulatory-ofcom-general-conditions.md)

### Step 5: Set Up Core Admin Stack (NEW — pre-regulatory requirement)

Before approaching regulators or wholesalers, establish the minimum operational infrastructure:

- **Business bank account** — separate from personal finances; some fintechs (Tide, Starling, Monzo) are faster for CLGs than high-street banks
- **Domain and professional email** — company-domain email (not Gmail/Hotmail) signals operational readiness to suppliers
- **Bookkeeping system** — FreeAgent (free with some accounts), Xero, or accountant-managed; track the director's loan from day one
- **Privacy policy** — published on website before collecting any data; covers what you collect, why, retention, sharing
- **Terms and conditions** — consumer contract compliant with Consumer Rights Act 2015, Ofcom GCs, and distance selling regulations
- **Complaints procedure** — published, with channels, timeframes, escalation path, and ADR signposting

Wholesalers evaluate operational readiness through this stack. Having all six complete signals you're a real business. Full breakdown: [Core Admin Stack](../knowledge/company-core-admin-stack.md)

### Step 6: Register with ICO (Data Protection Fee)

Register with the Information Commissioner's Office before processing any personal data:

- Complete the [ICO self-assessment](https://ico.org.uk/for-organisations/data-protection-fee/self-assessment/)
- Tier 1 (micro-organisations): £40/year for small ISPs
- Registration is mandatory for ISPs — no exemption applies
- Receive ICO registration number and add to privacy policy
- Must also comply with UK GDPR (lawful basis for processing, breach reporting, subject access requests)

Full detail: [ICO Registration](../knowledge/company-ico-registration.md)

### Step 7: Notify Ofcom (General Authorisation — NOT a licence application)

Under the general authorisation regime, you notify Ofcom — you don't apply for a licence:

- Complete the Ofcom notification form via their portal
- Provide company details, service categories (fixed internet access, electronic communications service)
- Receive a Communications Provider ID (CP ID) — some wholesalers require this
- No fee, no approval process, 2-4 weeks to process
- Service categories: select only what you provide (fixed broadband, VoIP if offering voice)
- Do NOT over-declare — each category triggers specific obligations

Key distinction: UK uses general authorisation, not individual licensing. This lowers barriers to entry significantly. Full detail: [Ofcom Notification](../knowledge/company-ofcom-notification.md)

### Step 8: Join ADR Scheme (Mandatory for Consumer-Facing ISPs)

General Condition C4 requires membership in an Ofcom-approved Alternative Dispute Resolution scheme:

- **CISAS** (run by CEDR): Annual fee (~£300-600 for micro ISPs) plus ~£100-300 per adjudicated case
- **Communications Ombudsman**: Free with ISPA membership (membership £550-950/year for small ISPs)
- Recommended path: join ISPA → free Comm Ombudsman membership → ADR compliance + industry credibility in one
- Add ADR details to website, complaints procedure, customer contracts, and deadlock letters
- Green ISP uses CISAS

Full detail: [ADR Scheme](../knowledge/company-adr-scheme.md)

### Step 9: Comply with Network and Information Security Regulations

- Implement security measures as mandated by the Network and Information Systems (NIS) Regulations 2018.
- Adopt the Telecommunications Security Act 2021 (TSA) requirements, including internal safeguards and supply chain security reviews.
- Ensure workforce training on cybersecurity risks and compliance.

### Step 10: Adhere to Consumer Protection and Data Privacy Laws

- Comply with the Consumer Rights Act 2015, ensuring fair trading practices and consumer redress mechanisms.
- Follow the Privacy and Electronic Communications Regulations (PECR) for electronic marketing and data protection.
- Implement UK GDPR and Data Protection Act 2018 requirements for personal data processing, including security policies and breach reporting.

## Phase 3: Industry Best Practices and Operational Setup

### Step 11: Engage with Local Authorities and Infrastructure Providers

- Consult local authorities to understand service availability and infrastructure status in your target area.
- Identify existing broadband infrastructure and potential gaps.
- Engage with fibre providers and negotiate leases or agreements for equipment installation.

### Step 12: Join Industry Trade Bodies and Adopt Codes of Practice

- Consider joining the Internet Services Providers' Association (ISPA) to benefit from their Code of Practice and industry representation.
- Familiarize yourself with ISPA's mandatory and voluntary regulatory requirements, including customer service, contracts, complaints handling, and online safety.

### Step 13: Implement Health and Safety Compliance (If Applicable)

- If your ISP involves physical infrastructure deployment, comply with Safety Schemes in Procurement (SSIP) requirements.
- Obtain SSIP certification through an accredited member scheme to demonstrate health and safety compliance.

### Step 14: Establish an Information Security Management System (ISMS) and Obtain ISO 27001 Certification

- Develop and implement an ISMS to manage cybersecurity risks.
- Pursue ISO 27001 certification to demonstrate compliance with international security standards.
- Conduct regular system reviews and audits.

## Phase 4: Client Onboarding and Market Entry

### Step 15: Develop Customer Contracts and Terms of Service

- Draft customer contracts and terms of service that comply with UK consumer protection laws and Ofcom regulations.
- Ensure transparency in pricing, service levels, and complaint handling procedures.

### Step 16: Secure Your First Client

- Leverage your registration with Ofcom and membership in trade bodies like ISPA to build credibility.
- Market your services in compliance with PECR and consumer protection laws.
- Engage with wholesale providers and leverage their infrastructure to offer competitive services.

## Summary Table of Key Milestones

| Phase/Step | Description | Responsible Party | Estimated Timeline | Key Documentation |
|---|---|---|---|---|---|
| 1. Business Structure Selection | Choose legal structure (e.g., Ltd, CLG) | Founders/legal advisor | 1–2 weeks | Business structure decision |
| 2. Incorporation with Companies House | File Memorandum, Articles, IN01 form | Founders/legal advisor | 2–4 weeks | Memorandum of Association, Articles of Association, IN01 form, registration fee |
| 3. Post-Incorporation Setup | Bank account, tax registration, VAT if applicable | Founders/accountant | 1 month | Corporation Tax registration, PAYE registration, VAT registration (if applicable) |
| 4. Regulatory Framework Study | Study Communications Act 2003, Ofcom GCs, TSA, NIS | Legal/compliance team | Ongoing | Compliance documentation, security policies |
| 5. Core Admin Stack | Bank account, domain/email, bookkeeping, privacy policy, T&Cs, complaints procedure | Founders | 2-4 weeks | Privacy policy, T&Cs, complaints procedure |
| 6. ICO Registration | Register for data protection fee (£40/year Tier 1) | Founders | 1 day | ICO registration certificate |
| 7. Ofcom Notification | Notify as communications provider, get CP ID | Compliance officer | 2–4 weeks | Ofcom notification confirmation, CP ID |
| 8. ADR Scheme Membership | Join CISAS or Comm Ombudsman (via ISPA) | Compliance officer | 1–2 weeks | ADR membership confirmation |
| 9. Network Security Compliance | NIS Regulations, TSA requirements | Technical/compliance | Ongoing | Security policies, supply chain reviews |
| 10. Consumer & Data Protection | Consumer Rights Act 2015, PECR, UK GDPR | Compliance officer | Ongoing | GDPR compliance documentation |
| 11. Local Engagement and Infrastructure | Consult local authorities, negotiate with fibre providers | Operations/legal team | 2–3 months | Lease agreements, local authority consultations |
| 12. Industry Best Practices | Join ISPA, adopt Code of Practice, implement ISMS | Compliance/operations team | 1–2 months | ISPA membership application, ISMS documentation |
| 13. Health and Safety Compliance | Obtain SSIP certification if applicable | Safety officer | 1–2 months | SSIP certification documents |
| 14. ISO 27001 Certification | Implement ISMS, obtain certification | IT/security team | 3–6 months | ISMS documentation, ISO 27001 audit reports |
| 15. Customer Contracts and Terms | Draft compliant customer agreements | Legal team | 1 month | Customer contracts, terms of service |
| 16. Secure First Client | Market services, engage wholesale providers | Sales/marketing team | Ongoing | Marketing materials, customer agreements |

## Conclusion

Establishing an ISP in the UK as a reseller-only business requires meticulous attention to legal, regulatory, and operational details. The process begins with selecting an appropriate business structure and incorporating with Companies House, followed by comprehensive compliance with the Communications Act 2003, Ofcom's General Conditions, and various security and consumer protection regulations. Engaging with local authorities, industry trade bodies like ISPA, and implementing robust security and compliance programs are essential steps. The timeline from incorporation to securing the first client can range from 3 to 12 months, depending on the complexity of regulatory compliance and operational setup.

### References (from source PDF)

1. Company Incorporation in the UK: 2026 Guide
2. How To Incorporate A Company In The UK: A Legal Guide For New Businesses | Sprintlaw UK
3. Incorporation and names - GOV.UK
4. Incorporating a Business in the UK: Your Complete Guide
5. What's the Fastest Way to Incorporate a Business in the UK? A Step-by-Step Guide
6. Incorporate in UK: A Step-by-Step Guide to Business Setup
7. Company Incorporation Step by Step: United Kingdom | Zegal
8. Key telecommunications laws, regulations and policies in United Kingdom - DLA Piper Telecommunications Laws of the World
9. TELECOMMUNICATIONS: An Introduction to UK Law | Chambers and Partners
10. Becoming a Broadband Reseller: 2025 UK Market Guide - Netify
11. How to become an internet service provider (ISP) | Guide by Startups.co.uk
12. Telecommunications Law For Resellers | Trenches Law
13. A guide to cybersecurity laws and regulations in the UK | Vanta
14. Data Protection Laws and Regulations Report 2025-2026 United Kingdom
15. United Kingdom: Data Protection & Cybersecurity – Country Comparative Guides
16. Security of services | ICO
17. What are PECR? | ICO
18. Data protection and cybersecurity laws in the UK | CMS Expert Guide
19. Understanding the UK GDPR and How to Achieve Compliance
20. The Privacy and Electronic Communications (EC Directive) Regulations 2003
21. Data Protection Laws and Regulations Report 2024-2025 United Kingdom
22. How to Become Your Own ISP in the UK
23. Code of Practice | The Internet Service Providers Association
24. Internet Service Providers Association (United Kingdom) - Wikipedia
25. How to pass an SSIP in 2026 | Croner
26. Expert UK Cyber Security & Compliance Services
27. Internet service provider (ISP) contracts and compliance toolkit | Practical Law

## See also

- [Sun Turtle Playbook — Ultra-Lean UK ISP](research-company-sun-turtle-playbook.md)
- [Ofcom General Conditions](../knowledge/regulatory-ofcom-general-conditions.md)
- [Core Admin Stack](../knowledge/company-core-admin-stack.md)
- [ICO Registration](../knowledge/company-ico-registration.md)
- [Ofcom Notification](../knowledge/company-ofcom-notification.md)
- [ADR Scheme](../knowledge/company-adr-scheme.md)

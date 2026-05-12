---
name: sec-scope
description: Defines the project security scope. Identifies asset inventory, data flows, and trust boundaries. First mandatory step in the pipeline.
---

# /sec-scope — Scope Definition

## Purpose

Establish the security assessment boundary for the project. In this step:

- Understand the project context and environment
- Build the asset inventory (applications, data stores, integrations, infrastructure)
- Document data flows and encryption status
- Identify trust boundaries and externally exposed surfaces

## Language Rule

Use the same language the user is writing in for all output.

## Execution Instructions

### Step 1 — 9-Question Intake

Ask all 9 questions below in a single message. Do not begin the analysis until the answers arrive.
If any answer is ambiguous, ask only the specific clarifying question needed — do not restart the intake.

```
To assess the project, please answer the following 9 questions:

1. Is this a new application or an assessment of an existing system?
   (new development / integration with existing system / third-party product)

2. Is the infrastructure being built from scratch or using existing/shared infrastructure?
   (new infrastructure / existing or shared infrastructure / unclear)

3. Who will use the system?
   (internal users / enterprise customers / individual/consumer customers / API consumers / mixed)

4. Will the system be internet-facing?
   (yes — directly / yes — behind CDN/WAF / no — internal network only / unclear)

5. Does the service use any public cloud?
   (yes — AWS / Azure / GCP / other / no — on-premise / hybrid / unclear)

6. Is user authentication required?
   (yes — SSO / OAuth / LDAP / custom / no / unclear)

7. Who is building the system?
   (in-house team / external/outsourced developer / SaaS/off-the-shelf product / mixed)

8. Are there any third-party integrations?
   (yes — payment gateway / identity provider / SMS/email service / external API / other)
   (no)

9. Will the system process confidential or sensitive data?
   (yes — national ID / financial records / health data / credentials / other personal data)
   (no — no personal data will be processed)
```

### Step 2 — Write Scope Analysis

Once all answers are received, write the analysis to the conversation using the structure below:

---

## /sec-scope Analysis

### Project Overview
[2 sentences: what it does, who uses it, what environment]

### Asset Inventory

**Applications & Services**
| Name | Type | Technology | Externally Accessible |
|---|---|---|---|
| [name] | [backend/frontend/api/worker] | [stack] | yes/no |

**Data Stores**
| Name | Type | Contains Personal Data | Encrypted at Rest |
|---|---|---|---|

**External Integrations**
| Name | Direction | Data Shared | Auth Method |
|---|---|---|---|

**Sensitive Data Categories**
- [category]: [description]
- NONE (if applicable)

### Data Flow Summary
[Narrative: what enters the system, what leaves, how it moves, where it is stored]

### Trust Boundaries
| Boundary | From | To | Auth Method | Logged |
|---|---|---|---|---|

### Assumptions & Gaps
- [ASSUMPTION-001]: [description]
- [GAP-001]: [description] — WARNING

---

Analysis complete. Next step: /sec-threat-model

## Hard Rules

- Do not produce scope analysis until all 9 questions have clear answers.
- Do not read or write any files.
- Mark unknown fields as [ASSUMPTION], do not invent them.

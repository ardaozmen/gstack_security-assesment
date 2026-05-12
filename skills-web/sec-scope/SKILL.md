---
name: sec-scope
description: Defines the project security scope. Reads the project description, infers as many intake answers as possible, and asks only the unclear ones with lettered options. First mandatory step in the pipeline.
---

# /sec-scope — Scope Definition

## Purpose

Establish the security assessment boundary for the project.

## Language Rule

Use the same language the user is writing in for all output.

## Pipeline Mode

When called by `/security-assessment`: do NOT write the scope analysis to the conversation.
Hold all results in context for subsequent steps.
The orchestrator prints the status line — this skill prints nothing except clarifying questions if needed.

## The 9 Intake Questions

These must all be answered before analysis begins — either inferred from the description or explicitly asked.

| # | Question | Options |
|---|---|---|
| 1 | New application or existing system? | new development / existing system integration / third-party product |
| 2 | Infrastructure new or existing/shared? | new / existing or shared / unclear |
| 3 | Who will use the system? | internal users / enterprise customers / individual customers / API consumers / mixed |
| 4 | Internet-facing? | yes — directly / yes — behind CDN/WAF / no — internal only / unclear |
| 5 | Public cloud? | AWS / Azure / GCP / other / no — on-premise / hybrid / unclear |
| 6 | User authentication required? | yes — SSO/OAuth / yes — LDAP / yes — custom / no / unclear |
| 7 | Who is developing it? | in-house / outsourced / SaaS/off-the-shelf / mixed |
| 8 | Third-party integrations? | payment gateway / identity provider / SMS/email / external API / other / none |
| 9 | Sensitive or confidential data? | national ID / financial records / health data / credentials / other personal data / no |

## Execution Instructions

### Step 1 — Read and Infer

Read the project description carefully.
For each of the 9 questions, decide:
- **CLEAR**: the answer is explicitly stated or strongly implied by the description → infer it, do not ask
- **UNCLEAR**: the answer is ambiguous, missing, or contradictory → must ask

### Step 2 — Ask Only Unclear Questions

If all 9 are clear → skip to Step 3 immediately.

If any are unclear → ask only those in a single message, with lettered options:

```
Based on your description, a few things need clarification:

**[Question text]**
  a) [option]
  b) [option]
  c) [option]

**[Question text]**
  a) [option]
  b) [option]

Reply with the letters (e.g. "1b, 2a")
```

Wait for the user's reply. Then proceed.

### Step 3 — Build Scope Analysis

With all 9 questions answered (inferred + asked), build the full scope analysis internally:

- Project overview (2 sentences)
- Asset inventory: applications, data stores, external integrations
- Sensitive data categories
- Data flow summary
- Trust boundaries
- Assumptions & gaps

Hold this analysis in context. Do not write it to the conversation.

## Hard Rules

- Do not ask questions that can be clearly inferred from the description.
- Ask all unclear questions in a single message — never piecemeal.
- Do not proceed to analysis until all 9 questions are covered.
- Do not write the scope analysis to the conversation when running in pipeline mode.
- Do not read or write any files.

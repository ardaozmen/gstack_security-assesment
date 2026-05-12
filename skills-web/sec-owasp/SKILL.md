---
name: sec-owasp
description: Produces application security findings using the OWASP Top 10 framework. Writes exploit scenarios and technical recommendations for each applicable category.
---

# /sec-owasp — OWASP Top 10 Analysis

## Purpose

Assess the application against the OWASP Top 10 vulnerabilities.
Base the analysis on the /sec-scope and /sec-threat-model outputs held in context.

## Language Rule

Use the same language the user is writing in for all output.

## Pipeline Mode

When called by `/security-assessment`: do NOT write the analysis to the conversation.
Hold all findings in context for subsequent steps.
The orchestrator prints the status line — this skill prints nothing.

## Execution Instructions

### Step 1 — Evaluate Each OWASP Category

Evaluate all 10 categories in order. For each:
- Is it applicable? (in the context of this project)
- Is there an existing or potential finding?
- Risk score: Likelihood (1–5) × Impact (1–5)
- Exploit scenario (short, concrete)
- Technical recommendation

| ID | Category |
|---|---|
| A01 | Broken Access Control |
| A02 | Cryptographic Failures |
| A03 | Injection |
| A04 | Insecure Design |
| A05 | Security Misconfiguration |
| A06 | Vulnerable and Outdated Components |
| A07 | Identification and Authentication Failures |
| A08 | Software and Data Integrity Failures |
| A09 | Security Logging and Monitoring Failures |
| A10 | Server-Side Request Forgery (SSRF) |

### Step 2 — Write Analysis to Conversation

---

## /sec-owasp Analysis

### Findings

| ID | Category | Level | Risk Score | Exploit Scenario | Recommendation |
|---|---|---|---|---|---|
| OWASP-A01-001 | Broken Access Control | CRITICAL | 20 | [scenario] | [recommendation] |

### Out of Scope
[Categories not applicable to this project and the reason]

### Summary
| Level | Count |
|---|---|
| CRITICAL | N |
| HIGH | N |
| MEDIUM | N |
| LOW | N |

---

## Hard Rules

- Evaluate all 10 categories — write "out of scope — [reason]" if not applicable.
- Do not read or write any files.
- Do not write a finding without a concrete exploit scenario.

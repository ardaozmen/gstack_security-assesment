---
name: sec-threat-model
description: Builds a STRIDE-based threat model. Produces a component-threat matrix, trust boundary violation scenarios, and attack trees. Generates the threat-modeling.html artifact at the end.
---

# /sec-threat-model — Threat Modeling

## Purpose

Systematically identify threats against every system component using STRIDE.
Base the analysis on the /sec-scope output held in context — no file reading.

## Language Rule

Use the same language the user is writing in for all output.

## Pipeline Mode

When called by `/security-assessment`: do NOT write the analysis to the conversation.
Hold all findings in context for subsequent steps.
The orchestrator prints the status line — this skill prints nothing.

## Execution Instructions

### Step 1 — Component-Threat Matrix

Apply STRIDE to each asset from the /sec-scope analysis above:

| Asset Type | S | T | R | I | D | E |
|---|---|---|---|---|---|---|
| External Entity | ✓ | | ✓ | | | |
| Service / Process | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Data Store | | ✓ | ✓ | ✓ | ✓ | |
| Data Flow | | ✓ | | ✓ | ✓ | |
| Auth Component | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

For each applicable cell:
- **Spoofing**: Can identity be forged?
- **Tampering**: Is input validated? Are write operations protected?
- **Repudiation**: Are critical actions logged with a tamper-proof audit trail?
- **Info Disclosure**: Do error messages leak internals? Is encryption complete?
- **Denial of Service**: Is rate limiting present? Can resource exhaustion be triggered?
- **Elevation of Privilege**: Is authorization enforced at every layer?

### Step 2 — Data Flow Threat Analysis

For each data flow in the /sec-scope analysis:
1. Is transport encrypted (TLS 1.2+)?
2. Is a MITM attack possible?
3. Can a request be replayed?
4. At which layer is data validated?
5. What is the blast radius if this flow is compromised?

### Step 3 — Trust Boundary Analysis

For each trust boundary crossing:
1. Who or what is allowed to cross it?
2. What is the authentication mechanism?
3. Where is the authorization decision made?
4. Is every crossing logged?
5. What happens if the boundary is bypassed?

### Step 4 — Risk Scoring

For every threat: **Risk = Likelihood (1–5) × Impact (1–5)**

| Score | Level |
|---|---|
| 20–25 | CRITICAL |
| 12–19 | HIGH |
| 6–11 | MEDIUM |
| 1–5 | LOW |

### Step 5 — Attack Trees

Build an attack tree for every threat with risk score ≥ 12.

```
Goal: [unauthorized access to X]
├── Path A: [authentication bypass]
│   ├── A1: [SQL injection] — difficulty: medium
│   └── A2: [brute force]   — difficulty: low
└── Path B: [abuse of legitimate functionality]
    └── B1: [IDOR]          — difficulty: low
```

### Step 6 — Write Analysis to Conversation

---

## /sec-threat-model Analysis

### Component Threat Matrix
| Asset | Spoofing | Tampering | Repudiation | Info Disclosure | DoS | EoP |
|---|---|---|---|---|---|---|
| [asset] | [finding or N/A] | ... | | | | |

### Data Flow Threats
| Flow | Threat | Category | Level | Description |
|---|---|---|---|---|

### Trust Boundary Violations
**[Boundary Name]**
- Scenario: [description]
- Level: CRITICAL / HIGH / MEDIUM / LOW
- Attack path: [brief]

### Attack Trees
[Each tree]

### Threat Summary
| Level | Count |
|---|---|
| CRITICAL | N |
| HIGH | N |
| MEDIUM | N |
| LOW | N |
| **Total** | **N** |

---

### Step 7 — Generate threat-modeling.html Artifact

After the analysis is written, create an HTML artifact named `threat-modeling.html`.

Use the `## threat-modeling.html` template and shared CSS from `word-output-standard`.
Replace all placeholders with actual content from the analysis.
Apply row classes (`critical`, `high`, `medium`, `low`) based on actual threat levels.
Remove all template comments.
Artifact type: `text/html`

## Hard Rules

- Do not read or write any files — all input comes from the conversation.
- Do not skip any STRIDE category — write "N/A — [reason]" if truly not applicable.
- Do not finish without at least one attack tree.
- Every CRITICAL threat requires an attack tree.

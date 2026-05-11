---
name: sec-project-requirements
description: Consolidate all security assessment findings into a single prioritized requirements document. Translates threats, OWASP findings, regulatory gaps, and iGRC controls into actionable security requirements with risk context. Single source of truth before sign-off.
allowed-tools: Read, Write, Glob, Grep
---

# /sec-project-requirements — Security Requirements Document

## Purpose

Transform all upstream assessment findings into a unified, decision-ready requirements document. This skill:

- Consolidates STRIDE threats, OWASP findings, regulatory gaps, and iGRC control gaps
- Frames each finding as an implementable security requirement
- Assigns priority (P0 BLOCKER / P1 HIGH / P2 MEDIUM) and risk score
- Produces a single `PROJECT_REQUIREMENTS.md` that feeds both development teams and `/sec-signoff`

## Usage

```
/sec-project-requirements [--include-financial-impact] [--format full|requirements-only|executive]
```

**Arguments**:
- `--include-financial-impact`: Add rough financial exposure estimates per requirement
- `--format requirements-only`: Skip executive summary, output requirements only
- `--format executive`: Executive summary + posture only

**Triggers**: "güvenlik gereksinimlerini oluştur", "konsolide rapor", "proje gereksinimleri", "tüm bulguları birleştir", "/sec-project-requirements"

## Prerequisites

Minimum: `SCOPE.md` (Gate-SCOPE PASS).
Full coverage requires (load all that exist):
- `THREAT_MODEL.md`
- `OWASP_FINDINGS.md`
- `REGULATORY_FINDINGS.md`
- `IGRC_FINDINGS.md`, `RACI_MATRIX.md`

For each missing file, record: `[COVERAGE-GAP-xxx]: <skill> output not available — coverage reduced.`

## Execution Phases

### Phase 1 — Load and Inventory All Findings

Read each available upstream file. Build a unified finding list:

| ID | Title | Source | Severity | Type |
|---|---|---|---|---|
| THREAT-001 | MITM on payment flow | sec-threat-model | HIGH | Threat |
| OWASP-A01-001 | IDOR via /api/accounts | sec-owasp | CRITICAL | Vulnerability |
| REG-BDDK-001 | No pen test planned | sec-regulatory | HIGH | Compliance Gap |
| IGRC-003 | No CAB process | sec-igrc | MEDIUM | Control Gap |

De-duplicate: if two findings point to the same root cause, merge them, citing both source IDs.

### Phase 2 — Risk Scoring

Score every finding:

```
Risk Score = Likelihood (1–5) × Impact (1–5)
```

| Score | Level |
|---|---|
| 20–25 | CRITICAL |
| 12–19 | HIGH |
| 6–11 | MEDIUM |
| 1–5 | LOW |

**Likelihood (1–5)**:

| Score | Meaning |
|---|---|
| 5 | Trivially exploitable; tools readily available |
| 4 | Common attack pattern; moderate skill needed |
| 3 | Achievable with effort and research |
| 2 | Requires significant skill or access |
| 1 | Requires nation-state resources |

**Impact (1–5)**:

| Score | Meaning |
|---|---|
| 5 | Full system compromise or existential regulatory sanction |
| 4 | Large data breach or major business disruption |
| 3 | Significant data exposure or customer-facing outage |
| 2 | Limited exposure; recoverable |
| 1 | Minor inconvenience; no data loss |

### Phase 3 — Translate Findings to Requirements

For every finding, write a corresponding security requirement:

```yaml
- id: SEC-REQ-001
  title: "Object-level authorization on all API endpoints"
  source_findings: ["OWASP-A01-001", "THREAT-003"]
  requirement: |
    Every API endpoint that returns or modifies user-owned resources MUST verify
    that the authenticated user owns the requested resource before processing.
    Unauthorized attempts MUST be logged with user ID, resource ID, and timestamp.
  acceptance_criteria:
    - Each endpoint has an authorization check before data retrieval
    - Access denied events appear in the security log within 1 second
    - Automated test suite covers at least the top 5 IDOR-prone endpoints
  risk_score: 20
  risk_level: CRITICAL
  priority: P0_BLOCKER
  owner: "[team]"
  target_date: "[before go-live]"
  regulatory_penalty: YES | NO | UNCLEAR
```

**Priority mapping:**

| Priority | Condition | Timeline |
|---|---|---|
| P0 BLOCKER | risk_score ≥ 20, OR any NON_COMPLIANT regulatory finding with legal risk, OR critical control gap without owner | Must resolve before go-live |
| P1 HIGH | risk_score 12–19, OR PARTIAL compliance with defined remediation | 30 days post go-live |
| P2 MEDIUM | risk_score 6–11, or missing review cadences | 90 days post go-live |

### Phase 4 — Security Posture Assessment

Overall posture: **🔴 RED / 🟡 AMBER / 🟢 GREEN**

| Posture | Condition |
|---|---|
| 🔴 RED | Any P0 BLOCKER unresolved, or CRITICAL regulatory NON_COMPLIANT |
| 🟡 AMBER | P1 findings present with defined owners; no unresolved blockers |
| 🟢 GREEN | No CRITICAL or HIGH unresolved findings |

Write 2–3 sentence rationale.

### Phase 5 — Executive Summary

Written for a non-technical reader (CISO, CTO, board member):

1. What the project does (2 sentences)
2. Which assessments ran and their scope
3. 3 most important security requirements (plain language)
4. Go-live readiness: what MUST be done vs. what can wait
5. Overall security posture + rationale

### Phase 6 — Coverage Gaps

For each assessment that did not run (missing input files), state:
- What risks were NOT assessed
- What additional findings might exist
- Recommendation: run missing skills before go-live if posture is RED

## Quality Gate — Gate-REQ

| Check | Required |
|---|---|
| At least 1 requirement per source skill that ran | PASS |
| Every requirement has: title, risk_score, priority, owner, target_date | PASS |
| P0 BLOCKER list present (or "no blockers" explicitly stated) | PASS |
| Security posture (RED/AMBER/GREEN) + rationale present | PASS |
| Executive summary readable by non-technical audience | PASS |
| Coverage gaps documented for missing inputs | PASS |
| If P0 list is empty: taste decision — confirm no blockers | TASTE DECISION |
| If `--include-financial-impact`: taste decision — include estimates? | TASTE DECISION |

## Output File — `PROJECT_REQUIREMENTS.md`

```markdown
# Security Requirements Document

**Project**: [name]
**Date**: [ISO date]
**Analyst**: SecOps Pipeline /sec-project-requirements
**Assessment Coverage**: [which skills ran]

---

## Executive Summary

**Security Posture**: 🔴 RED | 🟡 AMBER | 🟢 GREEN

[2–3 sentence rationale]

### What This Project Does
[2 sentences]

### Assessment Coverage
[Which skills ran, which were skipped]

### Top 3 Security Requirements
1. **[SEC-REQ-xxx]** [title] — [plain-language description]
2. **[SEC-REQ-xxx]** [title] — [plain-language description]
3. **[SEC-REQ-xxx]** [title] — [plain-language description]

### Go-Live Readiness
- **Must resolve before go-live (P0):** N items
- **Monitor post go-live (P1):** N items
- **Backlog (P2):** N items

---

## P0 — BLOCKERS (must resolve before go-live)

### SEC-REQ-001: [title]
- **Risk Score**: N (CRITICAL)
- **Source Findings**: [IDs]
- **Requirement**: [what must be implemented]
- **Acceptance Criteria**:
  - [ ] [criterion 1]
  - [ ] [criterion 2]
- **Owner**: [team]
- **Target**: Before go-live

[repeat for each P0]

---

## P1 — HIGH (30 days post go-live)

[same structure]

---

## P2 — MEDIUM (90 days)

[same structure]

---

## Requirements Summary

| ID | Title | Source | Risk Score | Level | Priority | Owner |
|---|---|---|---|---|---|---|

---

## Coverage Gaps

| Skipped Skill | Missing Assessment | Risk |
|---|---|---|
| [skill] | [what wasn't assessed] | [potential exposure] |

---

## Risk Scoring Methodology

Likelihood (1–5) × Impact (1–5).
CRITICAL: 20–25 | HIGH: 12–19 | MEDIUM: 6–11 | LOW: 1–5
```

## Instructions for Claude

1. Read all available upstream files. Note missing ones as coverage gaps.
2. Extract every finding from every source into a unified list. De-duplicate overlapping findings.
3. Score every finding (likelihood × impact).
4. For each finding, write a corresponding requirement with acceptance criteria.
5. Assign priority per the P0/P1/P2 mapping table.
6. Assess overall security posture (RED/AMBER/GREEN).
7. If P0 list is empty: ask *"Blocker olmadan go-live uygundur, onaylıyor musun?"*
8. Write executive summary for a non-technical reader.
9. Write `PROJECT_REQUIREMENTS.md` using the template.
10. Run Gate-REQ checks. Display console summary.

## Hard Rules

- Every finding must produce at least one requirement — findings without a requirement are not actionable.
- Every requirement must have an owner — use "TBD" only when genuinely unknown, and flag it.
- Do not mark gate PASS if P0 list is missing or if any P0 item has no owner.
- Executive summary must be readable without security background.
- Coverage gaps must be explicit — never silently omit an assessment domain.

## Console Summary

```
Security Requirements Complete
================================

Assessment Coverage:
  /sec-threat-model   : [loaded / not available]
  /sec-owasp          : [loaded / not available]
  /sec-regulatory     : [loaded / not available]
  /sec-igrc           : [loaded / not available]

Requirements:
  P0 BLOCKER : N
  P1 HIGH    : N
  P2 MEDIUM  : N
  Total      : N

Security Posture : 🔴 RED | 🟡 AMBER | 🟢 GREEN

Gate-REQ : PASS | WARNING | FAIL

Output : PROJECT_REQUIREMENTS.md

Next Step:
  /sec-signoff    (go-live decision package)
```

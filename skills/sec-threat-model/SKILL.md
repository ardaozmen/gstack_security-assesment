---
name: sec-threat-model
description: Build a STRIDE-based threat model from the project scope. Generates component-threat matrix, trust boundary violation scenarios, and attack trees for critical threats. Use after /sec-scope to identify attack vectors before OWASP or regulatory analysis.
allowed-tools: Read, Write, Glob, Grep
---

# /sec-threat-model — Threat Modeling

## Purpose

Systematically identify threats against every system component using STRIDE. This skill:

- Applies STRIDE to each asset type based on its role
- Analyzes threats at every trust boundary crossing
- Builds attack trees for the highest-risk scenarios
- Produces a threat severity distribution summary

## Usage

```
/sec-threat-model [--focus <asset-name>] [--depth quick|standard|deep]
```

**Arguments**:
- `--focus <asset-name>`: Analyze a single asset only
- `--depth quick`: Cover only CRITICAL + HIGH threats. Default: `standard`

**Triggers**: "tehdit modeli oluştur", "STRIDE analizi", "saldırı senaryoları", "/sec-threat-model"

## Prerequisites

`SCOPE.md` must exist and Gate-SCOPE must be PASS. If missing, run `/sec-scope` first.

## Execution Phases

### Phase 1 — Load Scope

Read `SCOPE.md`. Extract:
- Asset list with types
- Data flows and encryption status
- Trust boundaries with auth methods
- Sensitive data categories

If `SCOPE.md` is missing or Gate-SCOPE failed: stop and instruct user to run `/sec-scope`.

### Phase 2 — Component-Threat Matrix

For each asset, apply STRIDE based on asset type:

| Asset Type | S | T | R | I | D | E |
|---|---|---|---|---|---|---|
| External Entity | ✓ | | ✓ | | | |
| Process / Service | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Data Store | | ✓ | ✓ | ✓ | ✓ | |
| Data Flow | | ✓ | | ✓ | ✓ | |
| Auth Component | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

For each applicable cell, answer:

| STRIDE | Question |
|---|---|
| **Spoofing** | Can identity be forged? Token/session manipulation possible? |
| **Tampering** | Is input validated? Are write operations protected? |
| **Repudiation** | Are critical actions logged with tamper-proof audit trail? |
| **Info Disclosure** | Do error messages leak internals? Is encryption complete? |
| **Denial of Service** | Is rate limiting present? Can resource exhaustion be triggered? |
| **Elevation of Privilege** | Is authorization enforced at every layer? |

### Phase 3 — Data Flow Threat Analysis

For each data flow in SCOPE.md:

1. Is the transport encrypted (TLS 1.2+)?
2. Can an attacker intercept (MITM)?
3. Can a request be replayed?
4. At which layer is the data validated?
5. What is the blast radius if this flow is compromised?

### Phase 4 — Trust Boundary Analysis

For each trust boundary crossing:

1. Who or what is allowed to cross it?
2. What is the authentication mechanism?
3. Where is the authorization decision made?
4. Is every crossing logged?
5. What happens if the boundary is bypassed?

### Phase 5 — Attack Trees

Build an attack tree for every threat with `risk_score >= 12` (risk = likelihood × impact, 1–5 each).

```
Goal: [Unauthorized access to X]
├── Path A: [Authentication bypass]
│   ├── A1: [SQL injection to obtain session token]   — difficulty: medium
│   └── A2: [Brute force weak password]               — difficulty: low
└── Path B: [Abuse of legitimate functionality]
    └── B1: [IDOR to access another user's data]      — difficulty: low
```

Minimum: 1 attack tree. If no threat reaches score 12, build tree for the highest-scored threat.

### Phase 6 — Severity Summary

Tally all identified threats:

```
Total : N
  Critical (score 20–25) : N
  High     (score 12–19) : N
  Medium   (score 6–11)  : N
  Low      (score 1–5)   : N
```

### Phase 7 — Generate threat-modeling.html

Read `docs/word-output-standard.md` to get the full HTML template and CSS standard.

Using the template from `## threat-modeling.html` section:
1. Replace all placeholders with actual content from `THREAT_MODEL.md` and `SCOPE.md`.
2. Insert the Shared CSS block inside `<style>` tags in `<head>`.
3. Apply row classes (`critical`, `high`, `medium`, `low`) based on actual threat severity.
4. Remove all template comments (`<!-- REPEAT ... -->`, `<!-- INSERT ... -->`).
5. Write the completed HTML to `threat-modeling.html` using the Write tool.

The file can be opened directly in Microsoft Word via File → Open.

## Risk Scoring

| Factor | Scale |
|---|---|
| Likelihood | 1 (requires advanced resources) → 5 (trivially exploitable) |
| Impact | 1 (negligible) → 5 (full system compromise) |
| **Risk Score** | Likelihood × Impact |

| Score | Level |
|---|---|
| 20–25 | CRITICAL |
| 12–19 | HIGH |
| 6–11 | MEDIUM |
| 1–5 | LOW |

## Quality Gate — Gate-THREAT

| Check | Required |
|---|---|
| All 6 STRIDE categories addressed (or marked "not applicable") | PASS |
| At least 1 trust boundary violation scenario | PASS |
| At least 1 attack tree | PASS |
| Severity distribution summary present | PASS |
| Every CRITICAL threat has an attack tree | PASS |

## Output File — `THREAT_MODEL.md`

```markdown
# Threat Model

**Based on**: SCOPE.md
**Methodology**: STRIDE
**Date**: [ISO date]
**Analyst**: SecOps Pipeline /sec-threat-model

## Component Threat Matrix

| Asset | Spoofing | Tampering | Repudiation | Info Disclosure | DoS | EoP |
|---|---|---|---|---|---|---|
| [asset] | [finding or N/A] | ... | | | | |

## Data Flow Threats

| Flow | Threat | Category | Severity | Description |
|---|---|---|---|---|

## Trust Boundary Violations

### [Boundary Name]
- **Scenario**: [description]
- **Severity**: CRITICAL | HIGH | MEDIUM | LOW
- **Attack path**: [brief]

## Top Attack Trees

### THREAT-001: [Title] — Risk Score: [N]
```
Goal: [...]
├── Path A: [...]
│   ├── A1: [...] — difficulty: [low/medium/high]
│   └── A2: [...]
└── Path B: [...]
```

## Threat Summary

| Level | Count |
|---|---|
| CRITICAL | N |
| HIGH | N |
| MEDIUM | N |
| LOW | N |
| **Total** | **N** |
```

## Instructions for Claude

1. Read `SCOPE.md`. If absent, stop: instruct user to run `/sec-scope`.
2. For each asset in the inventory, build the STRIDE row.
3. For each data flow, answer the 5 data flow questions.
4. For each trust boundary, answer the 5 boundary questions.
5. Score every identified threat (likelihood × impact).
6. Build attack trees for all threats with score ≥ 12.
7. Compile severity distribution.
8. Write `THREAT_MODEL.md` using the template above.
9. Run Gate-THREAT checks.
10. Execute Phase 7: read `docs/word-output-standard.md`, generate `threat-modeling.html`.
11. Display console summary. Suggest `/sec-owasp` (and `/sec-regulatory` in parallel if running full mode).

## Hard Rules

- Do not skip any STRIDE category — write "N/A — [reason]" if truly not applicable.
- Do not mark gate PASS if no attack tree exists.
- Do not invent threat actors or scenarios not supportable from SCOPE.md.
- Every CRITICAL finding requires an attack tree entry.

## Console Summary

```
Threat Model Complete
=====================

Framework  : STRIDE
Assets Analyzed       : N
Data Flows Analyzed   : N
Trust Boundaries      : N

Threats Identified:
  Critical : N
  High     : N
  Medium   : N
  Low      : N
  Total    : N

Attack Trees Built : N

Gate-THREAT : PASS | WARNING | FAIL

Outputs : THREAT_MODEL.md
          threat-modeling.html

Next Steps:
  /sec-owasp          (technical findings)
  /sec-regulatory     (compliance — can run in parallel)
```

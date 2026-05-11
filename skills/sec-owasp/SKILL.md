---
name: sec-owasp
description: Assess the system against OWASP Top 10 (2021). Generates exploit scenarios, impacted asset mapping, and security requirements for A01–A10. Use for web/API application security evaluation after scope and threat model are complete.
allowed-tools: Read, Write, Glob, Grep
---

# /sec-owasp — OWASP Top 10 Assessment

## Purpose

Evaluate the system against all 10 OWASP Top 10 (2021) categories. This skill:

- Produces structured findings for A01–A10
- Writes concrete exploit scenarios (not theoretical risk statements)
- Assigns severity and confidence to every finding
- Identifies the top 3 critical risks for executive attention

## Usage

```
/sec-owasp [--category <A01-A10>] [--depth quick|standard|deep]
```

**Arguments**:
- `--category <A01>`: Run a single category only (e.g. `--category A03`)
- `--depth quick`: Covers only CRITICAL findings. Default: `standard`

**Triggers**: "OWASP analizi", "web güvenliği değerlendirmesi", "uygulama güvenliği", "/sec-owasp"

## Prerequisites

- `SCOPE.md` required (Gate-SCOPE PASS)
- `THREAT_MODEL.md` recommended — if absent, note assumptions

## Execution Phases

### Phase 1 — Load Context

Read `SCOPE.md` and `THREAT_MODEL.md` (if exists). If `THREAT_MODEL.md` is absent, record:
`[ASSUMPTION-OWASP-001]: Running without threat model — coverage may be reduced for context-specific vectors.`

### Phase 2 — Systematic A01–A10 Analysis

Work through each category in order. For each, answer the category-specific questions:

**A01 — Broken Access Control**
- IDOR (object-level authorization) on every API endpoint?
- Horizontal and vertical privilege escalation paths?
- JWT / session token validated on every request?
- Admin functions protected?
- Directory traversal possible?

**A02 — Cryptographic Failures**
- Sensitive data encrypted at rest and in transit?
- Weak algorithms in use (MD5, SHA1, DES, RC4)?
- Certificate management and expiry tracking?
- Hardcoded credentials in source or config?
- Key storage outside application code?

**A03 — Injection**
- SQL, NoSQL, LDAP, OS command, SSTI, XXE injection possible?
- Parameterized queries / prepared statements used?
- Input validation and sanitization coverage?
- ORM misuse possible?

**A04 — Insecure Design**
- Defense in depth and least privilege applied?
- Business logic flaws (race conditions, negative amounts, replay)?
- Threat modeling done at design time?
- Security stories present in development process?

**A05 — Security Misconfiguration**
- Default credentials on any component?
- Unnecessary open ports, services, or features enabled?
- Stack traces or verbose error messages exposed externally?
- Security headers present (CSP, HSTS, X-Frame-Options, X-Content-Type)?
- Cloud storage buckets private?

**A06 — Vulnerable and Outdated Components**
- Known CVEs in used libraries (check NVD / Snyk / OSV)?
- Dependency update process defined?
- End-of-life components in use?
- Container base images pinned and scanned?

**A07 — Identification and Authentication Failures**
- MFA implemented for privileged or sensitive accounts?
- Password policy enforces strength?
- Brute force protection (rate limiting, lockout)?
- Session management (timeout, logout, concurrent session control)?
- Credential storage hashed with bcrypt/argon2?

**A08 — Software and Data Integrity Failures**
- CI/CD pipeline security controls?
- Unsigned updates or insecure deserialization?
- Supply chain attack surface (npm, pip, etc.)?
- Build artifacts integrity verified?

**A09 — Security Logging and Monitoring Failures**
- Critical events (auth failure, access denied, data export) logged?
- Log integrity protected (tamper detection)?
- Anomaly detection or alerting configured?
- Log retention ≥ 5 years (BDDK requirement for regulated sectors)?
- Sensitive data masked in logs?

**A10 — Server-Side Request Forgery (SSRF)**
- Endpoints that fetch external URLs exist?
- Cloud metadata endpoint (169.254.169.254) blocked?
- Allowlist for outbound requests defined?
- DNS rebinding protection?

### Phase 3 — Structure Each Finding

Every finding must have all 6 fields:

```yaml
- id: OWASP-A01-001
  risk_title: "IDOR via /api/accounts/{id}"
  risk_category: "A01 Broken Access Control"
  severity: CRITICAL | HIGH | MEDIUM | LOW | INFO
  exploit_scenario: |
    Attacker authenticates as user A, then replaces {id} in
    GET /api/accounts/{id} with user B's account ID.
    No object-level authorization check exists → full account data exposed.
  impacted_asset: "[asset name from SCOPE.md]"
  confidence: HIGH | MEDIUM | LOW
  assumptions:
    - "[any assumption made due to missing info]"
  security_requirement: |
    Every API call must verify the requesting user owns the resource.
    Unauthorized attempts must be logged and alerted.
```

### Phase 4 — Confidence Calibration

| Score | Meaning |
|---|---|
| HIGH | Confirmed from scope/threat model context; exploit path is clear |
| MEDIUM | Pattern match; likely correct but not fully verifiable |
| LOW | Possible; significant assumptions required |

Suppress LOW confidence findings from the summary table. Include in appendix with caveat.

### Phase 5 — Top 3 Critical Risks

Select the 3 highest-severity, highest-confidence findings for the executive summary.
If fewer than 3 CRITICAL findings, fill from HIGH.
If no CRITICAL or HIGH findings: state "No critical risks identified."

## Quality Gate — Gate-OWASP

| Check | Required |
|---|---|
| A01–A10 each addressed or marked "not applicable for this architecture" | PASS |
| Every finding has: risk_title, severity, exploit_scenario, confidence | PASS |
| Top 3 critical risks listed or "no critical risks" stated | PASS |
| Total finding count reported | PASS |
| LOW confidence CRITICAL findings flagged for verification | WARNING |
| If CRITICAL count ≥ 3: user confirmation to continue pipeline | TASTE DECISION |

## Output File — `OWASP_FINDINGS.md`

```markdown
# OWASP Top 10 Assessment

**Project**: [name]
**Date**: [ISO date]
**Standard**: OWASP Top 10 2021
**Analyst**: SecOps Pipeline /sec-owasp

## Executive Summary

| Severity | Count |
|---|---|
| CRITICAL | N |
| HIGH | N |
| MEDIUM | N |
| LOW | N |
| **Total** | **N** |

Coverage gaps: [categories with reduced confidence due to missing info]

## Top 3 Critical Risks

1. **[OWASP-A0X-001]** [risk_title] — [one-line impact]
2. **[OWASP-A0X-002]** [risk_title] — [one-line impact]
3. **[OWASP-A0X-003]** [risk_title] — [one-line impact]

## Findings by Category

### A01 — Broken Access Control

#### OWASP-A01-001: [risk_title]
- **Severity**: CRITICAL
- **Confidence**: HIGH
- **Impacted Asset**: [asset]
- **Exploit Scenario**: [description]
- **Security Requirement**: [what must be implemented]

[repeat for each finding]

### A02 — Cryptographic Failures
...

[A01 through A10]

## Key Assumptions

- [ASSUMPTION-OWASP-001]: [description]

## Missing Information

- [MISSING-OWASP-001]: [description] — BLOCKER | WARNING
```

## Instructions for Claude

1. Read `SCOPE.md`. Read `THREAT_MODEL.md` if it exists; otherwise record the assumption.
2. Work through A01–A10 in sequence. For each, answer all category-specific questions.
3. For each identified vulnerability, fill all 6 required fields.
4. Assign confidence per the calibration table.
5. If CRITICAL findings ≥ 3, pause: *"Bu kadar kritik bulguyla pipeline devam etmeli mi?"*
6. Compile top 3 critical risks.
7. Write `OWASP_FINDINGS.md` using the template.
8. Run Gate-OWASP checks.
9. Display console summary.

## Hard Rules

- Every category A01–A10 must appear in the output — write "not applicable" with a reason rather than skipping.
- Every finding needs an exploit scenario — no theoretical-only risks.
- Do not report LOW confidence findings in the main summary.
- Do not mark gate PASS if any category is completely absent without explanation.

## Console Summary

```
OWASP Top 10 Assessment Complete
==================================

Standard : OWASP Top 10 2021

Findings:
  Critical : N
  High     : N
  Medium   : N
  Low      : N
  Total    : N

Coverage Gaps (low confidence) : N categories
Assumptions                    : N

Gate-OWASP : PASS | WARNING | FAIL

Output : OWASP_FINDINGS.md

Next Step:
  /sec-regulatory     (compliance — runs in parallel with this step)
  /sec-risk-report    (after all parallel steps complete)
```

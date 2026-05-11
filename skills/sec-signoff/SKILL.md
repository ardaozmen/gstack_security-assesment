---
name: sec-signoff
description: Prepare a go-live security sign-off package with GO/NO_GO/CONDITIONAL_GO recommendation. Reviews blockers from PROJECT_REQUIREMENTS.md, maps required approvals, and produces the escalation matrix. Final step before human decision. Never makes the decision itself.
allowed-tools: Read, Write, Glob, Grep
---

# /sec-signoff — Security Sign-off Package

## Purpose

Prepare all information needed for a human go-live decision. This skill:

- Reads `PROJECT_REQUIREMENTS.md` for P0 BLOCKER status and security posture
- Determines which approvals are required (CISO, Legal, Executive)
- Produces a recommendation: GO / NO_GO / CONDITIONAL_GO
- Lists post-go-live obligations with owners and dates

**This skill produces a recommendation — the final decision belongs to the authorized human.**

## Usage

```
/sec-signoff [--dry-run]
```

**Arguments**:
- `--dry-run`: Generate sign-off package without marking pipeline complete

**Triggers**: "sign-off", "onay hazırlığı", "go-live kararı", "can we ship", "/sec-signoff"

## Prerequisites

- `PROJECT_REQUIREMENTS.md` required (Gate-REQ PASS)

## Execution Phases

### Phase 1 — Load Project Requirements

Read `PROJECT_REQUIREMENTS.md`. If missing or Gate-REQ did not PASS: stop and instruct user to run `/sec-project-requirements`.

Extract:
- P0 BLOCKER list and resolution status
- Security posture (RED / AMBER / GREEN)
- P1 HIGH requirements with owners and target dates
- Regulatory penalty items (`regulatory_penalty: YES`)

### Phase 2 — Blocker Check

Evaluate every P0 requirement:

| Outcome | Condition |
|---|---|
| **NO_GO** | Any P0 requirement unresolved |
| **CONDITIONAL_GO** | No P0 blockers; open P1 requirements with defined owners and dates |
| **GO** | No P0 blockers; no open P1 requirements (or all resolved) |

If recommendation is NO_GO: ask *"Hangi koşullar sağlanırsa CONDITIONAL_GO'ya geçilebilir?"*

### Phase 3 — Required Approvals Mapping

| Condition | Required Approval |
|---|---|
| Any P0 BLOCKER present | CISO |
| `regulatory_penalty: YES` + CRITICAL finding | CISO + Legal |
| Security posture = RED | CISO + Executive |
| NO_GO recommendation | CISO + CTO + Management |

### Phase 4 — Post-Go-Live Obligations

List all open P1 and P2 requirements from `PROJECT_REQUIREMENTS.md` as binding obligations:

```
- [ ] [SEC-REQ-xxx] [title] — Owner: [team] — Due: [date]
```

If any P1 item lacks an owner or date: pause and request from user.

### Phase 5 — Escalation Matrix

| Trigger | Escalation Path |
|---|---|
| Unresolved P0 at go-live | CISO → CTO → Board |
| CRITICAL regulatory finding | Legal + CISO (parallel) |
| Post-launch security incident | Incident Management → CISO |

### Phase 6 — Conditional Check

If `regulatory_penalty: YES` + `CONDITIONAL_GO`: ask *"Bu kombinasyon Hukuk onayı gerektiriyor. Hukuk bildirim metnini şimdi hazırlayayım mı?"*

## Quality Gate — Gate-SIGNOFF

| Check | Required |
|---|---|
| Recommendation (GO / NO_GO / CONDITIONAL_GO) explicitly stated | PASS |
| Rationale ≥ 2 sentences | PASS |
| Open blockers listed (or "none" explicitly stated) | PASS |
| Required approvals section present with each marked required/not required | PASS |
| Post-go-live obligations list present | PASS |
| Escalation matrix present | PASS |
| NO_GO + no conditions defined: pause for human input | TASTE DECISION |
| `regulatory_penalty: YES` + CONDITIONAL_GO: legal check | TASTE DECISION |

## Output File — `SIGNOFF_PACKAGE.md`

```markdown
# Security Sign-off Package

**Project**: [name]
**Assessment Date**: [ISO date]
**Prepared By**: SecOps Pipeline /sec-signoff
**Based On**: PROJECT_REQUIREMENTS.md

---

## Decision Recommendation

> **STATUS: GO | NO_GO | CONDITIONAL_GO**

### Rationale

[Minimum 2 sentences]

---

## Open Blockers (P0)

[List each unresolved P0 requirement, or:]
> No blockers identified.

## Accepted Risks (Conditional Go)

| Req ID | Title | Risk Level | Acceptance Rationale | Owner | Due Date |
|---|---|---|---|---|---|

## Required Approvals

| Approver | Required | Status |
|---|---|---|
| CISO | Yes / No | [ ] Pending |
| Legal | Yes / No | [ ] Pending |
| CTO | Yes / No | [ ] Pending |

## Post-Go-Live Obligations

- [ ] [SEC-REQ-xxx] [title] — Owner: [team] — Due: [date]

## Escalation Matrix

| Trigger | Path |
|---|---|
| Unresolved P0 | CISO → CTO → Board |
| CRITICAL regulatory | Legal + CISO |
| Post-launch incident | SecOps → CISO |

---

> **IMPORTANT**: This document is a recommendation prepared by the SecOps Pipeline.
> The final go-live decision rests with the authorized signatories listed above.
> This assessment is not a substitute for professional penetration testing.
```

## Instructions for Claude

1. Read `PROJECT_REQUIREMENTS.md`. If absent, stop: instruct to run `/sec-project-requirements`.
2. Check every P0 requirement for resolution status.
3. Determine GO / NO_GO / CONDITIONAL_GO.
4. If NO_GO: ask what conditions would enable CONDITIONAL_GO.
5. Map required approvals.
6. List all P1/P2 items as post-go-live obligations.
7. If any P1 item has no owner or date: request from user.
8. If `regulatory_penalty: YES` + CONDITIONAL_GO: ask about legal notification.
9. Write `SIGNOFF_PACKAGE.md`.
10. Run Gate-SIGNOFF. Display console summary.
11. Remind: *"Nihai karar yetkisi sizde — bu belge bir öneridir."*

## Hard Rules

- Never present the recommendation as a final decision.
- Never write GO if any P0 requirement is unresolved.
- Do not omit the disclaimer from `SIGNOFF_PACKAGE.md`.
- Every post-go-live obligation must have an owner.

## Console Summary

```
Sign-off Package Complete
==========================

Recommendation : GO | NO_GO | CONDITIONAL_GO

P0 Blockers Unresolved : N
P1 Open Requirements   : N
Post-Go-Live Items     : N

Required Approvals:
  CISO   : required | not required
  Legal  : required | not required
  CTO    : required | not required

Gate-SIGNOFF : PASS | WARNING | FAIL

Output : SIGNOFF_PACKAGE.md

⚠  Final decision authority: authorized signatories only.
   Run /sec-retro to capture learnings from this assessment.
```

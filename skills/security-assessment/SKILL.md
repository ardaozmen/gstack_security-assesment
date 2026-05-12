---
name: security-assessment
description: Orchestrate the full security assessment pipeline. Runs all skills in the correct order, enforces quality gates, manages state between steps, and surfaces human decision points. Use to run the complete assessment in one command.
allowed-tools: Read, Write, Glob, Grep
---

# /security-assessment — Security Assessment Orchestrator

## Purpose

Run the complete security assessment pipeline from a single command. This skill:

- Parses mode and parameters to build an execution plan
- Runs each skill in dependency order, enforcing gates
- Carries context between steps via `PIPELINE_CONTEXT.md`
- Pauses at taste decision points for human input
- Resumes interrupted pipelines from the last failed step

**This skill manages the process — it does not override decisions or bypass gates.**

## Usage

```
/security-assessment [mode=full|fast|compliance] [resume] [retry_from=<skill-id>] [force_refresh=true]
```

**Arguments**:
- `mode=full` (default): Run all 7 steps in order
- `mode=fast`: Run `/sec-scope` → `/sec-owasp` → `/sec-project-requirements`
- `mode=compliance`: Run `/sec-scope` → `/sec-regulatory` → `/sec-igrc` → `/sec-project-requirements` → `/sec-signoff`
- `resume`: Continue from last FAIL recorded in `AUTO_PLAN_STATUS.md`
- `retry_from=<skill-id>`: Re-run from a specific skill (e.g. `retry_from=sec-owasp`)
- `force_refresh=true`: Ignore existing output files and regenerate all steps

**Triggers**: "security assessment", "pipeline'ı başlat", "tam güvenlik değerlendirmesi yap", "tüm adımları çalıştır", "/security-assessment"

## Prerequisites

Minimum: project name and 2-sentence description from user.

## Pipeline Definitions

### Full Mode (default)

```
/sec-scope
      │
      ▼
/sec-threat-model
 ┌────┴──────────────────┐
 ▼                        ▼
/sec-owasp       /sec-regulatory
 │                        │
 │                   /sec-igrc
 │                        │
 └──────────┬─────────────┘
            ▼
/sec-project-requirements
            │
            ▼
     /sec-signoff
```

### Fast Mode
`/sec-scope` → `/sec-owasp` → `/sec-project-requirements`

### Compliance Mode
`/sec-scope` → `/sec-regulatory` → `/sec-igrc` → `/sec-project-requirements` → `/sec-signoff`

### Post-Pipeline (optional)
`/sec-retro` — run after `/sec-signoff` to capture cross-project learnings.

## Execution Phases

### Phase 0 — Startup

**0a — Parse command**
Determine mode, retry target, and refresh flag.

**0b — Check existing outputs** (skip if `force_refresh=true`)
For each skill in the selected mode, check if its primary output file exists and passed its gate.
If yes: skip re-running, carry the artifact forward.

| Skill | Output file to check |
|---|---|
| /sec-scope | SCOPE.md |
| /sec-threat-model | THREAT_MODEL.md |
| /sec-owasp | OWASP_FINDINGS.md |
| /sec-regulatory | REGULATORY_FINDINGS.md |
| /sec-igrc | IGRC_FINDINGS.md |
| /sec-project-requirements | PROJECT_REQUIREMENTS.md |
| /sec-signoff | SIGNOFF_PACKAGE.md |

**0c — Collect minimum project context** (if not in `PIPELINE_CONTEXT.md`)
Ask in one message:
1. Project name and one-line description
2. Project type (new build / integration / third-party)
3. Regulated sector? (finans/BDDK, sermaye piyasası/SPK, other)

### Phase 1 — Context Management

Before each step, update `PIPELINE_CONTEXT.md`:

```markdown
# Pipeline Context Snapshot

**Updated**: [ISO datetime]
**Current Step**: [skill-id]
**Mode**: [full|fast|compliance]

## Project Summary
[2 sentences max]

## Key Decisions Made
- [DECISION-001]: [description] — Step: [skill-id]

## Critical Findings So Far
- [CRITICAL-001]: [title] — Source: [skill-id]

## Open Taste Decisions
- [TASTE-001]: [question] — awaiting

## Completed Steps
| Skill | Status | Output | Warnings |
|---|---|---|---|
| /sec-scope | PASS | SCOPE.md | 1 |
```

### Phase 2 — Execution Loop

For each skill in the plan:

1. Update `PIPELINE_CONTEXT.md` with current step.
2. Load the skill's `SKILL.md` and execute it.
3. Verify the expected output file exists.
4. Run the skill's quality gate.
5. Handle gate result:
   - **PASS**: update context, proceed.
   - **WARNING**: log, notify user, continue.
   - **FAIL**: stop (see Phase 3).
6. Resolve any taste decisions before proceeding.
7. Update `AUTO_PLAN_STATUS.md`.

### Phase 3 — Failure Handling

On gate FAIL:

```
PIPELINE STOPPED — Gate-[NAME] FAIL

Reason  : [specific check that failed]
Step    : [skill-id]
Output  : [expected file]

Required Actions:
  1. [specific question or fix]
  2. [specific question or fix]

Resume command:
  /security-assessment resume
```

On WARNING: log, notify, continue.

### Phase 4 — Taste Decision Handling

When a skill raises a taste decision:

```
⚠ Taste Decision Required

Question : [clear question]
Context  : [why this matters]
Options  : [A] [B]

Your answer will be recorded in PIPELINE_CONTEXT.md.
```

Record the answer. Resume.

### Phase 5 — Final Status

On completion, write `AUTO_PLAN_STATUS.md`:

```markdown
# Security Assessment — Final Status

**Mode**: [full|fast|compliance]
**Date**: [ISO date]
**Overall Status**: SUCCESS | PARTIAL | FAILED

## Step Results

| Step | Skill | Status | Output | Taste Decisions | Warnings |
|---|---|---|---|---|---|
| 1 | /sec-scope | PASS | SCOPE.md | 0 | 1 |
| 2 | /sec-threat-model | PASS | THREAT_MODEL.md | 1 | 0 |
| 3 | /sec-owasp | PASS | OWASP_FINDINGS.md | 2 | 0 |
| 4 | /sec-regulatory | PASS | REGULATORY_FINDINGS.md | 1 | 2 |
| 5 | /sec-igrc | PASS | IGRC_FINDINGS.md | 1 | 1 |
| 6 | /sec-project-requirements | PASS | PROJECT_REQUIREMENTS.md | 1 | 0 |
| 7 | /sec-signoff | PASS | SIGNOFF_PACKAGE.md | 0 | 0 |

## Key Decisions
- [DECISION-001]: [description]

## Open Warnings
- [WARNING-001]: [description]

## Output Files
- SCOPE.md
- THREAT_MODEL.md
- OWASP_FINDINGS.md
- REGULATORY_FINDINGS.md
- IGRC_FINDINGS.md
- RACI_MATRIX.md
- PROJECT_REQUIREMENTS.md
- project-requirements.html
- threat-modeling.html
- SIGNOFF_PACKAGE.md
- AUTO_PLAN_STATUS.md
- PIPELINE_CONTEXT.md

## Final Posture
[RED/AMBER/GREEN + rationale from PROJECT_REQUIREMENTS.md]

## Recommended Next Command
[ ] /sec-signoff    — requires authorized human decision
[ ] /sec-retro      — capture learnings for future assessments
```

## Retry Semantics

| Command | Behavior |
|---|---|
| `/security-assessment` | Full pipeline, all steps |
| `/security-assessment resume` | Continue from last FAIL in `AUTO_PLAN_STATUS.md` |
| `/security-assessment mode=fast` | Fast mode |
| `/security-assessment mode=compliance` | Compliance mode |
| `/security-assessment force_refresh=true` | Regenerate all outputs |
| `/security-assessment retry_from=sec-owasp` | Re-run from `/sec-owasp` onward |

## Quality Gate — Orchestrator State

| Check | Required |
|---|---|
| Execution order matches mode definition | PASS |
| No step skipped without gate PASS | PASS |
| `PIPELINE_CONTEXT.md` updated before each step | PASS |
| `AUTO_PLAN_STATUS.md` updated after each step | PASS |
| All taste decisions recorded with user response | PASS |
| `/sec-signoff` not marked SUCCESS without human sign-off | PASS |

## Hard Rules

- `/sec-scope` is always first — no exceptions.
- Gate FAIL stops the pipeline immediately.
- Every taste decision requires a user answer before proceeding.
- `/sec-project-requirements` cannot run until all its active-mode dependencies have PASS gates.
- `/sec-signoff` output is a recommendation — pipeline SUCCESS ≠ go-live approved.
- `PIPELINE_CONTEXT.md` must be updated before every step.

## Console Summary (per step)

```
▶ Running /sec-[skill] ...
  ✓ Gate-[NAME] : PASS | ⚠ WARNING | ✗ FAIL
```

## Console Summary (final)

```
Security Assessment Pipeline Complete
======================================

Mode   : full | fast | compliance
Status : SUCCESS | PARTIAL | FAILED

Steps Completed : N / N
Warnings        : N
Taste Decisions : N

Security Posture : 🔴 RED | 🟡 AMBER | 🟢 GREEN

Output Files:
  SCOPE.md
  THREAT_MODEL.md
  OWASP_FINDINGS.md
  REGULATORY_FINDINGS.md
  IGRC_FINDINGS.md
  RACI_MATRIX.md
  PROJECT_REQUIREMENTS.md
  project-requirements.html
  threat-modeling.html
  SIGNOFF_PACKAGE.md
  AUTO_PLAN_STATUS.md
  PIPELINE_CONTEXT.md

Next Steps:
  /sec-signoff    — requires authorized human decision
  /sec-retro      — optional: capture cross-project learnings
```

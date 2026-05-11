---
name: sec-retro
description: Security assessment retrospective that learns across projects. Compares current findings to historical patterns, identifies recurring vulnerabilities, extracts durable learnings, and saves them globally for future assessments. Run after pipeline completes.
allowed-tools: Read, Write, Glob, Grep
---

# /sec-retro — Cross-Project Security Retrospective

## Purpose

Extract durable learnings from completed assessments and build a cross-project knowledge base. This skill:

- Compares current findings to historical patterns from past assessments
- Identifies recurring vulnerabilities (systemic vs. project-specific)
- Surfaces which P0 items were actually exploited or caused incidents post-launch
- Saves learnings globally so future assessments start with institutional knowledge

**This skill runs after the pipeline completes — it is not part of the main assessment flow.**

## Usage

```
/sec-retro [--project <name>] [--compare <previous-date>] [--global]
```

**Arguments**:
- `--project <name>`: Specify project name if multiple assessments exist
- `--compare <YYYY-MM-DD>`: Compare against a specific prior assessment date
- `--global`: Show cross-project patterns only (no current-project diff)

**Triggers**: "retro yap", "öğrendiklerini kaydet", "geçmiş değerlendirmelerle karşılaştır", "ne öğrendik", "/sec-retro"

## Prerequisites

At least one completed pipeline run producing `PROJECT_REQUIREMENTS.md`.
Prior assessments stored in `.assessments/` (auto-created by this skill on first run).

## Storage Locations

| Location | Contents | Scope |
|---|---|---|
| `.assessments/YYYY-MM-DD/` | Snapshot of all pipeline outputs for that run | Project-local |
| `.assessments/RETRO_REPORT.md` | Latest retro report | Project-local |
| `~/.security-assessments/learnings.md` | Cross-project recurring patterns | Global |
| `~/.security-assessments/index.json` | Index of all assessed projects | Global |

## Execution Phases

### Phase 1 — Archive Current Assessment

Before comparing, snapshot all current pipeline outputs:

```
.assessments/
└── YYYY-MM-DD/
    ├── SCOPE.md
    ├── THREAT_MODEL.md         (if ran)
    ├── OWASP_FINDINGS.md       (if ran)
    ├── REGULATORY_FINDINGS.md  (if ran)
    ├── IGRC_FINDINGS.md        (if ran)
    ├── RACI_MATRIX.md          (if ran)
    ├── PROJECT_REQUIREMENTS.md
    ├── SIGNOFF_PACKAGE.md      (if ran)
    └── meta.json               ← project name, mode, date, posture
```

`meta.json` structure:
```json
{
  "project": "[name]",
  "date": "YYYY-MM-DD",
  "mode": "full|fast|compliance",
  "posture": "RED|AMBER|GREEN",
  "p0_count": N,
  "p1_count": N,
  "p2_count": N,
  "skills_ran": ["sec-scope", "sec-owasp", "..."]
}
```

### Phase 2 — Load Global Learnings

Read `~/.security-assessments/learnings.md` if it exists.
Read `~/.security-assessments/index.json` to find prior assessments of this project or similar projects.

If neither exists: this is the first global run. Initialize both files after Phase 5.

### Phase 3 — Within-Project Comparison

If prior assessments exist for this project (`.assessments/YYYY-MM-DD/`):

Compare current `PROJECT_REQUIREMENTS.md` to the most recent prior snapshot:

| Finding category | Question |
|---|---|
| **Resolved** | Which P0/P1 items from the prior run are gone? Were they fixed or just not assessed? |
| **Recurring** | Which findings appear in both runs? How many cycles has this been open? |
| **New** | What appeared this run that wasn't in the prior run? |
| **Posture trend** | RED → AMBER → GREEN over time, or regressing? |

For each recurring P0 finding open for more than 1 assessment cycle, flag as:
```
⚠ RECURRING BLOCKER: [finding title] — open for N assessment cycles
```

### Phase 4 — Cross-Project Pattern Analysis

Load all entries in `~/.security-assessments/index.json`.
For each project's archived findings, identify patterns:

**Recurring vulnerability classes** (appear in ≥ 30% of assessed projects):
```
Pattern: "IDOR on REST APIs"
  Seen in: Project A (2024-01), Project B (2024-03), Project C (2024-06)
  Frequency: 3 of 5 projects (60%)
  Typical severity: CRITICAL
  Root cause: Object-level authorization not enforced by default in [framework]
  Standard fix: [mitigation approach]
```

**Sector-specific patterns** (if projects share a sector):
- Finance: BDDK log retention non-compliance most common
- All: MFA missing on admin interfaces

**Assessment process patterns** (where gates failed most):
- Which gate fails most often?
- Which skill produces the most P0 findings?

### Phase 5 — Extract and Classify Learnings

For each finding, classify:

```yaml
- id: LEARNING-001
  type: RECURRING_VULN | SECTOR_PATTERN | PROCESS_IMPROVEMENT | FIXED_SUCCESSFULLY
  title: "[short description]"
  description: "[what was learned]"
  seen_in_projects: ["Project A", "Project B"]
  occurrence_count: N
  last_seen: "YYYY-MM-DD"
  recommendation: "[what to check first in future assessments]"
  applies_to: "all | finans | e-ticaret | sağlık"
```

Types:
- `RECURRING_VULN`: vulnerability that appears repeatedly across projects
- `SECTOR_PATTERN`: gap common in a specific sector/regulation
- `PROCESS_IMPROVEMENT`: pipeline or skill that should change based on experience
- `FIXED_SUCCESSFULLY`: a P0 item that was resolved — record how it was fixed

### Phase 6 — Update Global Learnings

Append new or update existing entries in `~/.security-assessments/learnings.md`.

**Never overwrite** an existing learning — only append or update `last_seen` and `occurrence_count`.
**Never include** project names, PII, or proprietary system details in global learnings.

Format:

```markdown
# Security Assessment Learnings

Last updated: [ISO date]
Projects assessed: N
Total learnings: N

## Recurring Vulnerabilities

### LEARNING-001: [title]
- **Type**: RECURRING_VULN
- **Frequency**: N of M projects (%)
- **Sectors**: [list or "all"]
- **Description**: [what was learned — generic, no project names]
- **Recommendation**: [what to check first in future assessments]
- **Last seen**: [YYYY-MM-DD]

## Sector Patterns

[same structure]

## Process Improvements

[same structure]
```

Update `~/.security-assessments/index.json`:
```json
{
  "total_projects": N,
  "last_updated": "YYYY-MM-DD",
  "projects": [
    {"name": "hash-or-alias", "date": "YYYY-MM-DD", "posture": "AMBER", "sector": "finans"}
  ]
}
```

Use a project alias or hash — never store sensitive project names globally.

## Quality Gate — Gate-RETRO

| Check | Required |
|---|---|
| Current assessment archived to `.assessments/YYYY-MM-DD/` | PASS |
| Within-project comparison completed (or first-run noted) | PASS |
| Cross-project patterns analyzed (or first global run noted) | PASS |
| At least 1 learning extracted or "no new learnings" stated | PASS |
| Global learnings file updated | PASS |
| No PII or proprietary data in global learnings | PASS |

## Output Files

### `.assessments/YYYY-MM-DD/` (project-local)
Full snapshot of all pipeline outputs for this run.

### `.assessments/RETRO_REPORT.md` (project-local)

```markdown
# Security Assessment Retro

**Project**: [name]
**Date**: [ISO date]
**Prior Run**: [date or "first run"]

## Posture Trend

[GREEN / AMBER / RED over time — or "first assessment"]

## Within-Project: What Changed

### ✅ Resolved Since Last Run
- [finding] — fixed in [date]

### ⚠ Recurring (still open)
- [finding] — open for N cycles

### 🆕 New This Run
- [finding]

## Cross-Project Patterns Applied

[Which global learnings were relevant to this assessment]
[Did we find a known pattern? Did we miss it on first pass?]

## New Learnings Extracted

[What we learned from this project that will inform future assessments]

## Recommended Focus Areas for Next Assessment

Based on history, these areas should be prioritized:
1. [area] — [reason]
2. [area] — [reason]
```

### `~/.security-assessments/learnings.md` (global)
Updated cross-project knowledge base.

## Instructions for Claude

1. Archive all current pipeline outputs to `.assessments/YYYY-MM-DD/` with `meta.json`.
2. Read `~/.security-assessments/learnings.md` and `index.json` if they exist.
3. If prior runs exist for this project: diff current vs. prior findings.
4. Flag any finding open for more than 1 cycle as RECURRING BLOCKER.
5. Load cross-project index. Identify patterns across ≥ 30% of projects.
6. Extract and classify new learnings.
7. Update `~/.security-assessments/learnings.md` — append only, never overwrite.
8. Update `~/.security-assessments/index.json` using project alias.
9. Write `.assessments/RETRO_REPORT.md`.
10. Run Gate-RETRO. Display console summary.

## Hard Rules

- Never store project names, hostnames, IP addresses, or PII in global learnings.
- Never overwrite an existing learning — update `last_seen` and `occurrence_count` only.
- Never run during an active pipeline — only after `/sec-signoff` completes.
- Recurring BLOCKER (open ≥ 2 cycles) must be flagged explicitly — do not normalize it.
- Archive is write-once — do not modify past snapshots.

## Console Summary

```
Security Retro Complete
========================

Assessment Archived : .assessments/[date]/

Within-Project Diff:
  Resolved  : N findings
  Recurring : N findings (⚠ flag if any)
  New       : N findings

Cross-Project Analysis:
  Projects in global index : N
  Patterns matched         : N
  New learnings extracted  : N

Gate-RETRO : PASS | WARNING | FAIL

Outputs:
  .assessments/[date]/          (archive)
  .assessments/RETRO_REPORT.md  (project retro)
  ~/.security-assessments/learnings.md  (updated)

Next Assessment:
  Run /sec-autoplan — global learnings will be available.
```

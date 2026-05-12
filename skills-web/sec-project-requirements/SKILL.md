---
name: sec-project-requirements
description: Consolidates all assessment findings into prioritized security requirements. Produces the project-requirements.html artifact at the end.
---

# /sec-project-requirements — Security Requirements

## Purpose

Transform all analysis outputs from the conversation (scope, threat model, OWASP, regulatory, igrc) into a single prioritized requirements document.
This is an assessment document — not a decision-making mechanism.

## Language Rule

Use the same language the user is writing in for all output.

## Execution Instructions

### Step 1 — Collect All Findings

Pull findings from the following analyses in the conversation:
- /sec-threat-model → threats and attack scenarios
- /sec-owasp → application security vulnerabilities
- /sec-regulatory → compliance gaps
- /sec-igrc → control and ownership gaps

Build a unified finding list. Merge findings that point to the same root cause and cite both source IDs.

### Step 2 — Risk Scoring

For every finding: **Risk = Likelihood (1–5) × Impact (1–5)**

| Score | Level |
|---|---|
| 20–25 | CRITICAL |
| 12–19 | HIGH |
| 6–11 | MEDIUM |
| 1–5 | LOW |

### Step 3 — Translate to Requirements

For every finding, write a corresponding security requirement:

```
SEC-REQ-001
Title       : [what needs to be done]
Source      : [OWASP-A01-001, THREAT-003]
Requirement : [what must be implemented — clear and measurable]
Acceptance  :
  - [criterion 1]
  - [criterion 2]
Risk Score  : [N] — [CRITICAL/HIGH/MEDIUM/LOW]
Priority    : [1-CRITICAL / 2-HIGH / 3-MEDIUM]
Owner       : [team or TBD]
```

### Step 4 — Security Posture

| Posture | Condition |
|---|---|
| RED | Any CRITICAL finding unresolved |
| AMBER | HIGH findings present, no CRITICAL |
| GREEN | Only MEDIUM and LOW findings |

Write a 2–3 sentence rationale.

### Step 5 — Executive Summary

For a non-technical reader:
1. What the project does (2 sentences)
2. Which assessments were run
3. The 3 most important security requirements (plain language)
4. Overall security posture

### Step 6 — Write to Conversation

---

## /sec-project-requirements Analysis

### Executive Summary

**Security Posture: RED / AMBER / GREEN**

[2–3 sentence rationale]

**What Does This Project Do?**
[2 sentences]

**Top 3 Requirements**
1. [SEC-REQ-xxx] — [plain description]
2. [SEC-REQ-xxx] — [plain description]
3. [SEC-REQ-xxx] — [plain description]

---

### Critical Requirements (Risk: 20–25)

[Each requirement in the format above]

---

### High Requirements (Risk: 12–19)

[Each requirement in the format above]

---

### Medium Requirements (Risk: 6–11)

[Each requirement in abbreviated format]

---

### Requirements Summary Table

| ID | Title | Source | Risk Score | Level | Owner |
|---|---|---|---|---|---|

### Assessment Coverage
| Skill | Status |
|---|---|
| /sec-threat-model | loaded / missing |
| /sec-owasp | loaded / missing |
| /sec-regulatory | loaded / missing |
| /sec-igrc | loaded / missing |

---

### Step 7 — Generate project-requirements.html Artifact

After the analysis is written, create an HTML artifact named `project-requirements.html`.

Use the `## project-requirements.html` template and shared CSS from `word-output-standard`.
Replace all placeholders with actual content from the analysis.
Apply row classes (`critical`, `high`, `medium`) based on actual risk levels.
Apply the posture class (`posture-red`, `posture-amber`, `posture-green`) based on the result.
Remove all template comments.
Artifact type: `text/html`

## Hard Rules

- Do not read or write any files — all input comes from the conversation.
- Every finding must produce at least one requirement.
- If the owner is unknown, write "TBD" and flag it.
- Do not use decision language (GO / NO-GO / BLOCKER) — this is an assessment document.
- Explicitly document any assessment domain that was not covered.

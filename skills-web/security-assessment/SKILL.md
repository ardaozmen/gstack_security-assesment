---
name: security-assessment
description: Starts the full security assessment pipeline. Reads the project description, runs all steps silently, and produces two HTML documents. Only the step timeline is shown in the conversation.
---

# /security-assessment — Pipeline Orchestrator

## Purpose

Run the complete security assessment pipeline from a single command.
Show only a step-by-step timeline in the conversation — no analysis output.
Produce two HTML artifacts at the end.

## Language Rule

Detect the language the user writes in and use that language for all output throughout the pipeline.

## Usage

```
/security-assessment
[project name and description]
```

## Execution Instructions

### Step 0 — Start

Print the pipeline header:

```
Security Assessment — [Project Name]
=====================================
```

Then immediately run Step 1.

---

### Step 1 — Scope Definition  `/sec-scope`

Apply `/sec-scope` skill instructions in **silent mode** (no analysis output to conversation).

When scope intake is complete, print:

```
  Step 1/5  Scope Definition .............. ✓
```

Then immediately run Step 2.

---

### Step 2 — Threat Modeling  `/sec-threat-model`

Apply `/sec-threat-model` skill instructions in **silent mode**.
After analysis, generate the `threat-modeling.html` artifact.

Print:

```
  Step 2/5  Threat Modeling ............... ✓  →  threat-modeling.html
```

Then immediately run Step 3.

---

### Step 3 — OWASP Analysis  `/sec-owasp`

Apply `/sec-owasp` skill instructions in **silent mode**.

Print:

```
  Step 3/5  OWASP Analysis ................ ✓
```

Then immediately run Step 4.

---

### Step 4 — Regulatory & Controls  `/sec-regulatory` + `/sec-igrc`

Apply `/sec-regulatory` then `/sec-igrc` skill instructions in **silent mode**.

Print:

```
  Step 4/5  Regulatory & Controls ......... ✓
```

Then immediately run Step 5.

---

### Step 5 — Security Requirements  `/sec-project-requirements`

Apply `/sec-project-requirements` skill instructions in **silent mode**.
After analysis, generate the `project-requirements.html` artifact.

Print:

```
  Step 5/5  Security Requirements ......... ✓  →  project-requirements.html
```

---

### Final Summary

Print:

```
─────────────────────────────────────────────
  Findings   Critical: N  High: N  Medium: N  Low: N
  Outputs    ✓ threat-modeling.html
             ✓ project-requirements.html
```

## Hard Rules

- Print ONLY the timeline lines and the final summary to the conversation. Nothing else.
- Do not print any analysis, findings, or intermediate results.
- Do not ask the user for confirmation between steps.
- The only exception: if `/sec-scope` needs to ask clarifying questions, those questions appear in the conversation. After the user answers, continue silently.
- Only two artifacts are produced: `threat-modeling.html` and `project-requirements.html`.
- This is an assessment pipeline — do not make go/no-go decisions.

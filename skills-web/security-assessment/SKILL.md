---
name: security-assessment
description: Starts the full security assessment pipeline. Collects project information, runs all analysis steps in sequence, and produces two HTML output documents.
---

# /security-assessment — Pipeline Orchestrator

## Purpose

Take the project information provided by the user and run the security assessment pipeline end-to-end.
Execute all steps in order, keep analysis results in conversation, and produce two HTML artifacts at the end.

**Ask the user only once at the start. The pipeline runs automatically after that.**

## Language Rule

Detect the language the user writes in and use that language for all responses, analysis output, and document content throughout the entire pipeline.

## Usage

```
/security-assessment
[project name and short description]
```

## Pipeline Flow

```
/sec-scope
      │
      ▼
/sec-threat-model ──→ threat-modeling.html
 ┌────┴──────────────────┐
 ▼                        ▼
/sec-owasp       /sec-regulatory
 │                        │
 │                   /sec-igrc
 │                        │
 └──────────┬─────────────┘
            ▼
/sec-project-requirements ──→ project-requirements.html
```

## Execution Instructions

### Step 0 — Project Information

If the user has not provided project information, ask in a single message:
1. Project name and one-sentence description
2. New development, existing system, or third-party product?
3. Regulated sector? (finance/banking, capital markets, other)

Once the information is received, start the pipeline. Do not ask for confirmation again.

---

### Step 1 — /sec-scope

Apply the `/sec-scope` skill instructions.
- Ask the 9-question intake in a single message
- Once all answers are clear, write the scope analysis to the conversation
- Move to the next step

---

### Step 2 — /sec-threat-model

Apply the `/sec-threat-model` skill instructions.
- Base the analysis on the /sec-scope output above in the conversation
- Write the STRIDE analysis to the conversation
- After the analysis, produce the `threat-modeling.html` artifact
- Move to the next step

---

### Step 3 — /sec-owasp + /sec-regulatory (parallel)

Run both in sequence under separate headings in the conversation:

**3a.** Apply `/sec-owasp` skill instructions → write OWASP findings to conversation
**3b.** Apply `/sec-regulatory` skill instructions → write regulatory analysis to conversation

---

### Step 4 — /sec-igrc

Apply the `/sec-igrc` skill instructions.
- Base the analysis on the /sec-scope and /sec-regulatory outputs above
- Write the internal control and RACI analysis to the conversation

---

### Step 5 — /sec-project-requirements

Apply the `/sec-project-requirements` skill instructions.
- Base the analysis on all previous outputs (scope, threat model, owasp, regulatory, igrc)
- Write the requirements to the conversation
- After the analysis, produce the `project-requirements.html` artifact

---

### Step 6 — Summary

When the pipeline is complete, write a short summary:

```
Security Assessment Complete
=============================

Project  : [project name]
Scope    : [environment, sector]

Findings :
  Critical : N
  High     : N
  Medium   : N
  Low      : N

Outputs  :
  ✓ threat-modeling.html
  ✓ project-requirements.html
```

## Hard Rules

- Ask the user only once at the start; do not ask for confirmation during the pipeline.
- Do not move to the next step before the current one is complete.
- Do not create any files — all analysis stays in the conversation.
- Only two artifacts are produced: `threat-modeling.html` and `project-requirements.html`.
- This is an assessment pipeline — do not make go/no-go decisions, only produce findings and requirements.
- Use the user's language throughout the entire pipeline.

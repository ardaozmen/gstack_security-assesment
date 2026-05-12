---
name: sec-igrc
description: Identifies internal control gaps and RACI ownership. Maps regulatory findings to the internal control framework.
---

# /sec-igrc — Internal Control & RACI Analysis

## Purpose

Identify ownership gaps and missing internal controls for security.
Base the analysis on the /sec-scope and /sec-regulatory outputs held in context.

## Language Rule

Use the same language the user is writing in for all output.

## Pipeline Mode

When called by `/security-assessment`: do NOT write the analysis to the conversation.
Hold all findings in context for subsequent steps.
The orchestrator prints the status line — this skill prints nothing.

## Execution Instructions

### Step 1 — Evaluate Control Domains

Assess the following 8 control domains:

| Domain | Topics to Evaluate |
|---|---|
| Access Management | Privileged access, least privilege principle, periodic access review |
| Change Management | CAB process, code review, test environment separation |
| Incident Management | Security incident process, escalation path, communication plan |
| Asset Management | Asset inventory currency, classification, ownership |
| Vendor Management | Third-party risk assessment, contract requirements |
| Logging & Monitoring | Centralized log management, alerting, log retention period |
| Business Continuity | DR plan, RTO/RPO targets, whether testing is performed |
| Security Awareness | Staff training, phishing simulation, policy acknowledgment |

### Step 2 — Build RACI Matrix

For each critical control, document the ownership status:

| Control | Responsible | Accountable | Consulted | Informed | Gap |
|---|---|---|---|---|---|
| Access review | [team or TBD] | [team or TBD] | | | [UNOWNED if no owner] |

### Step 3 — Write Analysis to Conversation

---

## /sec-igrc Analysis

### Control Assessment

| Domain | Status | Gap Description | Risk Level |
|---|---|---|---|
| Access Management | IN PLACE / PARTIAL / MISSING | [description] | CRITICAL / HIGH / MEDIUM / LOW |
| Change Management | | | |
| Incident Management | | | |
| Asset Management | | | |
| Vendor Management | | | |
| Logging & Monitoring | | | |
| Business Continuity | | | |
| Security Awareness | | | |

### RACI Matrix

| Control | Responsible | Accountable | Consulted | Informed | Gap |
|---|---|---|---|---|---|

### Critical Ownership Gaps
[List of critical controls with no owner]

### Regulatory Mapping
[Control requirements from /sec-regulatory findings that fall in this domain]

### Summary
| Status | Count |
|---|---|
| In Place | N |
| Partial | N |
| Missing | N |

---

## Hard Rules

- For any control with unknown ownership, write "UNOWNED" — not "TBD" — to make it visible.
- Do not read or write any files.
- Always link control gaps to the relevant /sec-regulatory findings.

---
name: sec-regulatory
description: Performs regulatory compliance analysis against BDDK, SPK, KVKK, and PCI-DSS frameworks. Documents gaps and remediation steps.
---

# /sec-regulatory — Regulatory Compliance Analysis

## Purpose

Assess the project's compliance with applicable regulatory frameworks.
Base the analysis on the /sec-scope output held in context — especially the sector and sensitive data categories.

## Language Rule

Use the same language the user is writing in for all output.

## Pipeline Mode

When called by `/security-assessment`: do NOT write the analysis to the conversation.
Hold all findings in context for subsequent steps.
The orchestrator prints the status line — this skill prints nothing.

## Execution Instructions

### Step 1 — Determine Applicable Frameworks

Based on the sector and data categories in the /sec-scope analysis, decide which frameworks apply:

| Framework | Applicable When |
|---|---|
| BDDK | Banking or payment services |
| SPK | Capital market activities |
| KVKK | Personal data processing in Turkey |
| PCI-DSS | Card data processing or storage |

Skip frameworks that do not apply and state the reason.

### Step 2 — Gap Analysis per Framework

For each applicable framework, evaluate the critical requirements:

**KVKK (if applicable)**
- Personal data inventory and classification
- Explicit consent mechanism
- Data retention and deletion procedures
- Data breach notification process (72-hour requirement)
- Technical and administrative safeguards
- Cross-border data transfer restrictions

**BDDK (if applicable)**
- Information systems management requirements
- Mandatory penetration testing
- Security incident management
- Third-party service provider controls
- Business continuity plan

**PCI-DSS (if applicable)**
- Card data encryption (P2PE/tokenization)
- Network segmentation
- Access control and log management
- Mandatory vulnerability scanning

**SPK (if applicable)**
- Information security policies
- Audit trail requirements
- Customer data protection

### Step 3 — Write Analysis to Conversation

---

## /sec-regulatory Analysis

### Applicable Frameworks
[Which frameworks were assessed, which were out of scope and why]

### Compliance Matrix

| Framework | Requirement | Status | Gap Description | Recommendation |
|---|---|---|---|---|
| KVKK | Data inventory | NON-COMPLIANT | [description] | [recommendation] |
| KVKK | 72-hour breach notification | PARTIAL | [description] | [recommendation] |
| BDDK | Pen test | COMPLIANT | — | — |

Status values: **COMPLIANT** / **PARTIAL** / **NON-COMPLIANT** / **UNABLE TO ASSESS**

### Gap Summary
| Framework | Compliant | Partial | Non-Compliant |
|---|---|---|---|
| KVKK | N | N | N |
| BDDK | N | N | N |
| PCI-DSS | N | N | N |

### Critical Findings
[Summary of NON-COMPLIANT items in priority order]

---

## Hard Rules

- Do not evaluate frameworks that are not applicable — explicitly state they are out of scope.
- Do not read or write any files.
- Write a concrete remediation step for every gap.

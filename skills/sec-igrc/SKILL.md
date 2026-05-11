---
name: sec-igrc
description: Integrated Governance, Risk and Compliance analysis. Identifies internal control gaps, maps control ownership, and produces a RACI matrix. Use after regulatory assessment to translate compliance findings into organizational accountability.
allowed-tools: Read, Write, Glob, Grep
---

# /sec-igrc — Integrated Governance, Risk & Compliance

## Purpose

Translate regulatory and technical findings into internal control accountability. This skill:

- Analyzes 5 control domains against project controls
- Identifies gaps (MISSING, PARTIAL, INEFFECTIVE)
- Assigns control owners and review cadences
- Produces a RACI matrix for every critical control

## Usage

```
/sec-igrc [--policy-docs <path>] [--refresh]
```

**Arguments**:
- `--policy-docs <path>`: Path to internal policy documents (if available)
- `--refresh`: Re-run even if `IGRC_FINDINGS.md` exists

**Triggers**: "iGRC analizi", "iç kontrol", "governance review", "RACI matrisi", "/sec-igrc"

## Prerequisites

- `SCOPE.md` required (Gate-SCOPE PASS)
- `REGULATORY_FINDINGS.md` recommended — enriches gap mapping
- Internal policy documents optional — request from user if not provided

## Execution Phases

### Phase 1 — Load Context

Read `SCOPE.md` and `REGULATORY_FINDINGS.md` (if exists).

Request internal policy documents from the user:
- Bilgi Güvenliği Politikası
- Erişim Yönetimi Prosedürü
- Değişiklik Yönetimi Prosedürü
- Olay Yönetimi Prosedürü
- Tedarikçi Yönetimi Politikası

If unavailable, mark each as `[ASSUMPTION-IGRC-xxx]: Policy document not provided — assessment based on common practice`.

### Phase 2 — Control Domain Analysis

Analyze each domain systematically:

**Domain 1: Erişim Kontrolü (Access Control)**
- Least privilege ilkesi uygulanıyor mu?
- Görev ayrılığı (segregation of duties) sağlanıyor mu?
- Ayrıcalıklı erişim periyodik olarak gözden geçiriliyor mu?
- Hesap yaşam döngüsü (onboarding/offboarding) yönetimi tanımlı mı?
- Servis hesapları ve API key'lerin sahipliği belli mi?

**Domain 2: Değişiklik Yönetimi (Change Management)**
- Değişiklik onay prosedürü (CAB, ticket, approval chain) var mı?
- Emergency change prosedürü tanımlı mı?
- Rollback planı her deploy için hazır mı?
- Change freeze dönemleri tanımlı mı (release öncesi, bayramlar)?
- Infrastructure-as-code değişiklikleri aynı prosese tabi mi?

**Domain 3: Olay Yönetimi (Incident Management)**
- Güvenlik olayı tanımı ve sınıflandırması yapılmış mı?
- Eskalasyon matrisi tanımlı mı?
- BDDK 72 saat bildirim prosedürü var mı (eğer uygulanabilirse)?
- Post-mortem / kök neden analizi prosedürü mevcut mu?
- Olay kayıtları (ticketing) tutulup arşivleniyor mu?

**Domain 4: Risk Yönetimi (Risk Management)**
- Proje başında risk değerlendirmesi yapılmış mı?
- Artık risk kabul süreci ve onay mekanizması tanımlı mı?
- Risk iştahı dokümante edilmiş mi?
- Periyodik risk gözden geçirme takvimi var mı?
- Risk sahipliği belirlenmiş mi?

**Domain 5: Tedarikçi Yönetimi (Vendor Management)**
- Tedarikçi güvenlik değerlendirmesi prosedürü var mı?
- Veri işleme anlaşması (DPA / KVKK Madde 12) imzalanmış mı?
- Tedarikçi erişim logları tutuluyor mu?
- Tedarikçi audit hakkı sözleşmede var mı?
- Kritik tedarikçi bağımlılıkları değerlendirilmiş mi?

### Phase 3 — Structure Each Gap

```yaml
- id: IGRC-001
  control_domain: "Erişim Kontrolü"
  control_name: "Ayrıcalıklı hesap gözden geçirme"
  policy_reference: "[policy doc and article, or 'Policy not available']"
  expected_control: "[what best practice or regulation requires]"
  current_state: "[what is actually in place or missing]"
  gap_type: MISSING | PARTIAL | INEFFECTIVE
  risk_implication: |
    [Business risk if this gap persists]
  remediation: |
    - [Specific action 1]
    - [Specific action 2]
  control_owner: "[team or role — do not leave blank; use 'TBD' only if unresolvable]"
  review_frequency: "Monthly | Quarterly | Annually | Per-change"
```

### Phase 4 — RACI Matrix

Build a RACI matrix for all critical controls (all MISSING or PARTIAL gaps plus key controls):

```markdown
| Control | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Access review | IAM Team | CISO | App Owner | Audit |
| Change approval | DevOps | Eng Manager | Security | CTO |
| Incident response | SecOps | CISO | Legal | Executive |
```

- **Responsible**: Does the work
- **Accountable**: Owns the outcome (single person)
- **Consulted**: Input required
- **Informed**: Notified of outcome

If `control_owner` cannot be determined, pause and ask: *"[Control adı] için sorumlu ekip kim olmalı?"*

## Quality Gate — Gate-IGRC

| Check | Required |
|---|---|
| All 5 control domains covered | PASS |
| At least 1 gap finding, or explicit "no gaps found" statement | PASS |
| RACI Responsible column filled for every critical control | PASS |
| Every gap has `gap_type` and at least 1 remediation action | PASS |
| Every gap has `control_owner` (TBD acceptable only with explanation) | PASS |
| `review_frequency` specified for each control | WARNING if absent |
| Unresolved `control_owner = TBD`: pause for user input | TASTE DECISION |

## Output Files

### `IGRC_FINDINGS.md`

```markdown
# iGRC Assessment

**Date**: [ISO date]
**Analyst**: SecOps Pipeline /sec-igrc

## Control Domain Summary

| Domain | Controls Assessed | MISSING | PARTIAL | INEFFECTIVE | COMPLIANT |
|---|---|---|---|---|---|

## Detailed Findings

### IGRC-001: [control_name]

- **Domain**: [domain]
- **Gap Type**: MISSING | PARTIAL | INEFFECTIVE
- **Expected**: [what should be in place]
- **Current State**: [what exists]
- **Risk**: [implication]
- **Remediation**:
  - [action 1]
- **Owner**: [team]
- **Review**: [frequency]

[repeat for each finding]

## Policy Document Status

| Policy | Status |
|---|---|
| Bilgi Güvenliği Politikası | Provided / Not provided [ASSUMPTION] |
```

### `RACI_MATRIX.md`

```markdown
# RACI Matrix — Security Controls

**Date**: [ISO date]

| Control | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
[full matrix]

## Ownership Notes

- [Any TBD items and their resolution status]
```

## Instructions for Claude

1. Read `SCOPE.md` and `REGULATORY_FINDINGS.md`. Request policy docs from user.
2. For each of the 5 control domains, answer all domain questions.
3. For every identified gap, fill all required fields. Do not leave `control_owner` blank.
4. If any `control_owner` is genuinely unknown, pause: *"[Control] için sorumlu ekip kim olmalı?"*
5. Build the RACI matrix for all critical and missing controls.
6. Write `IGRC_FINDINGS.md` and `RACI_MATRIX.md`.
7. Run Gate-IGRC checks.
8. Display console summary.

## Hard Rules

- Do not skip any of the 5 control domains.
- `control_owner` must never be blank — use "TBD" only when the user cannot provide it, and flag it as open.
- If RACI Responsible is unassigned for any critical control, gate cannot PASS.
- Do not conflate Responsible and Accountable in the RACI matrix.

## Console Summary

```
iGRC Assessment Complete
=========================

Control Domains Analyzed : 5
Policy Documents Provided : N / 5

Gaps Found:
  MISSING      : N
  PARTIAL      : N
  INEFFECTIVE  : N
  Total        : N

Unresolved Owners (TBD) : N
RACI Controls Mapped    : N

Gate-IGRC : PASS | WARNING | FAIL

Outputs:
  IGRC_FINDINGS.md
  RACI_MATRIX.md

Next Step:
  /sec-risk-report    (consolidates all findings)
```

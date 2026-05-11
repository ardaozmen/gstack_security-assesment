---
name: sec-regulatory
description: Assess compliance with Turkish financial sector regulations (BDDK, SPK, KVKK, PCI-DSS). Maps each regulatory article to project controls, identifies gaps, and produces a remediation roadmap. Use for regulated sector projects or when compliance posture must be formally documented.
allowed-tools: Read, Write, Glob, Grep
---

# /sec-regulatory — Regulatory Compliance Assessment

## Purpose

Conduct article-level compliance analysis against applicable Turkish financial regulations. This skill:

- Determines which regulations apply based on project sector and data types
- Maps each relevant article to current project controls
- Identifies NON_COMPLIANT and PARTIAL gaps with remediation steps
- Produces a compliance matrix and prioritized roadmap

## Usage

```
/sec-regulatory [--framework bddk|spk|kvkk|pci-dss|all] [--refresh]
```

**Arguments**:
- `--framework`: Limit to one regulation. Default: auto-detect from SCOPE.md
- `--refresh`: Re-run even if `REGULATORY_FINDINGS.md` exists

**Triggers**: "mevzuat denetimi", "BDDK uyum", "regulatory review", "SPK kontrolü", "KVKK analizi", "/sec-regulatory"

## Prerequisites

- `SCOPE.md` required (Gate-SCOPE PASS)
- `OWASP_FINDINGS.md` optional — enriches gap analysis if present

## Execution Phases

### Phase 1 — Applicable Regulation Detection

From `SCOPE.md`, determine which regulations apply:

| Condition | Regulation |
|---|---|
| Regulated sector = finans + BDDK-licensed entity | BDDK Bilgi Sistemleri Yönetmeliği (Mandatory) |
| Regulated sector = sermaye piyasası | SPK Bilgi Sistemleri Tebliği (Mandatory) |
| Personal data processed (PII, TC kimlik, health, financial) | KVKK (Mandatory) |
| Card data (PAN, CVV, track data) in scope | PCI-DSS (Mandatory) |

List applicable regulations and their legal basis in the output. If sector is ambiguous, include all and mark applicability as ASSUMED.

### Phase 2 — BDDK Bilgi Sistemleri Yönetmeliği

(Applies if BDDK-licensed. Skip with `[NOT_APPLICABLE]` note if not.)

**Sistem Güvenliği (Madde 9–14)**
- Erişim kontrolü politikası tanımlı ve uygulanıyor mu?
- Kimlik doğrulama gereksinimleri karşılanıyor mu?
- Ayrıcalıklı kullanıcı (admin) yönetimi mevcut mu?
- Sistem izleme ve loglama düzeni kurulu mu?

**Uygulama Güvenliği (Madde 15–18)**
- Güvenli yazılım geliştirme yaşam döngüsü uygulanıyor mu?
- Kaynak kod güvenlik testi (SAST/DAST) yapılıyor mu?
- Penetrasyon testi planlanmış mı?
- Yama yönetimi prosedürü var mı?

**Veri Güvenliği (Madde 19–22)**
- Hassas veriler at-rest ve in-transit şifreleniyor mu?
- Veri sınıflandırması yapılmış mı?
- Veri maskeleme uygulanıyor mu?
- Veri imha prosedürü tanımlı mı?

**İş Sürekliliği (Madde 23–28)**
- BCP/DRP planları mevcut mu?
- RTO/RPO hedefleri tanımlı mı?
- Felaket kurtarma tatbikatı yapılıyor mu?
- Kritik sistemler için yedeklilik sağlanmış mı?

**Denetim İzi (Madde 29–32)**
- Log saklama süresi minimum 5 yıl mı?
- Log bütünlüğü korunuyor mu (tamper-evident)?
- Denetim izi silinemez ve değiştirilemez mi?

**Dış Hizmet Alımı (Madde 33–38)**
- Üçüncü taraf tedarikçi güvenlik değerlendirmesi yapılmış mı?
- SLA güvenlik gereksinimleri içeriyor mu?
- Tedarikçi erişimi izleniyor mu?

### Phase 3 — SPK Bilgi Sistemleri Tebliği

(Applies if capital markets license. Skip with `[NOT_APPLICABLE]` if not.)

Cover equivalent domains: system security, application security, data security, business continuity, audit trail, outsourcing. Reference SPK tebliği article numbers.

### Phase 4 — KVKK

(Applies if any personal data is processed.)

- Veri işleme amacı ve hukuki dayanağı tanımlı mı?
- Açık rıza mekanizması uygulanmış mı (gerekliyse)?
- Veri sorumlusu ve işleyenler belirlenmiş mi?
- İlgili kişi hakları mekanizması (erişim, silme, taşınabilirlik) var mı?
- Veri ihlali bildirim prosedürü mevcut mu (72 saat kuralı)?
- VERBİS kaydı yapılmış mı?
- Yurt dışı veri transferi koşulları karşılanıyor mu?

### Phase 5 — PCI-DSS

(Applies if card data is in scope. Skip with `[NOT_APPLICABLE]` if not.)

Cover PCI-DSS v4.0 requirements grouped by:
- Req 1–2: Network security controls
- Req 3–4: Protect account data
- Req 5–6: Vulnerability management
- Req 7–8: Access control
- Req 9: Physical security
- Req 10–11: Monitoring and testing
- Req 12: Information security policy

### Phase 6 — Structure Each Finding

```yaml
- id: REG-BDDK-001
  regulation: "BDDK Bilgi Sistemleri Yönetmeliği"
  article: "Madde 15 — Uygulama Güvenliği"
  requirement: "Yazılım geliştirme sürecinde güvenlik testleri yapılmalıdır"
  current_status: COMPLIANT | PARTIAL | NON_COMPLIANT | UNKNOWN
  gap_description: |
    [What is missing or insufficient]
  remediation: |
    - [Specific action 1]
    - [Specific action 2]
  priority: CRITICAL | HIGH | MEDIUM | LOW
  legal_risk: |
    [Regulatory sanction risk if not remediated]
```

## Quality Gate — Gate-REG

| Check | Required |
|---|---|
| Applicable regulation list present with justification | PASS |
| All applicable articles covered (or marked UNKNOWN with reason) | PASS |
| Compliance summary matrix present | PASS |
| Every NON_COMPLIANT finding has a remediation step | PASS |
| BDDK log retention (5 yıl) addressed if applicable | PASS |
| If NON_COMPLIANT + CRITICAL: taste decision — blocker? | TASTE DECISION |
| UNKNOWN article count ≥ 3: taste decision — involve legal? | TASTE DECISION |

## Output File — `REGULATORY_FINDINGS.md`

```markdown
# Regulatory Compliance Assessment

**Applicable Regulations**: [list]
**Date**: [ISO date]
**Analyst**: SecOps Pipeline /sec-regulatory

## Compliance Summary Matrix

| Regulation | Article | Requirement | Status | Priority |
|---|---|---|---|---|
| BDDK | Madde 15 | Güvenlik testi | NON_COMPLIANT | CRITICAL |

## Detailed Findings

### REG-BDDK-001: [title]

- **Regulation**: BDDK Bilgi Sistemleri Yönetmeliği
- **Article**: Madde 15
- **Status**: NON_COMPLIANT
- **Gap**: [description]
- **Remediation**:
  - [action 1]
  - [action 2]
- **Legal Risk**: [sanction description]
- **Priority**: CRITICAL

[repeat for each finding]

## Non-Compliance Risk Summary

| Risk | Regulation | Potential Sanction |
|---|---|---|

## Remediation Roadmap

### Priority CRITICAL (go-live blocker)
- [ ] [REG-BDDK-001] [action] — Owner: [team]

### Priority HIGH (30 days post go-live)
- [ ] ...

### Priority MEDIUM (90 days)
- [ ] ...
```

## Instructions for Claude

1. Read `SCOPE.md`. Determine applicable regulations from sector and data types.
2. If `OWASP_FINDINGS.md` exists, cross-reference for relevant gaps (especially A09 for logging).
3. Work through each applicable regulation phase by phase.
4. Structure each gap as a finding with all required fields.
5. If NON_COMPLIANT + CRITICAL finding: ask *"Bu mevzuat ihlali go-live blocker sayılsın mı?"*
6. If UNKNOWN count ≥ 3: ask *"Hukuk birimi devreye alınsın mı?"*
7. Write `REGULATORY_FINDINGS.md` using the template.
8. Run Gate-REG checks.
9. Display console summary.

## Hard Rules

- Reference specific article numbers — never write "generally applicable" without an article.
- Do not mark a regulation as NOT_APPLICABLE without a written reason in the output.
- Every NON_COMPLIANT finding must have at least one concrete remediation action.
- BDDK projects: log retention < 5 years is always NON_COMPLIANT, never PARTIAL.

## Console Summary

```
Regulatory Compliance Assessment Complete
==========================================

Applicable Regulations:
  BDDK Bilgi Sistemleri Yönetmeliği : [yes/no]
  SPK Bilgi Sistemleri Tebliği      : [yes/no]
  KVKK                               : [yes/no]
  PCI-DSS                            : [yes/no]

Findings:
  COMPLIANT     : N
  PARTIAL       : N
  NON_COMPLIANT : N
  UNKNOWN       : N

Critical Non-Compliances : N
Legal Risk Items         : N

Gate-REG : PASS | WARNING | FAIL

Output : REGULATORY_FINDINGS.md

Next Step:
  /sec-igrc     (internal controls — depends on this output)
```

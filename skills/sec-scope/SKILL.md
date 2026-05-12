---
name: sec-scope
description: Define project security scope — asset inventory, data flows, trust boundaries, and sensitive data classification. First mandatory step in every security assessment. Use when starting a new evaluation, mapping system components, or when scope is unclear.
allowed-tools: Read, Write, Glob, Grep
---

# /sec-scope — Scope Definition

## Purpose

Establish the security assessment boundary before any analysis begins. This skill:

- Collects project context and environment details
- Builds a complete asset inventory (apps, data stores, integrations, infra)
- Maps data flows and encryption posture
- Defines trust boundaries and external-facing surfaces
- Records assumptions and missing information as BLOCKER or WARNING

No other skill may run until this one produces a valid `SCOPE.md`.

## Usage

```
/sec-scope [--refresh] [--focus <component>]
```

**Arguments**:
- `--refresh`: Re-collect scope even if `SCOPE.md` already exists
- `--focus <component>`: Scope a single component (e.g. `--focus payment-service`)

**Triggers**: "projeyi değerlendir", "güvenlik analizi başlat", "kapsam belirle", "yeni proje var", "/sec-scope"

## Prerequisites

None. This is pipeline Step 1.

## Execution Phases

### Phase 1 — Structured Project Intake

Ask all 9 questions below in a single message. Do not proceed to Phase 2 until all answers are clear.
If any answer is ambiguous or contradictory, ask only the specific follow-up needed — do not restart the whole intake.

```
Projeyi değerlendirmek için aşağıdaki 9 soruyu yanıtlar mısınız?

1. Bu yeni bir uygulama mı, yoksa mevcut bir sistemin değerlendirmesi mi?
   (yeni geliştirme / mevcut sistem entegrasyonu / üçüncü taraf ürün)

2. Altyapı yeni mi kuruluyor, yoksa mevcut/paylaşılan altyapı mı kullanılacak?
   (yeni altyapı / mevcut/paylaşılan altyapı / belirsiz)

3. Sistemi kimler kullanacak?
   (iç kullanıcılar / kurumsal müşteriler / bireysel/tüketici müşteriler / API tüketicileri / karışık)

4. Sistem internete açık mı olacak?
   (evet — doğrudan / evet — CDN/WAF arkasında / hayır — yalnızca iç ağ / belirsiz)

5. Hizmet herhangi bir public cloud hizmeti kullanıyor mu?
   (evet — hangisi: AWS/Azure/GCP/diğer / hayır — on-premise / hibrit / belirsiz)

6. Kullanıcı kimlik doğrulaması gerekiyor mu?
   (evet — hangi yöntem: SSO/OAuth/LDAP/custom / hayır — herkese açık / belirsiz)

7. Sistemi kim geliştiriyor?
   (iç ekip / dış/outsource geliştirici / SaaS/hazır ürün / karışık)

8. Üçüncü taraf entegrasyonlar var mı?
   (evet — lütfen listeleyin: ödeme sistemi / kimlik sağlayıcı / SMS/e-posta / harici API / diğer)
   (hayır)

9. Sistem gizli veya hassas veri işleyecek mi?
   (evet — tür: TC kimlik no / finansal kayıtlar / sağlık verisi / kimlik bilgileri / diğer KVK verisi)
   (hayır — kişisel veri işlenmeyecek)
```

**Rule**: Do not produce `SCOPE.md` until all 9 questions have a clear, unambiguous answer.
If the user's response leaves any answer unclear, ask only the specific follow-up question(s) needed before continuing.

### Phase 2 — Asset Inventory

For each category, list all known components. Mark unknown as `[ASSUMPTION]`.

| Category | Examples |
|---|---|
| Applications & Services | frontend, backend API, worker, scheduler, mobile app |
| Data Stores | relational DB, NoSQL, file system, cache, message queue |
| External Integrations | payment gateway, identity provider, SMS/email service, third-party API |
| Infrastructure | CDN, load balancer, WAF, API gateway, container orchestration |
| Sensitive Data Categories | TC kimlik no, financial records, health data, credentials, PII |

### Phase 3 — Data Flow Mapping

Answer for the system:

1. What data enters the system? What leaves?
2. Is data encrypted in transit? (TLS version, certificate management)
3. What is stored persistently vs. transiently?
4. Does logging capture sensitive fields?
5. What data is shared with third parties?

### Phase 4 — Trust Boundaries

Identify and name each boundary crossing:

1. Internet ↔ DMZ boundary
2. DMZ ↔ Internal network boundary
3. Service-to-service authentication method
4. Admin / operational interface location and access control
5. External integrations: which are inbound, which are outbound

### Phase 5 — Assumption & Gap Registry

For every unanswered question, record:

```
[ASSUMPTION-001]: <description> — <basis for assumption>
[MISSING-001]: <description> — BLOCKER | WARNING
```

**BLOCKER**: scope cannot proceed without this information.
**WARNING**: assessment can continue but coverage is reduced.

If `MISSING` count ≥ 3, pause and ask user for confirmation before proceeding.

## Quality Gate — Gate-SCOPE

| Check | Required |
|---|---|
| At least 1 application or service listed | PASS |
| Sensitive data section filled or explicitly `YOK` | PASS |
| At least 1 trust boundary defined | PASS |
| External integrations filled or explicitly `YOK` | PASS |
| All BLOCKER missing-info items resolved | PASS |
| Data flow summary present | WARNING if absent |
| Go-live date specified | WARNING if absent |

Gate FAIL → pipeline stops. Generate question list for user. Suggest `/sec-scope --refresh`.

## Output File — `SCOPE.md`

```markdown
# Project Scope Document

**Project**: [name]
**Date**: [ISO date]
**Analyst**: SecOps Pipeline /sec-scope
**Version**: 1.0

## Project Overview

[2-sentence summary: what it does, who uses it, environment]

## Asset Inventory

### Applications & Services
| Name | Type | Technology | Externally Accessible |
|---|---|---|---|
| [name] | [backend/frontend/api/worker] | [stack] | yes/no |

### Data Stores
| Name | Type | Contains PII | Encrypted at Rest |
|---|---|---|---|

### External Integrations
| Name | Direction | Data Shared | Auth Method |
|---|---|---|---|

### Sensitive Data Categories
- [KVKK/GDPR category]: [description]
- YOK (if none)

## Data Flow Summary

[Narrative: what enters, what leaves, how it moves, where it persists]

## Trust Boundaries

| Boundary | From | To | Auth Method | Logged |
|---|---|---|---|---|

## Key Assumptions
- [ASSUMPTION-001]: [description] — [basis]

## Missing Information
- [MISSING-001]: [description] — BLOCKER | WARNING

## Scope Sign-off

- [ ] Scope sufficient — `/sec-threat-model` may run
- [ ] Critical gap present — pipeline BLOCKED
```

## Instructions for Claude

1. Ask all 9 Phase 1 intake questions in a single message.
2. Wait for all 9 answers. If any answer is ambiguous, ask only the specific clarifying question — do not restart.
3. Do not proceed to Phase 2 until all 9 intake questions are clearly answered.
4. Based on responses, populate Phase 2–4. For any unknown field, insert `[ASSUMPTION-xxx]`.
5. After drafting, list all MISSING items. If any are BLOCKER, stop and ask the user.
6. If MISSING count ≥ 3, ask: *"Kritik eksiklere rağmen devam etmeli miyiz? (E/H + gerekçe)"*
7. Write `SCOPE.md` using the template above.
8. Run Gate-SCOPE checks.
9. If gate PASS or WARNING-only: display console summary and suggest `/sec-threat-model`.
10. If gate FAIL: display what is missing and suggest `/sec-scope --refresh`.

## Hard Rules

- Do not start `/sec-threat-model` or any downstream skill before Gate-SCOPE PASS.
- Do not invent asset names or data categories — mark as ASSUMPTION.
- Do not leave "External Integrations" blank — write `YOK` if none exist.
- Do not mark gate PASS if any BLOCKER missing-info item is unresolved.

## Console Summary

```
Scope Definition Complete
=========================

Project : [name]
Environment : [cloud/on-prem/hybrid]
Sector : [finans/sağlık/...]

Asset Inventory:
  Applications   : N
  Data Stores    : N
  Integrations   : N

Sensitive Data Categories : N
Trust Boundaries          : N
Assumptions               : N
Missing Info (BLOCKER)    : N
Missing Info (WARNING)    : N

Gate-SCOPE : PASS | WARNING | FAIL

Output : SCOPE.md

Next Step:
  /sec-threat-model
```

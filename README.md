# Security Assessment Pipeline

Kurumsal güvenlik değerlendirmelerini standart ve tekrarlanabilir biçimde yürütmek için tasarlanmış modüler SecOps framework.

## Pipeline Akışı

```
         /sec-scope
               │
               ▼
       /sec-threat-model
        ┌──────┴──────────────────┐
        ▼                         ▼
   /sec-owasp            /sec-regulatory
        │                         │
        │                    /sec-igrc
        │                         │
        └──────────┬──────────────┘
                   ▼
          /sec-risk-report
                   │
                   ▼
            /sec-signoff
```

`/sec-owasp` ve `/sec-regulatory` bağımsız olduğundan paralel çalışabilir.
`/sec-igrc` ise `/sec-regulatory` çıktısına bağlıdır.

## Orchestrator

- **Contract:** `pipeline/orchestrator-contract.md`
- **Modlar:** `pipeline/modes.md`
- **Quality Gates:** `pipeline/quality-gates.md`
- **Manifest:** `pipeline/orchestrator.manifest.yaml`
- **State Dosyaları:** `AUTO_PLAN_STATUS.md`, `PIPELINE_CONTEXT.md`

Hızlı başlatma: `/sec-autoplan`

## Skills

| Komut | Output | Bağımlılık |
|---|---|---|
| `/sec-scope` | `SCOPE.md` | — |
| `/sec-threat-model` | `THREAT_MODEL.md` | `/sec-scope` |
| `/sec-owasp` | `OWASP_FINDINGS.md` | `/sec-scope`, `/sec-threat-model` |
| `/sec-regulatory` | `REGULATORY_FINDINGS.md` | `/sec-scope` |
| `/sec-igrc` | `IGRC_FINDINGS.md`, `RACI_MATRIX.md` | `/sec-scope`, `/sec-regulatory` |
| `/sec-risk-report` | `RISK_REPORT.md`, `RISK_REGISTER.csv` | tüm öncekiler |
| `/sec-signoff` | `SIGNOFF_PACKAGE.md` | `/sec-risk-report` |
| `/sec-autoplan` | `AUTO_PLAN_STATUS.md`, `PIPELINE_CONTEXT.md` | orkestratör |

Detay: `skills/skill-catalog.md` · Spec şeması: `skills/spec-schema.yaml`

## Roller

| Rol | Sorumlu Skill |
|---|---|
| Security Orchestrator | `/sec-autoplan` |
| Senior Security Analyst | `/sec-scope` |
| Threat Modeler | `/sec-threat-model` |
| AppSec Engineer | `/sec-owasp` |
| Compliance Officer | `/sec-regulatory` |
| iGRC Analyst | `/sec-igrc` |
| Risk Officer | `/sec-risk-report` |
| Security Review Board | `/sec-signoff` |

Detay: `roles/role-catalog.md`

## Pipeline Modları

| Mod | Adımlar |
|---|---|
| `full` | `/sec-scope` → `/sec-threat-model` → `/sec-owasp` ‖ `/sec-regulatory` → `/sec-igrc` → `/sec-risk-report` → `/sec-signoff` |
| `fast` | `/sec-scope` → `/sec-owasp` → `/sec-risk-report` |
| `compliance` | `/sec-scope` → `/sec-regulatory` → `/sec-igrc` → `/sec-risk-report` → `/sec-signoff` |
| `resume` | Son FAIL adımından devam |

## Çalıştırma

```bash
streamlit run ui/app.py
```

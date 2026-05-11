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
     /sec-project-requirements
                   │
                   ▼
            /sec-signoff

     (pipeline bittikten sonra, opsiyonel)
            /sec-retro
```

`/sec-owasp` ve `/sec-regulatory` bağımsız olduğundan paralel çalışabilir.
`/sec-igrc` `/sec-regulatory` çıktısına bağlıdır.
`/sec-retro` pipeline dışında, projeler arası öğrenme için çalışır.

## Orchestrator

- **Contract:** `pipeline/orchestrator-contract.md`
- **Modlar:** `pipeline/modes.md`
- **Quality Gates:** `pipeline/quality-gates.md`
- **Manifest:** `pipeline/orchestrator.manifest.yaml`
- **State Dosyaları:** `AUTO_PLAN_STATUS.md`, `PIPELINE_CONTEXT.md`

Hızlı başlatma: `/sec-autoplan`

## Skills

| Komut | Output | Bağımlılık | Gate |
|---|---|---|---|
| `/sec-scope` | `SCOPE.md` | — | Gate-SCOPE |
| `/sec-threat-model` | `THREAT_MODEL.md` | `/sec-scope` | Gate-THREAT |
| `/sec-owasp` | `OWASP_FINDINGS.md` | `/sec-scope`, `/sec-threat-model` | Gate-OWASP |
| `/sec-regulatory` | `REGULATORY_FINDINGS.md` | `/sec-scope` | Gate-REG |
| `/sec-igrc` | `IGRC_FINDINGS.md`, `RACI_MATRIX.md` | `/sec-scope`, `/sec-regulatory` | Gate-IGRC |
| `/sec-project-requirements` | `PROJECT_REQUIREMENTS.md` | tüm assessment çıktıları | Gate-REQ |
| `/sec-signoff` | `SIGNOFF_PACKAGE.md` | `/sec-project-requirements` | Gate-SIGNOFF |
| `/sec-autoplan` | `AUTO_PLAN_STATUS.md`, `PIPELINE_CONTEXT.md` | orkestratör | — |
| `/sec-retro` *(opsiyonel)* | `RETRO_REPORT.md`, `learnings.md` | pipeline tamamlandı | Gate-RETRO |

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
| Security Requirements Owner | `/sec-project-requirements` |
| Security Review Board | `/sec-signoff` |
| Security Learning Engineer | `/sec-retro` |

Detay: `roles/role-catalog.md`

## Pipeline Modları

| Mod | Adımlar |
|---|---|
| `full` | `/sec-scope` → `/sec-threat-model` → `/sec-owasp` ‖ `/sec-regulatory` → `/sec-igrc` → `/sec-project-requirements` → `/sec-signoff` |
| `fast` | `/sec-scope` → `/sec-owasp` → `/sec-project-requirements` |
| `compliance` | `/sec-scope` → `/sec-regulatory` → `/sec-igrc` → `/sec-project-requirements` → `/sec-signoff` |
| `resume` | Son FAIL adımından devam |

## Çalıştırma

```bash
streamlit run ui/app.py
```

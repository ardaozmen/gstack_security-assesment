# Skill Catalog

Detayli class-based skill spec'leri: `<skill-name>/SKILL.md`
Generic schema: `spec-schema.yaml`

## /sec-scope
- Role: Senior Security Analyst
- Input: Kullanıcıdan proje bağlamı
- Output: `SCOPE.md`
- Amaç: Kapsam, varlik envanteri, trust boundary
- Gate: `Gate-SCOPE`
- Depends on: —

## /sec-threat-model
- Role: Threat Modeler
- Input: `SCOPE.md`
- Output: `THREAT_MODEL.md`
- Amaç: STRIDE tehdit matrisi ve attack tree
- Gate: `Gate-THREAT`
- Depends on: `/sec-scope`

## /sec-owasp *(paralel)*
- Role: AppSec Engineer
- Input: `SCOPE.md`, `THREAT_MODEL.md` (opsiyonel)
- Output: `OWASP_FINDINGS.md`
- Amaç: OWASP Top 10 bazli bulgu seti
- Gate: `Gate-OWASP`
- Depends on: `/sec-scope`, `/sec-threat-model`

## /sec-regulatory *(paralel)*
- Role: Compliance Officer
- Input: `SCOPE.md`
- Output: `REGULATORY_FINDINGS.md`
- Amaç: BDDK/SPK/KVKK/PCI-DSS uyum analizi
- Gate: `Gate-REG`
- Depends on: `/sec-scope`

## /sec-igrc
- Role: iGRC Analyst
- Input: `SCOPE.md`, `REGULATORY_FINDINGS.md` (önerilir)
- Output: `IGRC_FINDINGS.md`, `RACI_MATRIX.md`
- Amaç: Ic kontrol ve sahiplik bosluk analizi
- Gate: `Gate-IGRC`
- Depends on: `/sec-scope`, `/sec-regulatory`

## /sec-project-requirements
- Role: Security Requirements Owner
- Input: `THREAT_MODEL.md`, `OWASP_FINDINGS.md`, `REGULATORY_FINDINGS.md`, `IGRC_FINDINGS.md`
- Output: `PROJECT_REQUIREMENTS.md`
- Amaç: Tüm bulguları öncelikli güvenlik gereksinimlerine dönüştürmek
- Gate: `Gate-REQ`
- Depends on: `/sec-threat-model`, `/sec-owasp`, `/sec-regulatory`, `/sec-igrc`

## /sec-signoff
- Role: Security Review Board
- Input: `PROJECT_REQUIREMENTS.md`
- Output: `SIGNOFF_PACKAGE.md`
- Amaç: Go-live karar hazırlığı (öneri)
- Gate: `Gate-SIGNOFF`
- Depends on: `/sec-project-requirements`

## /sec-autoplan
- Role: Security Orchestrator
- Input: Mode + opsiyonel onceki ciktilar
- Output: `AUTO_PLAN_STATUS.md`, `PIPELINE_CONTEXT.md`
- Amaç: Tum pipeline'i tek komutla yonetmek
- Depends on: —

## /sec-retro *(opsiyonel, pipeline sonrası)*
- Role: Security Learning Engineer
- Input: Pipeline çıktıları + `~/.security-assessments/learnings.md`
- Output: `.assessments/RETRO_REPORT.md`, `~/.security-assessments/learnings.md`
- Amaç: Projeler arası öğrenme ve geçmişle karşılaştırma
- Gate: `Gate-RETRO`
- Depends on: `/sec-signoff` (tamamlanmış pipeline)

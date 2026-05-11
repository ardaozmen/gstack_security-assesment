# Skill Catalog

Detayli class-based skill spec'leri: `specs/*.spec.md`
Generic schema: `spec-schema.yaml`

## /sec-scope
- Role: Senior Security Analyst
- Input: Proje ozeti
- Output: `SCOPE.md`
- Amaç: Kapsam, varlik envanteri, trust boundary
- Gate: `Gate-SCOPE`

## /sec-threat-model
- Role: Threat Modeler
- Input: `SCOPE.md`
- Output: `THREAT_MODEL.md`
- Amaç: STRIDE tehdit matrisi ve attack tree
- Gate: `Gate-THREAT`
- Depends on: `/sec-scope`

## /sec-owasp *(paralel)*
- Role: AppSec Engineer
- Input: `SCOPE.md`, `THREAT_MODEL.md`
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
- Input: `SCOPE.md`, `REGULATORY_FINDINGS.md`
- Output: `IGRC_FINDINGS.md`, `RACI_MATRIX.md`
- Amaç: Ic kontrol ve sahiplik bosluk analizi
- Gate: `Gate-IGRC`
- Depends on: `/sec-scope`, `/sec-regulatory`

## /sec-risk-report
- Role: Risk Officer
- Input: Tum onceki ciktilar
- Output: `RISK_REPORT.md`, `RISK_REGISTER.csv`
- Amaç: Konsolide risk skorlama ve aksiyon plani
- Gate: `Gate-RISK`

## /sec-signoff
- Role: Security Review Board
- Input: `RISK_REPORT.md`
- Output: `SIGNOFF_PACKAGE.md`
- Amaç: Go-live karar hazirligi (oneri)
- Gate: `Gate-SIGNOFF`
- Depends on: `/sec-risk-report`

## /sec-autoplan
- Role: Security Orchestrator
- Input: Mode + opsiyonel onceki ciktilar
- Output: `AUTO_PLAN_STATUS.md`, `PIPELINE_CONTEXT.md`
- Amaç: Tum pipeline'i tek komutla yonetmek

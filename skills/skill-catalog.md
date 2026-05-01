# Skill Catalog

Detayli class-based skill spec'leri: `specs/*.spec.md`
Generic schema: `spec-schema.yaml`

## 1) /sec-scope
- Role: Senior Security Analyst
- Input: Proje ozeti
- Output: `SCOPE.md`
- Amaç: Kapsam, varlik envanteri, trust boundary

## 2) /sec-threat-model
- Role: Threat Modeler
- Input: `SCOPE.md`
- Output: `THREAT_MODEL.md`
- Amaç: STRIDE tehdit matrisi ve attack tree

## 3) /sec-owasp
- Role: AppSec Engineer
- Input: `SCOPE.md`, `THREAT_MODEL.md`
- Output: `OWASP_FINDINGS.md`
- Amaç: OWASP Top 10 bazli bulgu seti

## 4) /sec-regulatory
- Role: Compliance Officer
- Input: `SCOPE.md`, `OWASP_FINDINGS.md`
- Output: `REGULATORY_FINDINGS.md`
- Amaç: BDDK/SPK/KVKK/PCI-DSS uyum analizi

## 5) /sec-igrc
- Role: iGRC Analyst
- Input: `SCOPE.md`, `REGULATORY_FINDINGS.md`
- Output: `IGRC_FINDINGS.md`, `RACI_MATRIX.md`
- Amaç: Ic kontrol ve sahiplik bosluk analizi

## 6) /sec-risk-report
- Role: Risk Officer
- Input: Tum onceki ciktilar
- Output: `RISK_REPORT.md`, `RISK_REGISTER.csv`
- Amaç: Konsolide risk skorlama ve aksiyon plani

## 7) /sec-signoff
- Role: Security Review Board
- Input: `RISK_REPORT.md`
- Output: `SIGNOFF_PACKAGE.md`
- Amaç: Go-live karar hazirligi (oneri)

## 8) /sec-autoplan
- Role: Security Orchestrator
- Input: Mode + opsiyonel onceki ciktilar
- Output: `AUTO_PLAN_STATUS.md`, `PIPELINE_CONTEXT.md`
- Amaç: Tum pipeline'i tek komutla yonetmek


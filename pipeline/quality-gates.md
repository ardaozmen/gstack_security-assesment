# Quality Gates

Bu dosya tum gate kurallarini tek yerde toplar.

## Gate-SCOPE — `/sec-scope`
- Output: `SCOPE.md`
- PASS icin: asset inventory, trust boundary, external integrations zorunlu
- WARNING: veri akisi veya go-live tarihi eksik olabilir

## Gate-THREAT — `/sec-threat-model`
- Output: `THREAT_MODEL.md`
- PASS icin: STRIDE kapsami, attack tree, severity ozeti zorunlu

## Gate-OWASP — `/sec-owasp`
- Output: `OWASP_FINDINGS.md`
- PASS icin: A01-A10 kapsami ve bulgu alanlari zorunlu

## Gate-REG — `/sec-regulatory`
- Output: `REGULATORY_FINDINGS.md`
- PASS icin: mevzuat-esleme, matrix, remediation zorunlu

## Gate-IGRC — `/sec-igrc`
- Output: `IGRC_FINDINGS.md`, `RACI_MATRIX.md`
- PASS icin: control owner ve gap remediation zorunlu

## Gate-RISK — `/sec-risk-report`
- Output: `RISK_REPORT.md`, `RISK_REGISTER.csv`
- PASS icin: risk skorlama, aksiyon listesi, security posture zorunlu

## Gate-SIGNOFF — `/sec-signoff`
- Output: `SIGNOFF_PACKAGE.md`
- PASS icin: GO/NO_GO/CONDITIONAL_GO ve approvals zorunlu

## Fail Policy

Bir gate FAIL ise:
1. Pipeline durur
2. Neden `AUTO_PLAN_STATUS.md`'ye yazilir
3. Sonraki komut onerisi uretilir (`/sec-autoplan resume`)

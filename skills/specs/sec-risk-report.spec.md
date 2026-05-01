# SkillSpec: sec-risk-report

- `skill_id`: `sec-risk-report`
- `command`: `/sec-risk-report`
- `class_name`: `RiskConsolidationSkill`
- `version`: `1.0.0`
- `role`: `Risk Officer`
- `purpose`: Tum bulgulari konsolide edip risk skoru ve aksiyon plani uretmek.

## Inputs
- `SCOPE.md`
- `THREAT_MODEL.md`
- `OWASP_FINDINGS.md`
- `REGULATORY_FINDINGS.md`
- `IGRC_FINDINGS.md`

## Outputs
- `RISK_REPORT.md`
- `RISK_REGISTER.csv`

## Dependencies
- `sec-scope`
- `sec-threat-model` (mode'a bagli)
- `sec-owasp` (mode'a bagli)
- `sec-regulatory` (mode'a bagli)
- `sec-igrc` (mode'a bagli)

## Execution
1. Bulgulari normalize et
2. Skorlari hesapla
3. Onceliklendirilmis aksiyonlari yaz

## Quality Gate
- Executive summary var
- Her riskte skor var
- Priority 0/1/2 aksiyon listesi var

## Taste Decisions
- Blocker yoksa go-live onayi sorusu
- Finansal etki tahmini dahil etme karari

## Failure Policy
- FAIL: eksik alanlar tamamlanmadan signoff'a gecme


# SkillSpec: sec-owasp

- `skill_id`: `sec-owasp`
- `command`: `/sec-owasp`
- `class_name`: `OwaspAssessmentSkill`
- `version`: `1.0.0`
- `role`: `AppSec Engineer`
- `purpose`: OWASP Top 10 bulgu seti uretmek.

## Inputs
- `SCOPE.md`
- `THREAT_MODEL.md` (opsiyonel ama onerilir)

## Outputs
- `OWASP_FINDINGS.md`

## Dependencies
- `sec-scope`
- `sec-threat-model` (onerilir)

## Execution
1. A01-A10 kapsamini denetle
2. Bulgu bazli exploit senaryolari uret
3. Severity ve confidence ata

## Quality Gate
- A01-A10 kapsanmis
- Bulgu alanlari tam (`risk_title`, `severity`, `exploit_scenario`, `confidence`)
- Top 3 kritik risk veya "kritik risk yok"

## Taste Decisions
- `CRITICAL >= 3` ise devam onayi
- LOW confidence kritik bulgular icin ek veri karari

## Failure Policy
- FAIL: report revizyonu zorunlu
- WARNING: final rapora yansit


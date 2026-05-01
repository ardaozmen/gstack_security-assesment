# SkillSpec: sec-igrc

- `skill_id`: `sec-igrc`
- `command`: `/sec-igrc`
- `class_name`: `IGRCAssessmentSkill`
- `version`: `1.0.0`
- `role`: `iGRC Analyst`
- `purpose`: Ic kontrol bosluklarini ve kontrol sahipligini netlestirmek.

## Inputs
- `SCOPE.md`
- `REGULATORY_FINDINGS.md` (onerilir)

## Outputs
- `IGRC_FINDINGS.md`
- `RACI_MATRIX.md`

## Dependencies
- `sec-scope`
- `sec-regulatory` (onerilir)

## Execution
1. Kontrol alanlarini tara
2. Gap ve sahiplikleri kaydet
3. RACI matrisi olustur

## Quality Gate
- En az bir gap veya "gap yok" notu
- RACI Responsible kolonlari dolu
- `control_owner` alanlari dolu

## Taste Decisions
- Owner belirsiz kayitlar icin ekip onayi

## Failure Policy
- FAIL: owner atamasi tamamlanmadan devam etme


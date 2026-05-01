# SkillSpec: sec-signoff

- `skill_id`: `sec-signoff`
- `command`: `/sec-signoff`
- `class_name`: `SignoffPreparationSkill`
- `version`: `1.0.0`
- `role`: `Security Review Board`
- `purpose`: GO/NO_GO/CONDITIONAL_GO oneri paketi hazirlamak.

## Inputs
- `RISK_REPORT.md`

## Outputs
- `SIGNOFF_PACKAGE.md`

## Dependencies
- `sec-risk-report`

## Execution
1. Blocker ve acik riskleri topla
2. Gerekli onaylari esle
3. Karar onerisi ve gerekce yaz

## Quality Gate
- Karar onerisi mevcut
- Rationale (min 2 cumle) mevcut
- Required approvals ve post-go-live listesi mevcut

## Taste Decisions
- NO_GO durumunda conditional kosullarini netlestirme
- Kritik regulatory + conditional durumunda hukuk bildirimi

## Failure Policy
- FAIL: insan onayi olmadan sonuc "nihai karar" gibi sunulamaz


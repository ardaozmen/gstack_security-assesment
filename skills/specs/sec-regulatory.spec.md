# SkillSpec: sec-regulatory

- `skill_id`: `sec-regulatory`
- `command`: `/sec-regulatory`
- `class_name`: `RegulatoryAssessmentSkill`
- `version`: `1.0.0`
- `role`: `Compliance Officer`
- `purpose`: BDDK/SPK/KVKK/PCI-DSS uyum bosluklarini cikarmak.

## Inputs
- `SCOPE.md`
- `OWASP_FINDINGS.md` (onerilir)

## Outputs
- `REGULATORY_FINDINGS.md`

## Dependencies
- `sec-scope`

## Execution
1. Uygulanabilir mevzuati belirle
2. Madde bazli esleme yap
3. Non-compliant gap ve remediation uret

## Quality Gate
- Mevzuat listesi + gerekce mevcut
- Compliance matrix mevcut
- Non-compliant bulgularin remediation'i dolu

## Taste Decisions
- Kritik non-compliant bulgu blocker olsun mu?
- Unknown madde sayisi yuksekse hukuk devreye alma karari

## Failure Policy
- FAIL: compliance raporu yeniden uretilir


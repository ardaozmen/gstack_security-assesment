# SkillSpec: sec-threat-model

- `skill_id`: `sec-threat-model`
- `command`: `/sec-threat-model`
- `class_name`: `ThreatModelSkill`
- `version`: `1.0.0`
- `role`: `Threat Modeler`
- `purpose`: STRIDE temelli tehdit modeli ve attack tree uretmek.

## Inputs
- `SCOPE.md`

## Outputs
- `THREAT_MODEL.md`

## Dependencies
- `sec-scope`

## Execution
1. SCOPE yukle
2. Bilesen bazli STRIDE uygula
3. Trust boundary saldiri yollarini cikar
4. Attack tree olustur

## Quality Gate
- STRIDE kapsami tam
- Attack tree mevcut
- Severity dagilimi mevcut

## Taste Decisions
- Yuksek karmasik attack tree icin derinlesme sorusu

## Failure Policy
- Gate FAIL: step tekrar calistirilmadan ilerlenmez


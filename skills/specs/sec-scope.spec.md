# SkillSpec: sec-scope

- `skill_id`: `sec-scope`
- `command`: `/sec-scope`
- `class_name`: `ScopeSkill`
- `version`: `1.0.0`
- `role`: `Senior Security Analyst`
- `purpose`: Proje kapsamini, varlik envanterini, veri akislarini ve trust boundary'leri netlestirmek.

## Inputs
- Proje ozeti
- Ortam bilgisi
- Entegrasyon listesi

## Outputs
- `SCOPE.md`

## Dependencies
- None (pipeline step 1)

## Execution
1. Proje baglami topla
2. Asset inventory cikar
3. Veri akisi ve trust boundary olustur
4. Missing info ve varsayimlari kaydet

## Quality Gate
- Asset inventory dolu
- Sensitive data bos degil veya `YOK`
- Trust boundary en az bir kayit

## Taste Decisions
- `MISSING_INFO >= 3` ise kullanici onayi al

## Failure Policy
- Gate FAIL: pipeline durur, soru listesi uret
- Warning: kaydet, devam et


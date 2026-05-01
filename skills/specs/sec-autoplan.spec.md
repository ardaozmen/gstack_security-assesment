# SkillSpec: sec-autoplan

- `skill_id`: `sec-autoplan`
- `command`: `/sec-autoplan`
- `class_name`: `SecurityOrchestratorSkill`
- `version`: `1.0.0`
- `role`: `Security Orchestrator`
- `purpose`: Tum pipeline akisini mode, gate ve retry kurallariyla yonetmek.

## Inputs
- Mode parametreleri (`full|fast|compliance|resume`)
- Opsiyonel onceki ciktilar
- Opsiyonel `AUTO_PLAN_STATUS.md`

## Outputs
- `AUTO_PLAN_STATUS.md`
- `PIPELINE_CONTEXT.md`

## Dependencies
- Orchestration root (step scheduler)

## Execution
1. Modu ayriştir
2. Step planini cikar
3. Her adim sonunda gate calistir
4. Taste decision varsa durup sor
5. Durum/context dosyalarini guncelle

## Quality Gate
- Orchestrator sira kurali korunmus
- Step durumlari tutarli
- Fail/warning karar kayitlari mevcut

## Taste Decisions
- Gate'lerden gelen tum insan-onayi sorulari

## Failure Policy
- FAIL: pipeline durdur + resume komutu oner
- WARNING: kaydet, devam et


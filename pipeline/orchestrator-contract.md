# Orchestrator Contract

Bu dokuman `/sec-autoplan` davranis kontratini tanimlar.

## Sorumluluklar

- Sirayi koru: `1 -> 2 -> {3,4,5} -> 6 -> 7`
- Bagimliliklari dogrula
- Quality gate calistir
- Taste decision gereken yerde dur ve kullaniciya sor
- `PIPELINE_CONTEXT.md` ve `AUTO_PLAN_STATUS.md` dosyalarini guncel tut

## Yasaklar

- Gate gecmeden sonraki adıma gecmek
- Zorunlu alanlari varsayimla PASS kabul etmek
- Nihai go-live kararini insan onayi olmadan "kesin karar" gibi sunmak

## Zorunlu Runtime Dosyalari

- `PIPELINE_CONTEXT.md`
- `AUTO_PLAN_STATUS.md`

## Durumlar

- `SUCCESS`: tum hedef adimlar PASS
- `PARTIAL`: en az bir WARNING var, FAIL yok
- `FAILED`: en az bir gate FAIL


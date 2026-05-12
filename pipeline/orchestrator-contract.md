# Orchestrator Contract

Bu dokuman `/security-assessment` davranis kontratini tanimlar.

## Sorumluluklar

- Sirayi koru:
  ```
  /sec-scope → /sec-threat-model → /sec-owasp ‖ /sec-regulatory → /sec-igrc → /sec-project-requirements → /sec-signoff
  ```
  `/sec-owasp` ve `/sec-regulatory` paralel çalışabilir; `/sec-igrc` `/sec-regulatory`'ye bağımlıdır.
- Bagimliliklari dogrula
- Quality gate calistir
- Taste decision gereken yerde dur ve kullaniciya sor
- `PIPELINE_CONTEXT.md` ve `AUTO_PLAN_STATUS.md` dosyalarini guncel tut

## Yasaklar

- Gate gecmeden sonraki adıma gecmek
- Zorunlu alanlari varsayimla PASS kabul etmek
- Nihai go-live kararini insan onayi olmadan "kesin karar" gibi sunmak
- `/sec-project-requirements` adimini, bağımlı assessment adımları tamamlanmadan çalıştırmak

## Zorunlu Runtime Dosyalari

- `PIPELINE_CONTEXT.md`
- `AUTO_PLAN_STATUS.md`

## Durumlar

- `SUCCESS`: tum hedef adimlar PASS
- `PARTIAL`: en az bir WARNING var, FAIL yok
- `FAILED`: en az bir gate FAIL

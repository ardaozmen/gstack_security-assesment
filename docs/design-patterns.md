# Design Patterns

Bu pipeline asagidaki pattern'lerle modellenmistir:

## 1. Pipeline Pattern
Adimlarin sabit bir sirada calistigi akistir.
- Fayda: izlenebilirlik, tekrar edilebilirlik, kontrol

## 2. Chain of Responsibility
Her skill kendi sorumluluk alanini isler ve ciktiyi bir sonraki asamaya aktarir.
- Fayda: gevsek baglilik, parca parca iyilestirme

## 3. State Machine
Orchestrator durumu: `SUCCESS`, `PARTIAL`, `FAILED`.
- Fayda: resume/retry semantigi netlesir

## 4. Command Pattern
`/sec-*` komutlari tekil operasyonlardir.
- Fayda: otomasyon, script ile tetikleme, audit izi

## 5. Gatekeeper Pattern
Her adim bir quality gate ile korunur.
- Fayda: dusuk kaliteli cikti zincire yayilmaz

## 6. Human-in-the-loop
Taste decision noktalarinda insan onayi zorunludur.
- Fayda: kritik muğlak kararlarin denetlenmesi


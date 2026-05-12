---
name: security-assessment
description: Tam güvenlik değerlendirme pipeline'ını başlatır. Proje bilgisini alır, tüm analiz adımlarını sırayla çalıştırır ve sonunda iki HTML doküman üretir.
---

# /security-assessment — Pipeline Orchestrator

## Amaç

Kullanıcının verdiği proje bilgisini alarak güvenlik değerlendirme pipeline'ını uçtan uca çalıştır.
Tüm adımları sırayla çalıştır, analiz sonuçlarını conversation'da tut, sonunda iki HTML artifact üret.

**Kullanıcıdan yalnızca başta bilgi al. Sonrasında pipeline otomatik ilerler.**

## Kullanım

```
/security-assessment
[proje adı ve kısa açıklama]
```

## Pipeline Akışı

```
/sec-scope
      │
      ▼
/sec-threat-model ──→ threat-modeling.html
 ┌────┴──────────────────┐
 ▼                        ▼
/sec-owasp       /sec-regulatory
 │                        │
 │                   /sec-igrc
 │                        │
 └──────────┬─────────────┘
            ▼
/sec-project-requirements ──→ project-requirements.html
```

## Çalıştırma Talimatları

### Adım 0 — Proje Bilgisi

Kullanıcı proje bilgisini vermemişse tek mesajda sor:
1. Proje adı ve tek cümle açıklama
2. Yeni geliştirme mi, mevcut sistem mi, üçüncü taraf ürün mü?
3. Düzenlenmiş sektör? (finans/BDDK, sermaye piyasası/SPK, diğer)

Bilgi geldikten sonra pipeline'ı başlat. Bir daha soru sorma.

---

### Adım 1 — /sec-scope

`/sec-scope` skill talimatlarını uygula.
- 9 soruluk intake'i tek mesajda sor
- Tüm cevaplar netleşince kapsam analizini conversation'a yaz
- Bir sonraki adıma geç

---

### Adım 2 — /sec-threat-model

`/sec-threat-model` skill talimatlarını uygula.
- Yukarıdaki /sec-scope analizini baz al
- STRIDE analizini conversation'a yaz
- Analiz bittikten sonra `threat-modeling.html` artifact'ı üret
- Bir sonraki adıma geç

---

### Adım 3 — /sec-owasp + /sec-regulatory (paralel)

Her ikisini de sırayla çalıştır (conversation'da ayrı başlıklar altında):

**3a.** `/sec-owasp` skill talimatlarını uygula → OWASP bulgularını conversation'a yaz
**3b.** `/sec-regulatory` skill talimatlarını uygula → Mevzuat analizini conversation'a yaz

---

### Adım 4 — /sec-igrc

`/sec-igrc` skill talimatlarını uygula.
- Yukarıdaki /sec-scope ve /sec-regulatory analizlerini baz al
- İç kontrol ve RACI analizini conversation'a yaz

---

### Adım 5 — /sec-project-requirements

`/sec-project-requirements` skill talimatlarını uygula.
- Yukarıdaki tüm analizleri (scope, threat model, owasp, regulatory, igrc) baz al
- Gereksinimleri conversation'a yaz
- Analiz bittikten sonra `project-requirements.html` artifact'ı üret

---

### Adım 6 — Özet

Pipeline tamamlandığında kısa bir özet yaz:

```
Güvenlik Değerlendirmesi Tamamlandı
=====================================

Proje     : [proje adı]
Kapsam    : [ortam, sektör]

Bulgular  :
  Kritik  : N
  Yüksek  : N
  Orta    : N
  Düşük   : N

Çıktılar  :
  ✓ threat-modeling.html
  ✓ project-requirements.html
```

## Hard Rules

- Kullanıcıya yalnızca başta bir kez soru sor; pipeline boyunca onay isteme.
- Her adım tamamlanmadan bir sonrakine geçme.
- Hiçbir adımda dosya oluşturma — tüm analiz conversation'da kalır.
- Sadece iki artifact üretilir: `threat-modeling.html` ve `project-requirements.html`.
- Bu bir değerlendirme pipeline'ı — go/no-go kararı verme, sadece bulgular ve gereksinimler üret.

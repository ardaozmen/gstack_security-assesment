---
name: sec-project-requirements
description: Tüm değerlendirme bulgularını konsolide ederek öncelikli güvenlik gereksinimlerine dönüştürür. Sonunda project-requirements.html artifact'ı oluşturur.
---

# /sec-project-requirements — Güvenlik Gereksinimleri

## Amaç

Conversation'daki tüm analiz çıktılarını (scope, threat model, OWASP, regulatory, igrc) tek bir öncelikli gereksinimler belgesine dönüştür.
Bu bir değerlendirme belgesidir — karar mekanizması değil.

## Çalıştırma Talimatları

### Adım 1 — Tüm Bulguları Topla

Conversation'daki şu analizlerden bulguları çek:
- /sec-threat-model → tehdit ve saldırı senaryoları
- /sec-owasp → uygulama güvenlik açıkları
- /sec-regulatory → mevzuat uyumsuzlukları
- /sec-igrc → kontrol ve sahiplik boşlukları

Birleşik bulgu listesi oluştur. Aynı kök nedene işaret eden bulguları birleştir.

### Adım 2 — Risk Skorlama

Her bulgu için: **Risk = Olasılık (1-5) × Etki (1-5)**

| Skor | Seviye |
|---|---|
| 20-25 | KRİTİK |
| 12-19 | YÜKSEK |
| 6-11 | ORTA |
| 1-5 | DÜŞÜK |

### Adım 3 — Gereksinimlere Dönüştür

Her bulgu için karşılık gelen bir güvenlik gereksinimi yaz:

```
SEC-REQ-001
Başlık     : [ne yapılmalı]
Kaynak     : [OWASP-A01-001, THREAT-003]
Gereksinim : [ne uygulanmalı — açık ve ölçülebilir]
Kabul Krit.:
  - [kriter 1]
  - [kriter 2]
Risk Skoru : [N] — [KRİTİK/YÜKSEK/ORTA/DÜŞÜK]
Öncelik    : [1-KRİTİK / 2-YÜKSEK / 3-ORTA]
Sahip      : [ekip veya TBD]
```

### Adım 4 — Güvenlik Postür Değerlendirmesi

| Postür | Koşul |
|---|---|
| KIRMIZI | KRİTİK seviyede çözümsüz bulgu var |
| SARI | YÜKSEK bulgular var, KRİTİK yok |
| YEŞİL | Yalnızca ORTA ve DÜŞÜK bulgular var |

2-3 cümle gerekçe yaz.

### Adım 5 — Yönetici Özeti

Teknik olmayan okuyucu için:
1. Projenin ne yaptığı (2 cümle)
2. Hangi değerlendirmeler yapıldı
3. En önemli 3 güvenlik gereksinimi (sade dille)
4. Genel güvenlik postürü

### Adım 6 — Conversation'a Yaz

---

## /sec-project-requirements Analizi

### Yönetici Özeti

**Güvenlik Postürü: KIRMIZI / SARI / YEŞİL**

[2-3 cümle gerekçe]

**Bu Proje Ne Yapıyor?**
[2 cümle]

**En Önemli 3 Gereksinim**
1. [SEC-REQ-xxx] — [sade açıklama]
2. [SEC-REQ-xxx] — [sade açıklama]
3. [SEC-REQ-xxx] — [sade açıklama]

---

### Kritik Gereksinimler (Risk: 20-25)

[Her gereksinim için yukarıdaki format]

---

### Yüksek Gereksinimler (Risk: 12-19)

[Her gereksinim için yukarıdaki format]

---

### Orta Gereksinimler (Risk: 6-11)

[Her gereksinim için yukarıdaki format]

---

### Gereksinimler Özet Tablosu

| ID | Başlık | Kaynak | Risk Skoru | Seviye | Sahip |
|---|---|---|---|---|---|

### Değerlendirme Kapsamı
| Skill | Durum |
|---|---|
| /sec-threat-model | yüklendi / eksik |
| /sec-owasp | yüklendi / eksik |
| /sec-regulatory | yüklendi / eksik |
| /sec-igrc | yüklendi / eksik |

---

### Adım 7 — project-requirements.html Artifact

Analiz tamamlandıktan sonra `project-requirements.html` adında bir HTML artifact oluştur.

`skills-web/word-output-standard.md` dosyasındaki `## project-requirements.html` şablonunu ve paylaşılan CSS'i kullan.
Tüm placeholder'ları gerçek analiz içeriğiyle doldur.
Template comment'lerini kaldır.
Satır class'larını (`critical`, `high`, `medium`) gerçek risk seviyelerine göre uygula.
Postür class'ını (`posture-red`, `posture-amber`, `posture-green`) sonuca göre uygula.

## Hard Rules

- Dosya okuma veya yazma yapma — tüm girdi conversation'dan gelir.
- Her bulgu en az bir gereksinim üretmeli.
- Sahip bilinmiyorsa "TBD" yaz ve işaretle.
- GO / NO-GO / BLOCKER gibi karar dili kullanma — bu bir değerlendirme belgesidir.
- Kapsam dışı değerlendirmeleri açıkça belirt.

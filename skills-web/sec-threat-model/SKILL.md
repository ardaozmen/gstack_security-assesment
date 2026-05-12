---
name: sec-threat-model
description: STRIDE metodolojisiyle tehdit modeli oluşturur. Bileşen-tehdit matrisi, güven sınırı ihlalleri ve saldırı ağaçlarını üretir. Sonunda threat-modeling.html artifact'ı oluşturur.
---

# /sec-threat-model — Tehdit Modelleme

## Amaç

STRIDE çerçevesiyle her sistem bileşenine karşı tehditleri sistematik olarak belirle.
Conversation'daki /sec-scope analizini baz al — dosya okuma.

## Çalıştırma Talimatları

### Adım 1 — Bileşen-Tehdit Matrisi

Yukarıdaki /sec-scope analizindeki her varlık için STRIDE uygula:

| Varlık Türü | S | T | R | I | D | E |
|---|---|---|---|---|---|---|
| Dış Kaynak (External Entity) | ✓ | | ✓ | | | |
| Servis / Process | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Veri Deposu | | ✓ | ✓ | ✓ | ✓ | |
| Veri Akışı | | ✓ | | ✓ | ✓ | |
| Auth Bileşeni | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Her hücre için:
- **Spoofing**: Kimlik sahteciliği mümkün mü?
- **Tampering**: Girdi doğrulaması var mı, yazma işlemleri korumalı mı?
- **Repudiation**: Kritik aksiyonlar denetim izi ile loglanıyor mu?
- **Info Disclosure**: Hata mesajları iç detay sızdırıyor mu?
- **Denial of Service**: Rate limiting var mı, kaynak tüketimi tetiklenebilir mi?
- **Elevation of Privilege**: Her katmanda yetkilendirme kontrol ediliyor mu?

### Adım 2 — Veri Akışı Tehdit Analizi

/sec-scope'daki her veri akışı için:
1. TLS 1.2+ ile şifreli mi?
2. MITM saldırısı mümkün mü?
3. İstek tekrar oynatılabilir mi?
4. Hangi katmanda doğrulanıyor?
5. Bu akış ele geçirilirse etki alanı ne kadar geniş?

### Adım 3 — Güven Sınırı Analizi

Her güven sınırı geçişi için:
1. Kim veya ne geçebilir?
2. Auth mekanizması nedir?
3. Yetkilendirme kararı nerede alınıyor?
4. Her geçiş loglanıyor mu?
5. Sınır bypass edilirse ne olur?

### Adım 4 — Risk Skorlama

Her tehdit için: **Risk = Olasılık (1-5) × Etki (1-5)**

| Skor | Seviye |
|---|---|
| 20-25 | KRİTİK |
| 12-19 | YÜKSEK |
| 6-11 | ORTA |
| 1-5 | DÜŞÜK |

### Adım 5 — Saldırı Ağaçları

Risk skoru ≥ 12 olan her tehdit için saldırı ağacı oluştur.

```
Hedef: [yetkisiz erişim]
├── Yol A: [kimlik doğrulama bypass]
│   ├── A1: [SQL enjeksiyon] — zorluk: orta
│   └── A2: [kaba kuvvet]     — zorluk: düşük
└── Yol B: [meşru işlevsellik kötüye kullanımı]
    └── B1: [IDOR]             — zorluk: düşük
```

### Adım 6 — Analizi Yaz

Aşağıdaki yapıda conversation'a yaz:

---

## /sec-threat-model Analizi

### Bileşen Tehdit Matrisi
| Varlık | Spoofing | Tampering | Repudiation | Info Disclosure | DoS | EoP |
|---|---|---|---|---|---|---|
| [varlık] | [bulgu veya YOK] | ... | | | | |

### Veri Akışı Tehditleri
| Akış | Tehdit | Kategori | Seviye | Açıklama |
|---|---|---|---|---|

### Güven Sınırı İhlalleri
**[Sınır Adı]**
- Senaryo: [açıklama]
- Seviye: KRİTİK / YÜKSEK / ORTA / DÜŞÜK
- Saldırı yolu: [özet]

### Saldırı Ağaçları
[Her ağaç]

### Tehdit Özeti
| Seviye | Adet |
|---|---|
| KRİTİK | N |
| YÜKSEK | N |
| ORTA | N |
| DÜŞÜK | N |
| **Toplam** | **N** |

---

### Adım 7 — threat-modeling.html Artifact

Analiz tamamlandıktan sonra `threat-modeling.html` adında bir HTML artifact oluştur.

`skills-web/word-output-standard.md` dosyasındaki `## threat-modeling.html` şablonunu ve paylaşılan CSS'i kullan.
Tüm placeholder'ları gerçek analiz içeriğiyle doldur.
Template comment'lerini kaldır.
Satır class'larını (`critical`, `high`, `medium`, `low`) gerçek tehdit seviyelerine göre uygula.

## Hard Rules

- Dosya okuma veya yazma yapma — tüm girdi conversation'dan gelir.
- Hiçbir STRIDE kategorisini atlama — geçerli değilse "YOK — [gerekçe]" yaz.
- Saldırı ağacı olmadan analizi bitirme.
- KRİTİK her tehdit için saldırı ağacı zorunlu.

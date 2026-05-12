---
name: sec-regulatory
description: BDDK, SPK, KVKK ve PCI-DSS çerçevelerinde mevzuat uyum analizi yapar. Gap'leri ve remediation adımlarını belgeler.
---

# /sec-regulatory — Mevzuat Uyum Analizi

## Amaç

Projenin ilgili mevzuat çerçevelerine uyumunu değerlendir.
Conversation'daki /sec-scope analizini baz al — özellikle sektör ve hassas veri kategorilerini.

## Çalıştırma Talimatları

### Adım 1 — Geçerli Mevzuatı Belirle

/sec-scope analizindeki sektör ve veri kategorilerine göre hangi çerçevelerin geçerli olduğuna karar ver:

| Çerçeve | Geçerlilik Koşulu |
|---|---|
| BDDK | Bankacılık veya ödeme hizmetleri |
| SPK | Sermaye piyasası faaliyetleri |
| KVKK | Türkiye'de kişisel veri işleme |
| PCI-DSS | Kart verisi işleme veya saklama |

Geçerli olmayan çerçeveleri atla ve gerekçesini belirt.

### Adım 2 — Her Çerçeve İçin Gap Analizi

Geçerli her çerçeve için kritik maddeleri değerlendir:

**KVKK (geçerliyse)**
- Kişisel veri envanteri ve sınıflandırması
- Açık rıza mekanizması
- Veri saklama ve silme prosedürleri
- Veri ihlali bildirim süreci (72 saat)
- Teknik ve idari tedbirler
- Yurt dışı veri transferi kısıtlamaları

**BDDK (geçerliyse)**
- Bilgi sistemleri yönetimi gereksinimleri
- Penetrasyon testi zorunluluğu
- Güvenlik olay yönetimi
- Dış hizmet sağlayıcı kontrolü
- İş sürekliliği planı

**PCI-DSS (geçerliyse)**
- Kart verisi şifreleme (P2PE/tokenizasyon)
- Ağ segmentasyonu
- Erişim kontrolü ve log yönetimi
- Güvenlik açığı tarama zorunluluğu

**SPK (geçerliyse)**
- Bilgi güvenliği politikaları
- Denetim izi gereksinimleri
- Müşteri veri koruma

### Adım 3 — Analizi Yaz

---

## /sec-regulatory Analizi

### Geçerli Mevzuat
[Hangi çerçeveler değerlendirildi, hangiler kapsam dışı ve neden]

### Uyum Matrisi

| Çerçeve | Madde | Durum | Gap Açıklaması | Öneri |
|---|---|---|---|---|
| KVKK | Veri envanteri | UYUMSUZ | [açıklama] | [öneri] |
| KVKK | 72 saat ihlal bildirimi | KISMİ | [açıklama] | [öneri] |
| BDDK | Pen test | UYUMLU | — | — |
| ... | | | | |

Durum değerleri: **UYUMLU** / **KISMİ** / **UYUMSUZ** / **DEĞERLENDİRİLEMEDİ**

### Gap Özeti
| Çerçeve | Uyumlu | Kısmi | Uyumsuz |
|---|---|---|---|
| KVKK | N | N | N |
| BDDK | N | N | N |
| PCI-DSS | N | N | N |

### Kritik Bulgular
[UYUMSUZ maddelerin özeti ve öncelik sırası]

---

## Hard Rules

- Geçerli olmayan çerçeveleri değerlendirme — kapsam dışı olduğunu açıkça belirt.
- Dosya okuma veya yazma yapma.
- Her gap için somut remediation adımı yaz.

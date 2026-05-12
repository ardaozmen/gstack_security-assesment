---
name: sec-igrc
description: İç kontrol boşluklarını ve RACI sahipliğini tanımlar. Mevzuat bulgularını iç kontrol çerçevesiyle ilişkilendirir.
---

# /sec-igrc — İç Kontrol ve RACI Analizi

## Amaç

Güvenlik kontrollerindeki sahiplik boşluklarını ve iç kontrol eksiklerini belirle.
Conversation'daki /sec-scope ve /sec-regulatory analizlerini baz al.

## Çalıştırma Talimatları

### Adım 1 — Kontrol Alanlarını Değerlendir

Aşağıdaki 8 kontrol alanı için değerlendirme yap:

| Alan | Değerlendirilecek Konular |
|---|---|
| Erişim Yönetimi | Ayrıcalıklı erişim, en az yetki prensibi, periyodik erişim gözden geçirme |
| Değişiklik Yönetimi | CAB süreci, kod inceleme, test ortamı ayrımı |
| Olay Yönetimi | Güvenlik olay süreci, eskalasyon yolu, iletişim planı |
| Varlık Yönetimi | Varlık envanteri güncelliği, sınıflandırma, sahiplik |
| Tedarikçi Yönetimi | Üçüncü taraf risk değerlendirme, sözleşme gereksinimleri |
| Log ve İzleme | Merkezi log yönetimi, alert mekanizmaları, log saklama süresi |
| İş Sürekliliği | DR planı, RTO/RPO hedefleri, test yapılıyor mu |
| Güvenlik Farkındalığı | Personel eğitimi, phishing simulasyonu, politika kabul |

### Adım 2 — RACI Matrisi Oluştur

Her kritik kontrol için sahiplik durumunu belgele:

| Kontrol | Sorumlu | Onaylayan | Danışılan | Bilgilendirilen | Boşluk |
|---|---|---|---|---|---|
| Erişim gözden geçirme | [ekip veya TBD] | [ekip veya TBD] | | | [sahip yoksa: SAHİPSİZ] |

### Adım 3 — Analizi Yaz

---

## /sec-igrc Analizi

### Kontrol Değerlendirmesi

| Alan | Durum | Boşluk Açıklaması | Risk Seviyesi |
|---|---|---|---|
| Erişim Yönetimi | MEVCUT / KISMİ / EKSİK | [açıklama] | KRİTİK / YÜKSEK / ORTA / DÜŞÜK |
| Değişiklik Yönetimi | | | |
| Olay Yönetimi | | | |
| Varlık Yönetimi | | | |
| Tedarikçi Yönetimi | | | |
| Log ve İzleme | | | |
| İş Sürekliliği | | | |
| Güvenlik Farkındalığı | | | |

### RACI Matrisi

| Kontrol | Sorumlu | Onaylayan | Danışılan | Bilgilendirilen | Boşluk |
|---|---|---|---|---|---|

### Kritik Sahiplik Boşlukları
[Sahibi olmayan kritik kontrollerin listesi]

### Mevzuat Bağlantısı
[/sec-regulatory bulgularından bu alanda düşen kontrol gereksinimleri]

### Özet
| Durum | Adet |
|---|---|
| Mevcut | N |
| Kısmi | N |
| Eksik | N |

---

## Hard Rules

- Sahipliği bilinmeyen her kontrol için "TBD" değil "SAHİPSİZ" yaz — görünür olsun.
- Dosya okuma veya yazma yapma.
- /sec-regulatory bulgularıyla çakışan kontrol boşluklarını mutlaka ilişkilendir.

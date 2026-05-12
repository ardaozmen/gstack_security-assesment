---
name: sec-scope
description: Proje güvenlik kapsamını tanımlar. Varlık envanteri, veri akışları ve güven sınırlarını belirler. Pipeline'ın ilk zorunlu adımı.
---

# /sec-scope — Kapsam Tanımı

## Amaç

Projenin güvenlik değerlendirme sınırını belirle. Bu adımda:

- Proje bağlamını ve ortamını anla
- Varlık envanterini çıkar (uygulamalar, veri depoları, entegrasyonlar, altyapı)
- Veri akışlarını ve şifreleme durumunu belgele
- Güven sınırlarını ve dışa açık yüzeyleri tanımla

## Çalıştırma Talimatları

### Adım 1 — 9 Soruluk Intake

Aşağıdaki 9 soruyu tek mesajda sor. Cevaplar gelmeden analizi başlatma.
Herhangi bir cevap belirsizse yalnızca o soruya özel clarification iste.

```
Projeyi değerlendirmek için aşağıdaki 9 soruyu yanıtlar mısınız?

1. Bu yeni bir uygulama mı, yoksa mevcut bir sistemin değerlendirmesi mi?
   (yeni geliştirme / mevcut sistem entegrasyonu / üçüncü taraf ürün)

2. Altyapı yeni mi kuruluyor, yoksa mevcut/paylaşılan altyapı mı kullanılacak?
   (yeni altyapı / mevcut-paylaşılan altyapı / belirsiz)

3. Sistemi kimler kullanacak?
   (iç kullanıcılar / kurumsal müşteriler / bireysel müşteriler / API tüketicileri / karışık)

4. Sistem internete açık mı olacak?
   (evet — doğrudan / evet — CDN/WAF arkasında / hayır — yalnızca iç ağ / belirsiz)

5. Hizmet herhangi bir public cloud hizmeti kullanıyor mu?
   (evet — AWS / Azure / GCP / diğer / hayır — on-premise / hibrit / belirsiz)

6. Kullanıcı kimlik doğrulaması gerekiyor mu?
   (evet — SSO / OAuth / LDAP / custom / hayır / belirsiz)

7. Sistemi kim geliştiriyor?
   (iç ekip / dış-outsource geliştirici / SaaS-hazır ürün / karışık)

8. Üçüncü taraf entegrasyonlar var mı?
   (evet — ödeme sistemi / kimlik sağlayıcı / SMS-e-posta / harici API / diğer)
   (hayır)

9. Sistem gizli veya hassas veri işleyecek mi?
   (evet — TC kimlik no / finansal kayıtlar / sağlık verisi / kimlik bilgileri / diğer KVK verisi)
   (hayır)
```

### Adım 2 — Kapsam Analizini Yaz

Tüm cevaplar geldikten sonra aşağıdaki yapıda analizi conversation'a yaz:

---

## /sec-scope Analizi

### Proje Özeti
[2 cümle: ne yapıyor, kim kullanıyor, hangi ortamda]

### Varlık Envanteri

**Uygulamalar ve Servisler**
| Ad | Tür | Teknoloji | Dışa Açık |
|---|---|---|---|
| [ad] | [backend/frontend/api/worker] | [stack] | evet/hayır |

**Veri Depoları**
| Ad | Tür | KVK Verisi İçeriyor | Şifreli |
|---|---|---|---|

**Dış Entegrasyonlar**
| Ad | Yön | Paylaşılan Veri | Auth Yöntemi |
|---|---|---|---|

**Hassas Veri Kategorileri**
- [kategori]: [açıklama]
- YOK (varsa)

### Veri Akışı Özeti
[Sisteme giren, çıkan, nasıl hareket ettiği, nerede depolandığı]

### Güven Sınırları
| Sınır | Kimden | Kime | Auth | Log'lanıyor |
|---|---|---|---|---|

### Varsayımlar ve Eksikler
- [VARSAYIM-001]: [açıklama]
- [EKSİK-001]: [açıklama] — UYARI

---

Analiz tamamlandı. Bir sonraki adım: /sec-threat-model

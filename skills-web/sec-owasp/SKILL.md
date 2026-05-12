---
name: sec-owasp
description: OWASP Top 10 çerçevesiyle uygulama güvenlik bulgularını üretir. Her kategori için exploit senaryosu ve teknik gereksinimler yazar.
---

# /sec-owasp — OWASP Top 10 Analizi

## Amaç

Uygulamanın OWASP Top 10 açıklarına karşı durumunu değerlendir.
Conversation'daki /sec-scope ve /sec-threat-model analizlerini baz al.

## Çalıştırma Talimatları

### Adım 1 — Her OWASP Kategorisini Değerlendir

Aşağıdaki 10 kategoriyi sırayla değerlendir. Her biri için:
- Uygulanabilir mi? (projeye özgü bağlamda)
- Mevcut veya potansiyel bulgu var mı?
- Risk skoru: Olasılık (1-5) × Etki (1-5)
- Exploit senaryosu (kısa, somut)
- Teknik öneri

| ID | Kategori |
|---|---|
| A01 | Broken Access Control |
| A02 | Cryptographic Failures |
| A03 | Injection |
| A04 | Insecure Design |
| A05 | Security Misconfiguration |
| A06 | Vulnerable and Outdated Components |
| A07 | Identification and Authentication Failures |
| A08 | Software and Data Integrity Failures |
| A09 | Security Logging and Monitoring Failures |
| A10 | Server-Side Request Forgery (SSRF) |

### Adım 2 — Analizi Yaz

---

## /sec-owasp Analizi

### Bulgular

| ID | Kategori | Seviye | Risk Skoru | Exploit Senaryosu | Öneri |
|---|---|---|---|---|---|
| OWASP-A01-001 | Broken Access Control | KRİTİK | 20 | [senaryo] | [öneri] |
| ... | | | | | |

### Kapsam Dışı
[Projeye uygulanamayan kategoriler ve gerekçesi]

### Özet
| Seviye | Adet |
|---|---|
| KRİTİK | N |
| YÜKSEK | N |
| ORTA | N |
| DÜŞÜK | N |

---

## Hard Rules

- Her 10 kategoriyi değerlendir — uygulanamıyorsa "kapsam dışı — [gerekçe]" yaz.
- Dosya okuma veya yazma yapma.
- Exploit senaryosu olmayan bulgu yazma.

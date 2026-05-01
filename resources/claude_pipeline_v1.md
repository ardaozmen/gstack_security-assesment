Harika bir proje. Önce yapıyı netleştirelim, sonra her bileşeni detaylı tasarlayalım.Önce pipeline'ın genel mimarisini göstereyim, sonra her bir SKILL.md dosyasının tam içeriğini yazalım.Şimdi her bir SKILL.md dosyasını eksiksiz yazalım. Dosya yapısı şu şekilde olacak:

```
~/.claude/skills/secops/
├── sec-scope/SKILL.md
├── sec-threat-model/SKILL.md
├── sec-owasp/SKILL.md
├── sec-regulatory/SKILL.md
├── sec-igrc/SKILL.md
├── sec-risk-report/SKILL.md
└── sec-signoff/SKILL.md
```

---

## SKILL 1 — `/sec-scope`

```markdown
# /sec-scope

## Description
Güvenlik değerlendirmesinin ilk adımı. Projenin kapsamını, varlık envanterini,
veri akışlarını ve entegrasyonları haritalandır. Belirsiz veya eksik bilgileri
ortaya çıkar. Bu skill çalışmadan diğer hiçbir skill çalışmamalıdır.

Tetikleyiciler: "projeyi değerlendir", "güvenlik analizi başlat", "kapsam belirle",
"yeni proje var", "SEC-SCOPE", "/sec-scope"

## Role
Senior Security Analyst — Proje sahibinden bilgi toplayan, varsayımları sorgulayan,
eksikleri işaretleyen kıdemli güvenlik analisti. Agresif değil ama tavizsiz.
Yeterli bilgi gelmeden bir sonraki aşamaya geçmez.

## Instructions

### Adım 1 — Proje özetini al
Kullanıcıdan şunları iste (hepsini tek seferde):
- Projenin adı ve kısa açıklaması
- Projenin tipi: yeni geliştirme / mevcut sisteme entegrasyon / üçüncü taraf ürün
- Hangi ortamda çalışacak: on-premise / cloud / hybrid
- Hedef kullanıcı kitlesi: iç kullanıcı / kurumsal müşteri / bireysel müşteri / API tüketicisi
- Tahmini go-live tarihi

### Adım 2 — Varlık envanteri
Aşağıdaki kategorilerde varlıkları listele:
- Uygulamalar ve servisler (frontend, backend, API, worker, scheduler)
- Veri depoları (ilişkisel DB, NoSQL, dosya sistemi, cache, kuyruk)
- Dış entegrasyonlar (üçüncü taraf API, ödeme sistemi, kimlik sağlayıcı, SMS/e-posta servisi)
- Altyapı bileşenleri (CDN, load balancer, WAF, API gateway)
- Kişisel / hassas veri kategorileri (KVKK kapsamında: TC kimlik, finansal, sağlık, vb.)

### Adım 3 — Veri akışı haritası
Şu soruları yanıtla:
- Hangi veriler sisteme giriyor, sistemden çıkıyor?
- Veriler şifreli mi taşınıyor (TLS versiyonu, sertifika yönetimi)?
- Hangi veriler kalıcı olarak saklanıyor, hangisi geçici?
- Loglama yapılıyor mu? Loglar hassas veri içeriyor mu?
- Üçüncü taraflara hangi veriler iletiliyor?

### Adım 4 — Güven sınırlarını belirle
- İnternet ↔ DMZ ↔ İç Ağ sınırları nerede?
- Hangi bileşenler internetten direkt erişilebilir?
- Servisler arası iletişim nasıl authenticate ediliyor?
- Admin / operasyonel arayüzler nerede?

### Adım 5 — Varsayım ve eksik bilgi kaydı
Yanıtlanmayan her soruyu ASSUMPTION veya MISSING_INFO olarak işaretle.
Kritik eksikler için skope değerlendirmeyi BLOKLA ve kullanıcıya bildir.

### Adım 6 — SCOPE.md üret
Tüm bulguları aşağıdaki şablonla kaydet:

```
# Project Scope Document
**Project:** [ad]
**Date:** [tarih]
**Analyst:** SecOps Pipeline /sec-scope

## Project Overview
[özet]

## Asset Inventory
### Applications
- [liste]
### Data Stores
- [liste]
### External Integrations
- [liste]
### Sensitive Data Categories
- [KVKK/GDPR kategoriler]

## Data Flow Summary
[akış özeti]

## Trust Boundaries
[sınır tanımları]

## Key Assumptions
- [ASSUMPTION-001]: [açıklama]

## Missing Information
- [MISSING-001]: [açıklama] — [BLOCKER / WARNING]

## Scope Sign-off
[ ] Scope yeterli — /sec-threat-model çalıştırılabilir
[ ] Kritik eksik var — devam ENGELLENDI
```

## Inputs
- Kullanıcının proje tanımı (serbest metin veya önceki dokümanlar)

## Outputs
- `SCOPE.md` — sonraki tüm skill'lerin okuyacağı temel doküman

## Quality Gate
SCOPE.md'de en az şunlar dolu olmalı:
- Uygulama/servis listesi (en az 1 kayıt)
- Veri kategorileri (en az 1 kayıt)
- Güven sınırı tanımı
- Dış entegrasyon listesi (yoksa "YOK" yazılmalı, boş bırakılamaz)
Aksi halde /sec-threat-model çalıştırılamaz.
```

---

## SKILL 2 — `/sec-threat-model`

```markdown
# /sec-threat-model

## Description
SCOPE.md'yi okuyarak STRIDE metodolojisiyle tehdit modeli oluşturur.
Her bileşen ve veri akışı için saldırı senaryoları üretir. Trust boundary
ihlallerini tespit eder. Güven sınırları diyagramını metin formatında çizer.

Tetikleyiciler: "tehdit modeli oluştur", "STRIDE analizi", "trust boundary",
"/sec-threat-model"

## Role
Threat Modeler — Saldırgan bakış açısıyla sistemi inceleyen, "bu nasıl kötüye
kullanılır?" sorusunu sormaktan çekinmeyen güvenlik mimarı.

## Instructions

### Adım 1 — SCOPE.md oku
`SCOPE.md` dosyasını oku. Yoksa /sec-scope çalıştırılmasını talep et ve dur.

### Adım 2 — Bileşen-Tehdit Matrisi
Her bileşen için STRIDE kategorilerini tara:

| Kategori | Türkçe | Kontrol Sorusu |
|---|---|---|
| Spoofing | Kimlik Sahteciliği | Kimlik doğrulama var mı? Token/session manipülasyonu mümkün mü? |
| Tampering | Veri Manipülasyonu | Girdi doğrulama var mı? DB'ye yazma korumalı mı? |
| Repudiation | İnkar Edilebilirlik | Kritik işlemler loglanıyor mu? Log bütünlüğü korunuyor mu? |
| Info Disclosure | Bilgi İfşası | Hata mesajları fazla detay veriyor mu? Şifreleme eksik mi? |
| Denial of Service | Hizmet Reddi | Rate limiting var mı? Kaynak tüketimi kontrol ediliyor mu? |
| Elevation of Privilege | Yetki Yükseltme | Yetkilendirme her katmanda kontrol ediliyor mu? |

### Adım 3 — Veri Akışı Tehditleri
Her veri akışı için:
- Kaynaktan hedefe giden veri şifreli mi?
- Ortadaki adam saldırısı mümkün mü?
- Replay saldırısı mümkün mü?
- Veri doğrulama hangi katmanda yapılıyor?

### Adım 4 — Trust Boundary Analizi
Her güven sınırı geçişini sorgula:
- Bu sınırı kim/ne geçebilir?
- Kimlik doğrulama yöntemi nedir?
- Yetkilendirme kararı nerede alınıyor?
- Geçiş loglanıyor mu?

### Adım 5 — Saldırı Ağaçları (Attack Trees)
En kritik 3 saldırı senaryosu için attack tree yaz:
```
Hedef: [X'e yetkisiz erişim]
├── Yol 1: [kimlik doğrulama bypass]
│   ├── 1a: [SQL injection ile session token al]
│   └── 1b: [Brute force ile zayıf parola kır]
└── Yol 2: [servis mantığı istismarı]
    └── 2a: [IDOR ile başka kullanıcı verisine eriş]
```

### Adım 6 — THREAT_MODEL.md üret
```
# Threat Model
**Based on:** SCOPE.md
**Methodology:** STRIDE

## Component Threat Matrix
[bileşen × STRIDE matrisi]

## Data Flow Threats
[akış bazlı tehditler]

## Trust Boundary Violations
[ihlal senaryoları]

## Top Attack Trees
[3 attack tree]

## Threat Summary
- Total threats identified: [n]
- Critical: [n] | High: [n] | Medium: [n] | Low: [n]
```

## Inputs
- `SCOPE.md` (zorunlu)

## Outputs
- `THREAT_MODEL.md`
```

---

## SKILL 3 — `/sec-owasp`

```markdown
# /sec-owasp

## Description
OWASP Top 10 (2021) çerçevesinde sistemi analiz eder. Her OWASP kategorisi için
projenin mimari özelliklerine göre exploit senaryoları, etkilenen varlıklar ve
güvenlik gereksinimleri üretir. Kör nokta (eksik bilgi/varsayım) kayıtlarını tutar.

Tetikleyiciler: "OWASP analizi", "web güvenliği değerlendirmesi", "/sec-owasp"

## Role
AppSec Engineer — Kodu ve mimariyi OWASP lens'inden inceleyen uygulama güvenliği
mühendisi. Her bulgu için şu 6 alanı doldurur:
  risk_title | risk_category | severity | exploit_scenario | impacted_asset | confidence

## Instructions

### Adım 1 — Bağlam yükle
SCOPE.md ve THREAT_MODEL.md oku (varsa). Yoksa mevcut bilgiyle ilerle,
eksikleri ASSUMPTION olarak işaretle.

### Adım 2 — OWASP Top 10 Taraması
Her kategori için sistematik analiz yap:

**A01 — Broken Access Control**
- IDOR kontrolü var mı?
- Yatay ve dikey yetki yükseltme senaryoları?
- JWT/session token doğrulaması her endpoint'te mi?
- Admin fonksiyonları erişim kontrolü?

**A02 — Cryptographic Failures**
- Hassas veri şifreli mi (at-rest / in-transit)?
- Zayıf algoritma kullanımı (MD5, SHA1, DES, RC4)?
- Sertifika yönetimi ve geçerlilik süresi?
- Hardcoded credential riski?

**A03 — Injection**
- SQL, NoSQL, LDAP, OS command, SSTI, XXE injection?
- Parameterized query / prepared statement kullanımı?
- Input validation ve sanitization yerleri?

**A04 — Insecure Design**
- Güvenli tasarım ilkeleri (defense in depth, least privilege)?
- İş mantığı güvenliği (race condition, negatif miktar, vb.)?
- Threat modeling yapılmış mı?

**A05 — Security Misconfiguration**
- Default credential riski?
- Gereksiz açık port/servis/özellik?
- Stack trace / verbose hata mesajı?
- Security header eksikleri (CSP, HSTS, X-Frame-Options)?

**A06 — Vulnerable and Outdated Components**
- Kullanılan kütüphanelerin güvenlik durumu?
- Bağımlılık güncelleme süreci var mı?
- EOL (End-of-Life) bileşen riski?

**A07 — Identification and Authentication Failures**
- MFA uygulanmış mı?
- Parola politikası yeterli mi?
- Brute force koruması?
- Session yönetimi (timeout, logout, concurrent session)?

**A08 — Software and Data Integrity Failures**
- CI/CD pipeline güvenliği?
- Unsigned update / deserialization?
- Supply chain saldırı riski?

**A09 — Security Logging and Monitoring Failures**
- Kritik olaylar loglanıyor mu?
- Log bütünlüğü korunuyor mu?
- Anormallik tespiti / alerting var mı?
- Log saklama süresi (BDDK: min 5 yıl)?

**A10 — Server-Side Request Forgery (SSRF)**
- Dış URL çağrısı yapan endpoint var mı?
- Cloud metadata endpoint erişimi engellenmiş mi?
- Allowlist var mı?

### Adım 3 — Her bulgu için standart format
```yaml
- id: OWASP-A01-001
  risk_title: "IDOR ile müşteri hesabı erişimi"
  risk_category: "Broken Access Control"
  severity: CRITICAL | HIGH | MEDIUM | LOW | INFO
  exploit_scenario: |
    Saldırgan, /api/accounts/{id} endpoint'ine kendi oturumunu kullanarak
    başka bir müşterinin account ID'sini girerek hesap bilgilerine erişebilir.
    Yetkilendirme kontrolü yalnızca kimlik doğrulama ile sınırlı.
  impacted_asset: "Müşteri Hesap API, Müşteri Kişisel Verileri"
  confidence: HIGH | MEDIUM | LOW
  assumptions:
    - "API endpoint'lerinde object-level authorization eksik varsayılmaktadır"
  security_requirement: |
    Her API çağrısında kaynak sahibi doğrulanmalı (object-level authorization).
    Yetkisiz erişim denemesi loglanmalı ve alertlenmelidir.
```

### Adım 4 — OWASP_FINDINGS.md üret
```
# OWASP Top 10 Assessment
**Project:** [proje adı]
**Date:** [tarih]

## Executive Summary
- Total findings: [n]
- Critical: [n] | High: [n] | Medium: [n] | Low: [n]
- Coverage gaps: [eksik bilgi nedeniyle değerlendirilemeyen alanlar]

## Findings by Category
[A01 → A10 sırasıyla her bulgu]

## Key Assumptions
[ASSUMPTION listesi]

## Missing Information
[MISSING_INFO listesi]

## Top 3 Critical Risks
1. [risk adı] — [kısa açıklama]
2. [risk adı] — [kısa açıklama]
3. [risk adı] — [kısa açıklama]
```

## Inputs
- `SCOPE.md` (zorunlu)
- `THREAT_MODEL.md` (önerilir)

## Outputs
- `OWASP_FINDINGS.md`
```

---

## SKILL 4 — `/sec-regulatory`

```markdown
# /sec-regulatory

## Description
Türk finans sektörü mevzuatına göre uyum denetimi yapar:
- BDDK Bilgi Sistemleri Yönetmeliği (Madde bazlı)
- SPK Bilgi Sistemleri Tebliği
- KVKK (Kişisel Verilerin Korunması Kanunu)
- PCI-DSS (ödeme bileşeni varsa)

Tetikleyiciler: "mevzuat denetimi", "BDDK uyum", "regulatory review",
"SPK kontrolü", "/sec-regulatory"

## Role
Compliance Officer — Finans sektörü mevzuatını bilen, her gereksinimin
hangi madde kapsamında olduğunu gösteren uyum denetçisi. Muğlak ifadelerden
kaçınır, her bulguyu ilgili madde numarasına bağlar.

## Instructions

### Adım 1 — Uygulanabilir mevzuatı belirle
SCOPE.md'deki proje tipine göre:
- Banka projesi → BDDK Yönetmeliği zorunlu
- Sermaye piyasası → SPK Tebliği zorunlu
- Kişisel veri işleme → KVKK zorunlu
- Kart verisi → PCI-DSS zorunlu
- Hepsini işaretle, hangisinin uygulandığını SCOPE'dan tespit et

### Adım 2 — BDDK Bilgi Sistemleri Yönetmeliği Denetim Noktaları

**Sistem Güvenliği (Madde 9-14)**
- Erişim kontrolü politikası tanımlı mı?
- Kimlik doğrulama gereksinimleri karşılanıyor mu?
- Ayrıcalıklı kullanıcı (admin) yönetimi var mı?
- Sistem izleme ve loglama düzeni kurulu mu?

**Uygulama Güvenliği (Madde 15-18)**
- Güvenli yazılım geliştirme sürecine uyum?
- Kaynak kod güvenlik testi yapılıyor mu?
- Penetrasyon testi planlanmış mı?
- Yama yönetimi prosedürü var mı?

**Veri Güvenliği (Madde 19-22)**
- Hassas veriler şifreleniyor mu?
- Veri sınıflandırma yapılmış mı?
- Veri maskeleme uygulanıyor mu?
- Veri imha prosedürü var mı?

**İş Sürekliliği (Madde 23-28)**
- BCP/DRP planları var mı?
- RTO/RPO hedefleri tanımlanmış mı?
- Felaket kurtarma tatbikatı yapılıyor mu?
- Kritik sistemler için yedeklilik sağlanmış mı?

**Denetim İzi (Madde 29-32)**
- Log saklama süresi min 5 yıl mı?
- Log bütünlüğü korunuyor mu?
- Denetim izi silinemiyor mu?

**Dış Hizmet Alımı (Madde 33-38)**
- Üçüncü taraf tedarikçi güvenlik değerlendirmesi yapılmış mı?
- SLA güvenlik gereksinimleri içeriyor mu?
- Tedarikçi erişimi izleniyor mu?

### Adım 3 — Her bulgu için format
```yaml
- id: REG-BDDK-001
  regulation: "BDDK Bilgi Sistemleri Yönetmeliği"
  article: "Madde 15 - Uygulama Güvenliği"
  requirement: "Yazılım geliştirme sürecinde güvenlik testleri yapılmalıdır"
  current_status: COMPLIANT | PARTIAL | NON_COMPLIANT | UNKNOWN
  gap_description: |
    Proje kapsamında güvenlik testi planı bulunmamaktadır.
    Statik kod analizi (SAST) ve dinamik test (DAST) süreçleri tanımsız.
  remediation: |
    - Geliştirme pipeline'ına SAST aracı entegre edilmeli (SonarQube, Checkmarx)
    - Go-live öncesi penetrasyon testi planlanmalı
    - Test sonuçları BDDK'ya raporlanabilir formatta tutulmalı
  priority: CRITICAL | HIGH | MEDIUM | LOW
```

### Adım 4 — REGULATORY_FINDINGS.md üret
```
# Regulatory Compliance Assessment
**Applicable Regulations:** [liste]
**Date:** [tarih]

## Compliance Summary Matrix
| Mevzuat | Madde | Durum | Öncelik |
|---|---|---|---|
[tablo]

## Detailed Findings
[her bulgu]

## Non-Compliance Risks
[uyumsuzluk durumunda yasal yaptırım riskleri]

## Remediation Roadmap
[öncelik sırasına göre iyileştirme adımları]
```

## Inputs
- `SCOPE.md` (zorunlu)
- `OWASP_FINDINGS.md` (önerilir)

## Outputs
- `REGULATORY_FINDINGS.md`
```

---

## SKILL 5 — `/sec-igrc`

```markdown
# /sec-igrc

## Description
iGRC (Integrated Governance, Risk and Compliance) perspektifinden iç kontrol
gereksinimlerini analiz eder. Kurumun mevcut politika ve prosedür dokümanlarıyla
projeyi karşılaştırır. Kontrol açıklarını ve sorumluluk boşluklarını tespit eder.

Tetikleyiciler: "iGRC analizi", "iç kontrol", "governance review", "/sec-igrc"

## Role
iGRC Analyst — Kurumun iç kontrol çerçevesini bilen, projenin mevcut politikalarla
uyumunu değerlendiren, kontrol sahipliği ve sorumluluk matrisini oluşturan analist.

## Instructions

### Adım 1 — Politika dokümanlarını al
Kullanıcıdan şunları iste:
- Bilgi Güvenliği Politikası
- Erişim Yönetimi Prosedürü
- Değişiklik Yönetimi Prosedürü
- Olay Yönetimi Prosedürü
- Tedarikçi Yönetimi Politikası
Yoksa ASSUMPTION olarak işaretle.

### Adım 2 — Kontrol Kategorileri

**Erişim Kontrolü**
- Least privilege ilkesi uygulanıyor mu?
- Görev ayrılığı (segregation of duties) sağlanıyor mu?
- Ayrıcalıklı erişim gözden geçirme süreci var mı?
- Hesap yaşam döngüsü yönetimi tanımlı mı?

**Değişiklik Yönetimi**
- Değişiklik onay süreci var mı?
- Emergency change prosedürü tanımlı mı?
- Rollback planı mevcut mu?
- Change freeze dönemleri tanımlı mı?

**Olay Yönetimi**
- Güvenlik olayı tanımı ve sınıflandırması yapılmış mı?
- Eskalasyon matrisi tanımlı mı?
- BDDK'ya bildirim süreci (72 saat kuralı) var mı?
- Post-mortem prosedürü var mı?

**Risk Yönetimi**
- Proje risk değerlendirmesi yapılmış mı?
- Artık risk kabul süreci tanımlı mı?
- Risk iştahı dokümante edilmiş mi?
- Periyodik risk gözden geçirme planlanmış mı?

**Tedarikçi Yönetimi**
- Tedarikçi güvenlik değerlendirmesi prosedürü var mı?
- Veri işleme sözleşmesi (DPA) imzalanmış mı?
- Tedarikçi erişim logları tutuluyor mu?
- Tedarikçi audit hakkı sözleşmede var mı?

### Adım 3 — RACI Matrisi Üret
Kritik kontroller için sorumluluk matrisi:
```
| Kontrol | Sorumlu | Onaylayan | Danışılan | Bilgilendirilen |
|---|---|---|---|---|
| Erişim yönetimi | IAM Ekibi | CISO | Uygulama Sahibi | Denetim |
```

### Adım 4 — Kontrol Boşluğu Analizi
```yaml
- id: IGRC-001
  control_domain: "Erişim Kontrolü"
  control_name: "Ayrıcalıklı hesap gözden geçirme"
  policy_reference: "Erişim Yönetimi Prosedürü v2.1, Madde 5.3"
  expected_control: "Ayrıcalıklı hesaplar 3 ayda bir gözden geçirilmeli"
  current_state: "Gözden geçirme prosedürü proje kapsamında tanımlanmamış"
  gap_type: MISSING | PARTIAL | INEFFECTIVE
  risk_implication: |
    Eski çalışanlara ait hesaplar aktif kalabilir veya gereksizsiz
    ayrıcalıklar birikebilir (privilege creep).
  remediation: |
    - Proje kapsamına ayrıcalıklı hesap gözden geçirme aktivitesi ekle
    - IAM ekibiyle quarterly review takvimi oluştur
  control_owner: "IAM Ekibi"
  review_frequency: "Quarterly"
```

### Adım 5 — IGRC_FINDINGS.md üret

## Inputs
- `SCOPE.md` (zorunlu)
- İç politika dokümanları (varsa)
- `REGULATORY_FINDINGS.md` (önerilir)

## Outputs
- `IGRC_FINDINGS.md`
- `RACI_MATRIX.md`
```

---

## SKILL 6 — `/sec-risk-report`

```markdown
# /sec-risk-report

## Description
Tüm önceki skill çıktılarını konsolide eder. OWASP + STRIDE + Mevzuat + iGRC
bulgularını tek bir yönetici raporu haline getirir. Risk skorlaması yapar,
öncelik sırasına koyar ve aksiyon planı üretir.

Tetikleyiciler: "risk raporu üret", "konsolide rapor", "executive summary",
"/sec-risk-report"

## Role
Risk Officer — Teknik bulguları iş dili ve risk skoru olarak ifade eden,
yönetim kuruluna sunulabilecek kalitede rapor yazan risk yöneticisi.

## Instructions

### Adım 1 — Tüm bulguları topla
Şu dosyaları oku:
- `SCOPE.md`
- `THREAT_MODEL.md`
- `OWASP_FINDINGS.md`
- `REGULATORY_FINDINGS.md`
- `IGRC_FINDINGS.md`

### Adım 2 — Risk Skorlama
Her bulgu için DREAD veya CVSS benzeri skoring:

```
Risk Skoru = Olasılık × Etki

Olasılık: 1 (Düşük) → 5 (Yüksek)
Etki:     1 (Düşük) → 5 (Kritik)

Skor 20-25: CRITICAL
Skor 12-19: HIGH
Skor 6-11:  MEDIUM
Skor 1-5:   LOW
```

Ayrıca her bulgu için:
- `exploitability`: Teknik beceri gereksinimi (LOW / MEDIUM / HIGH)
- `detectability`: Mevcut monitoring ile tespit edilebilirlik
- `financial_impact`: Yaklaşık finansal etki (kaba tahmin)
- `regulatory_penalty`: Mevzuat yaptırım riski (VAR / YOK / BELİRSİZ)

### Adım 3 — Konsolide Risk Kayıt Defteri
Tüm benzersiz risk ID'lerini tek tabloda topla:
```
| ID | Başlık | Kaynak | Severity | Skor | Sahip | Hedef Tarih |
|---|---|---|---|---|---|---|
```

### Adım 4 — Yönetici Özeti (Executive Summary)
Teknik olmayan okuyucu için:
- Proje ne yapıyor (2 cümle)
- Değerlendirme kapsamı (hangi metodolojiler)
- Öne çıkan riskler (3 madde)
- Kritik aksiyonlar (go-live öncesi yapılması zorunlular)
- Genel güvenlik duruşu: RED / AMBER / GREEN + gerekçe

### Adım 5 — Aksiyon Planı
```
Priority 0 — BLOCKER (go-live önce çözülmeli):
  [ ] [OWASP-A01-001] IDOR kontrolü eklenmeli — Sorumlu: Backend Ekibi — 5 gün
  
Priority 1 — HIGH (go-live sonrası 30 gün):
  [ ] [REG-BDDK-001] Penetrasyon testi planlanmalı — Sorumlu: CISO — 30 gün

Priority 2 — MEDIUM (90 gün):
  [ ] [IGRC-001] Ayrıcalıklı hesap review prosedürü — Sorumlu: IAM — 90 gün
```

### Adım 6 — RISK_REPORT.md üret
Tam yönetici raporu, tüm bölümleriyle.

## Inputs
- Tüm önceki skill çıktıları (`SCOPE.md`, `THREAT_MODEL.md`, `OWASP_FINDINGS.md`,
  `REGULATORY_FINDINGS.md`, `IGRC_FINDINGS.md`)

## Outputs
- `RISK_REPORT.md` — ana çıktı
- `RISK_REGISTER.csv` — tüm riskler makine-okunabilir formatta
```

---

## SKILL 7 — `/sec-signoff`

```markdown
# /sec-signoff

## Description
Değerlendirme sürecinin son aşaması. RISK_REPORT.md'yi inceler, go-live kararı
için zemin hazırlar. Blocker yoksa onay verir, varsa eskalasyon matrisi çalıştırır.
Nihai karar her zaman insana aittir — bu skill KARAR VERMEZ, zemin hazırlar.

Tetikleyiciler: "sign-off", "onay hazırlığı", "go-live kararı", "/sec-signoff"

## Role
Security Review Board — Tüm bulguları gözden geçiren, onay / ret /
koşullu onay kararı için gerekli bilgiyi hazırlayan güvenlik kurulu.

## Instructions

### Adım 1 — RISK_REPORT.md oku
Yoksa /sec-risk-report çalıştırılmasını talep et.

### Adım 2 — Blocker Kontrolü
Priority 0 (BLOCKER) listesini tara:
- Tüm BLOCKER'lar kapatılmış mı?
- Kapatılmamış BLOCKER varsa: GO-LIVE ENGELLENDİ
- BLOCKER yoksa: koşullu onay değerlendirmesine geç

### Adım 3 — Koşullu Onay Kriterleri
HIGH bulguların durumuna göre:
- HIGH bulgu sayısı 3'ten az ve sahipleri atanmışsa: CONDITIONAL_APPROVAL
- HIGH bulgu sayısı 3 ve üzeri: CISO onayı gerekli
- CRITICAL regulatory bulgu varsa: Hukuk + CISO onayı gerekli

### Adım 4 — Sign-off Paketi Üret
```markdown
# Security Sign-off Package
**Project:** [ad]
**Assessment Date:** [tarih]
**Assessor:** SecOps Pipeline

## Decision Recommendation
STATUS: GO / NO_GO / CONDITIONAL_GO

## Rationale
[karar gerekçesi]

## Open Blockers
[varsa liste — yoksa "Blocker bulunamadı"]

## Accepted Risks (Conditional Go)
[açık HIGH/MEDIUM riskler ve kabul gerekçesi]

## Post-Go-Live Obligations
- [ ] [aksiyon] — [sorumlu] — [tarih]

## Required Approvals
- [ ] CISO onayı — [gerekli / gerekli değil]
- [ ] Hukuk onayı — [gerekli / gerekli değil]
- [ ] Üst Yönetim onayı — [gerekli / gerekli değil]

## Escalation Matrix
BLOCKER varsa → CISO → CTO → Yönetim Kurulu
CRITICAL regulatory → Hukuk + CISO
HIGH finansal etki → CFO bilgilendirmesi

---
NOT: Bu belge karar önerisi içerir. Nihai onay yetkisi
    ilgili kurum temsilcisine aittir.
```

## Inputs
- `RISK_REPORT.md` (zorunlu)
- Tüm önceki dokümanlar

## Outputs
- `SIGNOFF_PACKAGE.md`
```

---

## CLAUDE.md Girişi

Projenin `CLAUDE.md` dosyasına şunu ekle:

```markdown
## SecOps Assessment Pipeline

Bilgi güvenliği proje değerlendirmeleri için bu pipeline'ı kullan.
Sıraya uy — her skill öncekinin çıktısına bağlıdır.

Mevcut skills:
- /sec-scope        → Kapsam ve varlık envanteri (her zaman ilk)
- /sec-threat-model → STRIDE tehdit modellemesi
- /sec-owasp        → OWASP Top 10 analizi
- /sec-regulatory   → BDDK / SPK / KVKK mevzuat denetimi
- /sec-igrc         → iGRC iç kontrol analizi
- /sec-risk-report  → Konsolide risk raporu (her zaman son iki adımdan önce)
- /sec-signoff      → Go-live onay / eskalasyon paketi (her zaman en son)

Hızlı başlatma:
  /sec-scope ile başla, ardından /sec-risk-report çalıştır.
  Eksiksiz değerlendirme için tüm skill'leri sırayla çalıştır.

Çıktı dosyaları: SCOPE.md, THREAT_MODEL.md, OWASP_FINDINGS.md,
REGULATORY_FINDINGS.md, IGRC_FINDINGS.md, RISK_REPORT.md,
RISK_REGISTER.csv, SIGNOFF_PACKAGE.md
```

---

## Bir sonraki adım için öneriler

Bu tasarımın üzerine birkaç şey daha ekleyebiliriz — bunların hangisinden başlamak istersin?

1. `/sec-autoplan` — Garry Tan'ın `/autoplan`'ına benzer şekilde tüm pipeline'ı tek komutla sırayla çalıştıran orkestratör skill
2. Her skill için gerçek proje verisiyle çalışan örnek output dokümanları (mock SCOPE.md, mock RISK_REPORT.md)
3. `/sec-retro` — Değerlendirme süreci sonrası öğrenilenleri kaydeden retrospektif skill
4. Risk Register için Excel/CSV şablonu ve risk ısı haritası görselleştirmesi

---

## SKILL 8 — `/sec-autoplan`

```markdown
# /sec-autoplan

## Description
SecOps pipeline'ını tek komutla yöneten orkestratör skill. Her adımı sırayla
çalıştırır, quality gate'leri denetler, insan yargısı gerektiren noktalarda durur
ve sorar, context'i sonraki adımlara taşır.

Bu skill karar verici değildir; süreç yöneticisidir.
Nihai güvenlik/onay kararı yine insana aittir.

Tetikleyiciler: "sec autoplan", "pipeline'ı başlat", "tam güvenlik değerlendirmesi yap",
"tüm güvenlik adımlarını çalıştır", "/sec-autoplan"

## Role
Security Orchestrator — Sıra yönetimi, bağımlılık denetimi, quality gate kontrolü,
context taşıma ve insan kararı noktalarından sorumludur.
Hiçbir adımı atlamaz, sıralamayı bozmaz, muğlak kararları insan onayına taşır.

## Pipeline Modları
| Mod | Çalışan Adımlar | Kullanım Amacı |
|---|---|---|
| `full` (varsayılan) | 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 | Tam değerlendirme |
| `fast` | 1 -> 3 -> 6 | Hızlı teknik güvenlik resmi |
| `compliance` | 1 -> 4 -> 5 -> 6 -> 7 | Mevzuat odaklı denetim |
| `resume` | Belirtilen adımdan devam | Yarıda kalan pipeline'ı sürdür |

Paralel çalışabilecek adımlar (bağımsız): `3`, `4`, `5`
Zorunlu sıra: `1 -> 2 -> {3,4,5} -> 6 -> 7`

## Instructions

### Adım 0 — Başlangıç kontrolü
#### 0a. Mod ve parametre ayrıştır
Komutu parse et:
- `/sec-autoplan` -> `mode=full`, `retry_from=1`, `force_refresh=false`
- `/sec-autoplan mode=compliance` -> compliance modu
- `/sec-autoplan resume` -> `AUTO_PLAN_STATUS.md` içindeki son başarısız adımdan devam
- `/sec-autoplan force_refresh=true` -> mevcut çıktıları yoksay, hepsini yeniden üret

#### 0b. Mevcut çıktı kontrolü
`force_refresh=false` ise hangi dosyaların mevcut olduğunu kontrol et:
- `SCOPE.md` -> `/sec-scope` tamamlanmış
- `THREAT_MODEL.md` -> `/sec-threat-model` tamamlanmış
- `OWASP_FINDINGS.md` -> `/sec-owasp` tamamlanmış
- `REGULATORY_FINDINGS.md` -> `/sec-regulatory` tamamlanmış
- `IGRC_FINDINGS.md` -> `/sec-igrc` tamamlanmış
- `RACI_MATRIX.md` -> `/sec-igrc` tamamlanmış (ikincil çıktı)
- `RISK_REPORT.md` -> `/sec-risk-report` tamamlanmış
- `RISK_REGISTER.csv` -> `/sec-risk-report` tamamlanmış (ikincil çıktı)
- `SIGNOFF_PACKAGE.md` -> `/sec-signoff` tamamlanmış

Mevcut dosyaları yeniden üretme, quality gate'den geçir. Geçerliyse sonraki adıma ilerle.

#### 0c. Minimum proje bağlamı kontrolü
Proje bağlamı (isim, tip, özet) mevcut değilse kullanıcıdan al:
1. Proje adı ve tek cümlelik açıklaması
2. Proje tipi: `[yeni geliştirme / mevcut sisteme entegrasyon / üçüncü taraf ürün]`
3. Banka projesi mi? (`BDDK` mevzuatı belirlemek için)

### Adım 1 — Context Snapshot Yönetimi
Her adım geçişinde `PIPELINE_CONTEXT.md` dosyasını güncelle.
Bu dosya bir sonraki skill'in ihtiyaç duyacağı özeti taşır.

Şablon:
```markdown
# Pipeline Context Snapshot
**Updated:** [timestamp]
**Current Step:** [n]
**Mode:** [mod]

## Project Summary (2 cümle max)
[proje özeti]

## Key Decisions Made
- [DECISION-001]: Risk iştahı = MEDIUM (kullanıcı onaylı, Step 1)
- [DECISION-002]: BDDK mevzuatı uygulanabilir (banka projesi)

## Critical Findings So Far
- [CRITICAL-001]: [başlık] — kaynak: [skill-adı]

## Open Taste Decisions
- [TASTE-001]: [soru] — bekleniyor

## Completed Steps
- Step 1: /sec-scope — PASS
- Step 2: /sec-threat-model — PASS
```

### Adım 2 — Yürütme Döngüsü (Her Adım İçin)
Her skill için şu döngüyü uygula:
1. `PIPELINE_CONTEXT.md` dosyasını skill'e bağlam olarak ver
2. Skill'i çalıştır
3. Beklenen çıktı dosyasını doğrula
4. Quality gate kontrolünü çalıştır
5. Taste decision gerekiyor mu? Evetse dur ve sor, hayırsa devam et
6. `PIPELINE_CONTEXT.md` dosyasını güncelle
7. `AUTO_PLAN_STATUS.md` dosyasını güncelle
8. Sonraki adıma geç

### Adım 3 — Quality Gates (Geliştirilmiş)
#### Gate-SCOPE
Dosya: `SCOPE.md`

Zorunlu kontroller (biri başarısızsa `FAIL`):
- [ ] Asset inventory: en az 1 uygulama/servis kaydı var
- [ ] Sensitive data: dolu veya açıkça `YOK` yazılmış (boş bırakılamaz)
- [ ] Trust boundary: en az 1 sınır tanımlı
- [ ] External integrations: dolu veya açıkça `YOK` yazılmış
- [ ] `MISSING_INFO` blocker listesi: her blocker için çözüm notu var

Uyarı kontrolleri (biri başarısızsa `WARNING`, pipeline devam eder):
- [ ] Veri akışı haritası var
- [ ] Hassas veri kategorileri KVKK kapsamında sınıflandırılmış
- [ ] Tahmini go-live tarihi belirtilmiş

Taste decision:
- `MISSING_INFO` sayısı >= 3 -> "Kritik eksiklere rağmen devam etmeli miyiz? (Y/N + gerekçe)"
- Dış entegrasyon sayısı >= 5 -> "Bu entegrasyonlar için ayrı tehdit modeli istiyor musun?"
- Bulut ortamı + finansal veri -> "Cloud security review kapsamına alınsın mı?"

#### Gate-THREAT
Dosya: `THREAT_MODEL.md`

Zorunlu kontroller:
- [ ] STRIDE 6 kategori de ele alınmış (yoksa "bu kategori uygulanamaz" notu var)
- [ ] Trust boundary ihlalleri: en az 1 senaryo veya "ihlal tespit edilmedi" notu
- [ ] Attack trees: en az 1 ağaç (yoksa "saldırı yolu bulunamadı" notu)
- [ ] Tehdit özeti: toplam sayı ve severity dağılımı var

Taste decision:
- Yüksek karmaşıklıklı attack tree (>= 3 dal) varsa -> "Bu saldırı senaryosunu detaylı ele almamı ister misin?"

#### Gate-OWASP
Dosya: `OWASP_FINDINGS.md`

Zorunlu kontroller:
- [ ] A01-A10 her kategori ele alınmış (yoksa "bu uygulama için geçersiz" notu)
- [ ] Her bulguda: `risk_title`, `severity`, `exploit_scenario`, `confidence` dolu
- [ ] Top 3 kritik risk listelenmiş veya "kritik risk tespit edilmedi" yazılmış
- [ ] Toplam bulgu sayısı raporlanmış

Uyarı kontrolleri:
- [ ] `confidence=LOW` bulgu sayısı, toplam bulguların %50'sinden az
- [ ] Her `CRITICAL` bulgunun `impacted_asset` alanı dolu

Taste decision:
- `CRITICAL` bulgu sayısı >= 3 -> "Bu kadar kritik bulguyla pipeline devam etmeli mi, yoksa önce bunları ele alalım mı?"
- `confidence=LOW` olan `CRITICAL` bulgu varsa -> "Doğrulama için ek bilgi toplamak ister misin?"

#### Gate-REG
Dosya: `REGULATORY_FINDINGS.md`

Zorunlu kontroller:
- [ ] Uygulanabilir mevzuat listesi var ve gerekçelendirilmiş
- [ ] Her mevzuat için ilgili maddeler eşlenmiş
- [ ] `NON_COMPLIANT` bulgular için remediation önerisi var
- [ ] Compliance summary matrisi var

Uyarı kontrolleri:
- [ ] BDDK projesi ise loglama, yama yönetimi, 3. taraf maddeleri ele alınmış
- [ ] Kişisel veri işleniyorsa KVKK maddeleri ele alınmış

Taste decision:
- `NON_COMPLIANT + CRITICAL` kombinasyonu -> "Bu mevzuat ihlali go-live blocker sayılsın mı?"
- `UNKNOWN` statüde madde sayısı >= 3 -> "Hukuk birimi devreye alınsın mı?"

#### Gate-IGRC
Dosyalar: `IGRC_FINDINGS.md`, `RACI_MATRIX.md`

Zorunlu kontroller:
- [ ] En az 1 kontrol boşluğu tanımlı (yoksa "kontrol boşluğu tespit edilmedi" notu)
- [ ] RACI matrisi: her kritik kontrol için `Responsible` kolonu dolu
- [ ] Her gap için: `gap_type` ve `remediation` alanı dolu
- [ ] Her kayıtta `control_owner` var

Uyarı kontrolleri:
- [ ] `review_frequency` tanımlı
- [ ] `policy_reference` var (yoksa "politika mevcut değil" notu)

Taste decision:
- `control_owner` "belirsiz" veya "TBD" ise -> "Atanmamış kontroller için sorumlu kim olmalı? (Devam etmeden önce netleştirelim)"

#### Gate-RISK
Dosyalar: `RISK_REPORT.md`, `RISK_REGISTER.csv`

Zorunlu kontroller:
- [ ] Executive summary var (teknik olmayan okuyucuya uygun)
- [ ] Her bulgu için risk skoru hesaplanmış
- [ ] Priority 0 (`BLOCKER`) listesi var (yoksa "blocker yok" yazılmış)
- [ ] Aksiyon listesinde her iş için sorumlu ve hedef tarih var
- [ ] Genel güvenlik duruşu: `RED/AMBER/GREEN` + gerekçe

Taste decision:
- Priority 0 listesi boşsa -> "Blocker olmadan go-live uygundur, onaylıyor musun?"
- Risk skoru hesaplanamayan bulgu varsa -> "Bu bulgu için risk skoru nasıl belirlenmeli?"
- Finansal etki tahmini tercihi -> "Yaklaşık finansal etki tahmini raporda yer alsın mı?"

#### Gate-SIGNOFF
Dosya: `SIGNOFF_PACKAGE.md`

Zorunlu kontroller:
- [ ] `GO / NO_GO / CONDITIONAL_GO` önerisi var
- [ ] Karar gerekçesi var (en az 2 cümle)
- [ ] Açık blocker listesi var (yoksa "blocker yok" yazılmış)
- [ ] `Required approvals` bölümü var (her onay için gerekli/gerekli değil)
- [ ] `Post-go-live` yükümlülükleri listesi var

Taste decision:
- Öneri `NO_GO` ise -> "Hangi koşullar sağlanırsa `CONDITIONAL_GO`'ya geçilebilir? Bu koşulları belirleyelim mi?"
- `CRITICAL regulatory` bulgu + `CONDITIONAL_GO` ise -> "Bu kombinasyon Hukuk onayı gerektiriyor. Hukuk bildirim metnini şimdi hazırlayayım mı?"

### Adım 4 — Hata Yönetimi
Gate `FAIL` durumunda:
1. Pipeline'ı durdur
2. Başarısız gate ve nedeni `AUTO_PLAN_STATUS.md` dosyasına yaz
3. Somut çözüm adımlarını listele
4. Tekrarlanabilir devam komutunu göster

Örnek çıktı:
```text
PIPELINE DURDURULDU — Gate-IGRC FAIL

Neden: RACI_MATRIX.md'de 3 kontrolün Responsible kolonu boş.
Etkilenen kontroller: [Erişim gözden geçirme], [Log bütünlüğü], [Yama yönetimi]

Aksiyon:
1. /sec-igrc tekrar çalıştır
2. Şu soruları yanıtla:
   - Erişim gözden geçirme sahibi hangi ekip?
   - Log yönetimi kimin sorumluluğunda?
   - Yama yönetimi prosedürü var mı?

Devam komutu: /sec-autoplan resume
```

`WARNING` durumunda:
- Pipeline devam eder
- Warning kaydedilir ve nihai raporda listelenir
- Kullanıcıya bilgi verilir, onay beklenmez

### Adım 5 — Final Paket
Başarılı tamamlamada `AUTO_PLAN_STATUS.md` üret:

```markdown
# SecOps AutoPlan — Final Status
**Mode:** [full|fast|compliance]
**Date:** [tarih]
**Overall Status:** SUCCESS | PARTIAL | FAILED
**Duration:** [adım sayısı]

## Step Results
| Step | Skill | Status | Output | Taste Decisions | Warnings |
|---|---|---|---|---|---|
| 1 | /sec-scope | PASS | SCOPE.md | 0 | 1 |
| 2 | /sec-threat-model | PASS | THREAT_MODEL.md | 1 | 0 |
| 3 | /sec-owasp | PASS | OWASP_FINDINGS.md | 2 | 0 |
| 4 | /sec-regulatory | PASS | REGULATORY_FINDINGS.md | 1 | 2 |
| 5 | /sec-igrc | PASS | IGRC_FINDINGS.md | 1 | 1 |
| 6 | /sec-risk-report | PASS | RISK_REPORT.md | 1 | 0 |
| 7 | /sec-signoff | PASS | SIGNOFF_PACKAGE.md | 0 | 0 |

## Key Decisions (Taste Decisions Resolved)
- [DECISION-001]: Risk iştahı = MEDIUM (Step 1, kullanıcı onaylı)
- [DECISION-002]: Cloud review kapsama alındı (Step 1, kullanıcı onaylı)
- [DECISION-003]: 3 CRITICAL bulgu nedeniyle Hukuk devreye alındı (Step 4)

## Open Warnings (resolved during pipeline)
- [WARNING-001]: Veri akışı haritası eksik — devam kararı alındı

## Output Files
- SCOPE.md
- THREAT_MODEL.md
- OWASP_FINDINGS.md
- REGULATORY_FINDINGS.md
- IGRC_FINDINGS.md
- RACI_MATRIX.md
- RISK_REPORT.md
- RISK_REGISTER.csv
- SIGNOFF_PACKAGE.md
- PIPELINE_CONTEXT.md (bağlam kaydı)

## Final Recommendation
[RISK_REPORT.md'deki güvenlik duruşu buraya kopyalanır]

## Recommended Next Commands
[ ] /sec-signoff -> nihai onay paketi için insan onayı gerekiyor
```

### Adım 6 — Retry Semantiği
| Komut | Davranış |
|---|---|
| `/sec-autoplan` | Full pipeline, tüm adımları çalıştır |
| `/sec-autoplan resume` | AUTO_PLAN_STATUS.md'deki son FAIL adımından devam |
| `/sec-autoplan mode=fast` | Fast mod |
| `/sec-autoplan mode=compliance` | Compliance modu |
| `/sec-autoplan force_refresh=true` | Tüm çıktıları yeniden üret |
| `/sec-autoplan retry_from=3` | 3. adımdan devam et |
| `/sec-autoplan retry_from=3 force_refresh=3` | Yalnızca 3. adımı yenile, diğerlerini koru |

## Inputs
- Kullanıcı proje özeti
- Varsa önceki çıktı dosyaları
- Varsa `AUTO_PLAN_STATUS.md` (`resume` modu için)

## Outputs
- `AUTO_PLAN_STATUS.md` (zorunlu)
- `PIPELINE_CONTEXT.md` (zorunlu, bağlam taşıma)
- Seçilen moda göre tüm ara çıktılar

## Guardrails
- Zorunlu sıra bozulamaz (`1 -> 2 -> {3,4,5} -> 6 -> 7`)
- Quality gate geçmeden sonraki adıma geçilemez
- Kritik eksik bilgiyle `PASS` işaretlenemez
- Taste decision cevaplanmadan ilerlenemez
- `/sec-signoff` sonucu öneridir; nihai karar insan onayındadır
- `PIPELINE_CONTEXT.md` her adımda güncellenmek zorundadır (context kayıp önleme)
```

---

## Structured Project Layout

Bu dosya (`claude_pipeline_v1.md`) master README olarak kalir.
Operasyonel ve bakimi kolay moduler yapi `secops/` altina ayrilmistir:

- `secops/README.md` -> navigasyon ve kullanim
- `secops/pipeline/` -> orchestrator kontrati, modlar, quality gates
- `secops/roles/` -> rol katalogu
- `secops/skills/` -> skill katalogu
- `secops/templates/` -> status/context sablonlari
- `secops/docs/` -> design pattern dokumani

Bu ayrimla birlikte:
- Master dosya strateji ve tam baglami korur
- Alt klasorler implementation-level dokumantasyonu tasir
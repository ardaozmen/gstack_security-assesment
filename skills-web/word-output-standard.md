# Word Output Standard — Claude Web

LLM, aşağıdaki HTML şablonlarını **artifact olarak** üretir.
Microsoft Word `.html` dosyalarını natively açar.

Her iki artifact için **aynı CSS** kullanılır — aşağıda tanımlı.

---

## Paylaşılan CSS

Her HTML artifact'ın `<head>` bölümüne ekle:

```html
<style>
  body {
    font-family: Calibri, sans-serif;
    font-size: 11pt;
    color: #212121;
    margin: 2.5cm 2.5cm 2.5cm 3cm;
    line-height: 1.4;
  }
  h1 { font-size: 18pt; color: #1F3864; font-weight: bold;
       border-bottom: 2px solid #1F3864; padding-bottom: 6px; margin-top: 0; }
  h2 { font-size: 14pt; color: #2E5496; font-weight: bold; margin-top: 24px; }
  h3 { font-size: 12pt; color: #2E5496; margin-top: 16px; }
  table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 10pt; }
  th { background-color: #1F3864; color: #fff; font-weight: bold;
       padding: 6px 8px; text-align: left; border: 1px solid #1F3864; }
  td { padding: 5px 8px; border: 1px solid #ccc; vertical-align: top; }
  tr.critical { background-color: #FFE0E0; }
  tr.high     { background-color: #FFF3CD; }
  tr.medium   { background-color: #FFF9C4; }
  tr.low      { background-color: #E8F5E9; }
  .posture-red   { color: #C62828; font-weight: bold; font-size: 13pt; }
  .posture-amber { color: #E65100; font-weight: bold; font-size: 13pt; }
  .posture-green { color: #2E7D32; font-weight: bold; font-size: 13pt; }
  .tag-critical { background: #C62828; color: #fff; padding: 2px 6px; border-radius: 3px; font-size: 9pt; }
  .tag-high     { background: #E65100; color: #fff; padding: 2px 6px; border-radius: 3px; font-size: 9pt; }
  .tag-medium   { background: #F9A825; color: #fff; padding: 2px 6px; border-radius: 3px; font-size: 9pt; }
  .cover { text-align: center; padding: 60px 0 40px; border-bottom: 3px solid #1F3864; margin-bottom: 32px; }
  .cover h1 { border: none; font-size: 24pt; }
  .cover .meta { font-size: 11pt; color: #555; margin-top: 16px; line-height: 1.8; }
  .disclaimer { background-color: #FFF9C4; border: 1px solid #F9A825;
                padding: 10px 14px; font-size: 10pt; margin-top: 32px; color: #555; }
  pre, code { font-family: Consolas, "Courier New", monospace; font-size: 9pt;
              background: #F5F5F5; border: 1px solid #E0E0E0; padding: 8px;
              display: block; white-space: pre-wrap; }
  .page-break { page-break-before: always; }
</style>
```

---

## threat-modeling.html

`/sec-threat-model` tarafından Phase 7'de üretilir.

```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>Threat Model — [PROJE_ADI]</title>
  <!-- PAYLAŞILAN CSS BURAYA -->
</head>
<body>

<div class="cover">
  <h1>Threat Model Raporu</h1>
  <div class="meta">
    <strong>Proje:</strong> [PROJE_ADI]<br>
    <strong>Tarih:</strong> [ISO_TARIH]<br>
    <strong>Metodoloji:</strong> STRIDE<br>
    <strong>Hazırlayan:</strong> Security Assessment Pipeline /sec-threat-model
  </div>
</div>

<h2>Yönetici Özeti</h2>
<p>[2-3 cümle: en kritik tehditler, genel risk seviyesi, önerilen öncelikli aksiyon]</p>

<table>
  <tr><th>Toplam</th><th>Kritik</th><th>Yüksek</th><th>Orta</th><th>Düşük</th></tr>
  <tr><td>[N]</td><td>[N]</td><td>[N]</td><td>[N]</td><td>[N]</td></tr>
</table>

<h2>Kapsam Referansı</h2>
<ul>
  <li><strong>Uygulamalar:</strong> [liste]</li>
  <li><strong>Veri Depoları:</strong> [liste]</li>
  <li><strong>Güven Sınırları:</strong> [liste]</li>
  <li><strong>Hassas Veri:</strong> [liste]</li>
</ul>

<div class="page-break"></div>
<h2>STRIDE Bileşen Tehdit Matrisi</h2>
<table>
  <tr>
    <th>Varlık</th><th>Spoofing</th><th>Tampering</th>
    <th>Repudiation</th><th>Info Disclosure</th><th>DoS</th><th>EoP</th>
  </tr>
  <!-- Her varlık için bir satır — class: critical / high / medium / low -->
  <tr class="[seviye]">
    <td>[varlık]</td><td>[bulgu/YOK]</td><td>[bulgu/YOK]</td>
    <td>[bulgu/YOK]</td><td>[bulgu/YOK]</td><td>[bulgu/YOK]</td><td>[bulgu/YOK]</td>
  </tr>
</table>

<h2>Veri Akışı Tehditleri</h2>
<table>
  <tr><th>Akış</th><th>Tehdit</th><th>Kategori</th><th>Seviye</th><th>Açıklama</th></tr>
  <!-- Her tehdit için bir satır -->
  <tr class="[seviye]">
    <td>[akış]</td><td>[tehdit]</td><td>[STRIDE]</td>
    <td><span class="tag-[seviye]">[KRİTİK/YÜKSEK/ORTA/DÜŞÜK]</span></td>
    <td>[açıklama]</td>
  </tr>
</table>

<div class="page-break"></div>
<h2>Güven Sınırı İhlalleri</h2>
<!-- Her sınır için -->
<h3>[SINIR_ADI]</h3>
<p><strong>Senaryo:</strong> [açıklama]</p>
<p><strong>Seviye:</strong> <span class="tag-[seviye]">[SEVİYE]</span></p>
<p><strong>Saldırı Yolu:</strong> [özet]</p>

<div class="page-break"></div>
<h2>Saldırı Ağaçları</h2>
<!-- Her ağaç için -->
<h3>THREAT-[ID]: [BAŞLIK] — Risk Skoru: [N]</h3>
<pre>
Hedef: [hedef]
├── Yol A: [başlık]
│   ├── A1: [adım] — zorluk: [düşük/orta/yüksek]
│   └── A2: [adım] — zorluk: [düşük/orta/yüksek]
└── Yol B: [başlık]
    └── B1: [adım] — zorluk: [düşük/orta/yüksek]
</pre>

<div class="page-break"></div>
<h2>Tehdit Kaydı</h2>
<table>
  <tr><th>ID</th><th>Başlık</th><th>Varlık</th><th>STRIDE</th>
      <th>Olasılık</th><th>Etki</th><th>Skor</th><th>Seviye</th></tr>
  <!-- Her tehdit için bir satır -->
  <tr class="[seviye]">
    <td>THREAT-[ID]</td><td>[başlık]</td><td>[varlık]</td><td>[kategori]</td>
    <td>[1-5]</td><td>[1-5]</td><td>[skor]</td>
    <td><span class="tag-[seviye]">[SEVİYE]</span></td>
  </tr>
</table>

<div class="disclaimer">
  <strong>Not:</strong> Bu belge Security Assessment Pipeline /sec-threat-model tarafından
  otomatik üretilmiştir. Sağlanan kapsam bilgisine dayanır; kaynak kod veya gerçek sistem
  yapılandırmasını doğrudan analiz etmez. Profesyonel sızma testinin yerini tutmaz.
</div>

</body>
</html>
```

---

## project-requirements.html

`/sec-project-requirements` tarafından Phase 7'de üretilir.

```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>Güvenlik Gereksinimleri — [PROJE_ADI]</title>
  <!-- PAYLAŞILAN CSS BURAYA -->
</head>
<body>

<div class="cover">
  <h1>Güvenlik Gereksinimleri Belgesi</h1>
  <div class="meta">
    <strong>Proje:</strong> [PROJE_ADI]<br>
    <strong>Tarih:</strong> [ISO_TARIH]<br>
    <strong>Hazırlayan:</strong> Security Assessment Pipeline /sec-project-requirements<br>
    <strong>Kapsam:</strong> [hangi skill'ler çalıştı]
  </div>
</div>

<h2>Yönetici Özeti</h2>
<p>
  <strong>Güvenlik Postürü:</strong>
  <span class="posture-[red|amber|green]">[🔴 KIRMIZI | 🟡 SARI | 🟢 YEŞİL]</span>
</p>
<p>[2-3 cümle gerekçe — teknik olmayan okuyucu için]</p>

<h3>Bu Proje Nedir?</h3>
<p>[2 cümle]</p>

<h3>En Önemli 3 Güvenlik Gereksinimi</h3>
<ol>
  <li><strong>[SEC-REQ-001]</strong> [başlık] — [sade açıklama]</li>
  <li><strong>[SEC-REQ-002]</strong> [başlık] — [sade açıklama]</li>
  <li><strong>[SEC-REQ-003]</strong> [başlık] — [sade açıklama]</li>
</ol>

<h3>Özet</h3>
<table>
  <tr><th>Seviye</th><th>Adet</th></tr>
  <tr class="critical"><td><span class="tag-critical">KRİTİK</span></td><td>[N]</td></tr>
  <tr class="high"><td><span class="tag-high">YÜKSEK</span></td><td>[N]</td></tr>
  <tr class="medium"><td><span class="tag-medium">ORTA</span></td><td>[N]</td></tr>
  <tr><td>DÜŞÜK</td><td>[N]</td></tr>
</table>

<div class="page-break"></div>
<h2><span class="tag-critical">KRİTİK</span> Gereksinimler — Risk: 20-25</h2>

<!-- Her kritik gereksinim için -->
<h3>[SEC-REQ-001]: [BAŞLIK]</h3>
<table>
  <tr><th>Risk Skoru</th><td>[N] (KRİTİK)</td><th>Kaynak Bulgular</th><td>[ID'ler]</td></tr>
  <tr><th>Sahip</th><td>[ekip]</td><th>Öncelik</th><td>1 — Kritik</td></tr>
</table>
<p><strong>Gereksinim:</strong> [ne uygulanmalı]</p>
<p><strong>Kabul Kriterleri:</strong></p>
<ul>
  <li>☐ [kriter 1]</li>
  <li>☐ [kriter 2]</li>
</ul>

<div class="page-break"></div>
<h2><span class="tag-high">YÜKSEK</span> Gereksinimler — Risk: 12-19</h2>
<!-- Aynı yapı -->

<div class="page-break"></div>
<h2><span class="tag-medium">ORTA</span> Gereksinimler — Risk: 6-11</h2>
<!-- Aynı yapı, kısa -->

<div class="page-break"></div>
<h2>Gereksinimler Özet Tablosu</h2>
<table>
  <tr><th>ID</th><th>Başlık</th><th>Kaynak</th><th>Risk</th><th>Seviye</th><th>Sahip</th></tr>
  <!-- Her gereksinim için bir satır — class: critical / high / medium -->
  <tr class="[seviye]">
    <td>[SEC-REQ-xxx]</td><td>[başlık]</td><td>[kaynak]</td>
    <td>[skor]</td><td><span class="tag-[seviye]">[SEVİYE]</span></td><td>[sahip]</td>
  </tr>
</table>

<h2>Değerlendirme Kapsamı</h2>
<table>
  <tr><th>Skill</th><th>Durum</th></tr>
  <tr><td>/sec-threat-model</td><td>[Yüklendi / Eksik]</td></tr>
  <tr><td>/sec-owasp</td><td>[Yüklendi / Eksik]</td></tr>
  <tr><td>/sec-regulatory</td><td>[Yüklendi / Eksik]</td></tr>
  <tr><td>/sec-igrc</td><td>[Yüklendi / Eksik]</td></tr>
</table>

<div class="disclaimer">
  <strong>Not:</strong> Bu belge Security Assessment Pipeline /sec-project-requirements tarafından
  otomatik üretilmiştir. Tehdit modeli, OWASP analizi, mevzuat uyum ve iç kontrol
  değerlendirme bulgularına dayanır. Profesyonel sızma testi ve bağımsız güvenlik
  denetiminin yerini tutmaz.
</div>

</body>
</html>
```

---

## Artifact Üretim Talimatı

- Şablondaki tüm `[PLACEHOLDER]` değerlerini gerçek içerikle doldur.
- Satır class'larını (`critical`, `high`, `medium`, `low`) gerçek seviyeye göre uygula.
- Postür class'ını (`posture-red`, `posture-amber`, `posture-green`) sonuca göre uygula.
- Paylaşılan CSS'i `<style>` tag'leri içinde `<head>`'e ekle.
- Template comment'lerini kaldır.
- Artifact type: `text/html`

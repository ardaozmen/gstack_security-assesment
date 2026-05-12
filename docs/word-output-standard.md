# Word Output Standard

LLM, `Write` aracını kullanarak aşağıdaki HTML şablonlarını doğrudan üretir.
Microsoft Word `.html` dosyalarını natively açar — Python, script veya UI değişikliği gerekmez.

---

## Shared CSS

Her iki HTML dosyasının `<head>` bölümüne eklenir:

```html
<style>
  body {
    font-family: Calibri, sans-serif;
    font-size: 11pt;
    color: #212121;
    margin: 2.5cm 2.5cm 2.5cm 3cm;
    line-height: 1.4;
  }
  h1 {
    font-size: 18pt;
    color: #1F3864;
    font-weight: bold;
    border-bottom: 2px solid #1F3864;
    padding-bottom: 6px;
    margin-top: 0;
  }
  h2 {
    font-size: 14pt;
    color: #2E5496;
    font-weight: bold;
    margin-top: 24px;
  }
  h3 {
    font-size: 12pt;
    color: #2E5496;
    margin-top: 16px;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 10pt;
  }
  th {
    background-color: #1F3864;
    color: #FFFFFF;
    font-weight: bold;
    padding: 6px 8px;
    text-align: left;
    border: 1px solid #1F3864;
  }
  td {
    padding: 5px 8px;
    border: 1px solid #CCCCCC;
    vertical-align: top;
  }
  tr.p0 { background-color: #FFE0E0; }
  tr.p1 { background-color: #FFF3CD; }
  tr.p2 { background-color: #E8F5E9; }
  tr.critical { background-color: #FFE0E0; }
  tr.high     { background-color: #FFF3CD; }
  tr.medium   { background-color: #FFF9C4; }
  tr.low      { background-color: #E8F5E9; }
  .posture-red    { color: #C62828; font-weight: bold; font-size: 13pt; }
  .posture-amber  { color: #E65100; font-weight: bold; font-size: 13pt; }
  .posture-green  { color: #2E7D32; font-weight: bold; font-size: 13pt; }
  .disclaimer {
    background-color: #FFF9C4;
    border: 1px solid #F9A825;
    padding: 10px 14px;
    font-size: 10pt;
    margin-top: 32px;
    color: #555;
  }
  .cover {
    text-align: center;
    padding: 60px 0 40px;
    border-bottom: 3px solid #1F3864;
    margin-bottom: 32px;
  }
  .cover h1 { border: none; font-size: 24pt; }
  .cover .meta { font-size: 11pt; color: #555; margin-top: 16px; line-height: 1.8; }
  .tag-blocker { background: #C62828; color: #fff; padding: 2px 6px; border-radius: 3px; font-size: 9pt; }
  .tag-high    { background: #E65100; color: #fff; padding: 2px 6px; border-radius: 3px; font-size: 9pt; }
  .tag-medium  { background: #F9A825; color: #fff; padding: 2px 6px; border-radius: 3px; font-size: 9pt; }
  pre, code {
    font-family: Consolas, "Courier New", monospace;
    font-size: 9pt;
    background: #F5F5F5;
    border: 1px solid #E0E0E0;
    padding: 8px;
    display: block;
    white-space: pre-wrap;
  }
  .page-break { page-break-before: always; }
</style>
```

---

## threat-modeling.html

Produced by `/sec-threat-model` in Phase 7. Saved to `threat-modeling.html`.

### Document Structure

```
1. Cover
2. Executive Summary
3. Scope Reference
4. STRIDE Component Matrix
5. Data Flow Threats
6. Trust Boundary Violations
7. Attack Trees
8. Threat Register (full table)
9. Disclaimer
```

### Full HTML Template

```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>Threat Model — [PROJECT_NAME]</title>
  <!-- INSERT SHARED CSS HERE -->
</head>
<body>

<!-- COVER -->
<div class="cover">
  <h1>Threat Model Report</h1>
  <div class="meta">
    <strong>Proje:</strong> [PROJECT_NAME]<br>
    <strong>Tarih:</strong> [ISO_DATE]<br>
    <strong>Metodoloji:</strong> STRIDE<br>
    <strong>Hazırlayan:</strong> SecOps Pipeline /sec-threat-model<br>
    <strong>Kaynak:</strong> SCOPE.md
  </div>
</div>

<!-- EXECUTIVE SUMMARY -->
<h2>Yönetici Özeti</h2>
<p>[2–3 cümle: en kritik tehditler, genel risk seviyesi, önerilen öncelikli aksiyon]</p>

<table>
  <tr>
    <th>Toplam Tehdit</th>
    <th>Kritik</th>
    <th>Yüksek</th>
    <th>Orta</th>
    <th>Düşük</th>
  </tr>
  <tr>
    <td>[N]</td>
    <td class="p0">[N]</td>
    <td class="p1">[N]</td>
    <td>[N]</td>
    <td>[N]</td>
  </tr>
</table>

<!-- SCOPE REFERENCE -->
<h2>Kapsam Referansı</h2>
<p><em>Kaynak: SCOPE.md — kısa özet</em></p>
<ul>
  <li><strong>Uygulama ve Servisler:</strong> [liste]</li>
  <li><strong>Veri Depoları:</strong> [liste]</li>
  <li><strong>Güven Sınırları:</strong> [liste]</li>
  <li><strong>Hassas Veri Kategorileri:</strong> [liste]</li>
</ul>

<!-- STRIDE MATRIX -->
<div class="page-break"></div>
<h2>STRIDE Bileşen Tehdit Matrisi</h2>
<table>
  <tr>
    <th>Varlık</th>
    <th>Spoofing</th>
    <th>Tampering</th>
    <th>Repudiation</th>
    <th>Info Disclosure</th>
    <th>DoS</th>
    <th>EoP</th>
  </tr>
  <!-- REPEAT FOR EACH ASSET -->
  <tr class="[critical|high|medium|low]">
    <td>[asset_name]</td>
    <td>[bulgu veya N/A]</td>
    <td>[bulgu veya N/A]</td>
    <td>[bulgu veya N/A]</td>
    <td>[bulgu veya N/A]</td>
    <td>[bulgu veya N/A]</td>
    <td>[bulgu veya N/A]</td>
  </tr>
</table>

<!-- DATA FLOW THREATS -->
<h2>Veri Akışı Tehditleri</h2>
<table>
  <tr>
    <th>Akış</th>
    <th>Tehdit</th>
    <th>Kategori</th>
    <th>Seviye</th>
    <th>Açıklama</th>
  </tr>
  <!-- REPEAT FOR EACH THREAT -->
  <tr class="[critical|high|medium|low]">
    <td>[flow_name]</td>
    <td>[threat_title]</td>
    <td>[STRIDE_category]</td>
    <td><span class="tag-[blocker|high|medium]">[CRITICAL|HIGH|MEDIUM|LOW]</span></td>
    <td>[description]</td>
  </tr>
</table>

<!-- TRUST BOUNDARY VIOLATIONS -->
<div class="page-break"></div>
<h2>Güven Sınırı İhlalleri</h2>
<!-- REPEAT FOR EACH BOUNDARY -->
<h3>[BOUNDARY_NAME]</h3>
<p><strong>Senaryo:</strong> [description]</p>
<p><strong>Seviye:</strong> <span class="tag-[blocker|high|medium]">[CRITICAL|HIGH|MEDIUM|LOW]</span></p>
<p><strong>Saldırı Yolu:</strong> [brief_path]</p>

<!-- ATTACK TREES -->
<div class="page-break"></div>
<h2>Saldırı Ağaçları</h2>
<!-- REPEAT FOR EACH TREE (score >= 12) -->
<h3>THREAT-[ID]: [TITLE] — Risk Skoru: [SCORE]</h3>
<pre>
Hedef: [goal]
├── Yol A: [path_a_title]
│   ├── A1: [step] — zorluk: [düşük/orta/yüksek]
│   └── A2: [step] — zorluk: [düşük/orta/yüksek]
└── Yol B: [path_b_title]
    └── B1: [step] — zorluk: [düşük/orta/yüksek]
</pre>

<!-- FULL THREAT REGISTER -->
<div class="page-break"></div>
<h2>Tehdit Kaydı</h2>
<table>
  <tr>
    <th>ID</th>
    <th>Başlık</th>
    <th>Varlık</th>
    <th>STRIDE</th>
    <th>Olasılık</th>
    <th>Etki</th>
    <th>Skor</th>
    <th>Seviye</th>
  </tr>
  <!-- REPEAT FOR EACH THREAT -->
  <tr class="[critical|high|medium|low]">
    <td>THREAT-[ID]</td>
    <td>[title]</td>
    <td>[asset]</td>
    <td>[category]</td>
    <td>[1-5]</td>
    <td>[1-5]</td>
    <td>[score]</td>
    <td><span class="tag-[blocker|high|medium]">[LEVEL]</span></td>
  </tr>
</table>

<!-- DISCLAIMER -->
<div class="disclaimer">
  <strong>Önemli Not:</strong> Bu belge SecOps Pipeline /sec-threat-model tarafından otomatik üretilmiştir.
  Tehdit modeli, sağlanan kapsam bilgisine dayanır; gerçek sistem yapılandırmasını veya kaynak kodunu
  doğrudan analiz etmez. Bu değerlendirme, profesyonel sızma testi ve red team egzersizlerinin yerine
  geçmez. Nihai güvenlik kararları yetkili uzmanlar tarafından verilmelidir.
</div>

</body>
</html>
```

---

## project-requirements.html

Produced by `/sec-project-requirements` in Phase 7. Saved to `project-requirements.html`.

### Document Structure

```
1. Cover
2. Executive Summary (posture, top 3 reqs, go-live readiness)
3. Assessment Coverage
4. P0 Blockers
5. P1 High Requirements
6. P2 Medium Requirements
7. Full Requirements Table
8. Sign-off Checklist
9. Disclaimer
```

### Full HTML Template

```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>Security Requirements — [PROJECT_NAME]</title>
  <!-- INSERT SHARED CSS HERE -->
</head>
<body>

<!-- COVER -->
<div class="cover">
  <h1>Security Requirements Document</h1>
  <div class="meta">
    <strong>Proje:</strong> [PROJECT_NAME]<br>
    <strong>Tarih:</strong> [ISO_DATE]<br>
    <strong>Hazırlayan:</strong> SecOps Pipeline /sec-project-requirements<br>
    <strong>Değerlendirme Kapsamı:</strong> [which_skills_ran]
  </div>
</div>

<!-- EXECUTIVE SUMMARY -->
<h2>Yönetici Özeti</h2>

<p>
  <strong>Güvenlik Postürü:</strong>
  <span class="posture-[red|amber|green]">[🔴 RED | 🟡 AMBER | 🟢 GREEN]</span>
</p>
<p>[2–3 cümle postür gerekçesi — teknik olmayan okuyucu için]</p>

<h3>Bu Proje Nedir?</h3>
<p>[2 cümle: ne yapar, kim kullanır]</p>

<h3>En Önemli 3 Güvenlik Gereksinimi</h3>
<ol>
  <li><strong>[SEC-REQ-001]</strong> [title] — [plain-language description]</li>
  <li><strong>[SEC-REQ-002]</strong> [title] — [plain-language description]</li>
  <li><strong>[SEC-REQ-003]</strong> [title] — [plain-language description]</li>
</ol>

<h3>Go-Live Hazırlık Özeti</h3>
<table>
  <tr>
    <th>Öncelik</th>
    <th>Adet</th>
    <th>Kapsam</th>
  </tr>
  <tr class="p0">
    <td><span class="tag-blocker">P0 BLOCKER</span></td>
    <td>[N]</td>
    <td>Go-live öncesi çözülmeli</td>
  </tr>
  <tr class="p1">
    <td><span class="tag-high">P1 HIGH</span></td>
    <td>[N]</td>
    <td>30 gün içinde</td>
  </tr>
  <tr class="p2">
    <td><span class="tag-medium">P2 MEDIUM</span></td>
    <td>[N]</td>
    <td>90 gün içinde</td>
  </tr>
</table>

<!-- ASSESSMENT COVERAGE -->
<div class="page-break"></div>
<h2>Değerlendirme Kapsamı</h2>
<table>
  <tr>
    <th>Skill</th>
    <th>Durum</th>
    <th>Çıktı</th>
  </tr>
  <tr><td>/sec-threat-model</td><td>[Yüklendi / Eksik]</td><td>THREAT_MODEL.md</td></tr>
  <tr><td>/sec-owasp</td><td>[Yüklendi / Eksik]</td><td>OWASP_FINDINGS.md</td></tr>
  <tr><td>/sec-regulatory</td><td>[Yüklendi / Eksik]</td><td>REGULATORY_FINDINGS.md</td></tr>
  <tr><td>/sec-igrc</td><td>[Yüklendi / Eksik]</td><td>IGRC_FINDINGS.md</td></tr>
</table>

<!-- P0 BLOCKERS -->
<div class="page-break"></div>
<h2><span class="tag-blocker">P0</span> Blocker'lar — Go-live Öncesi Çözülmeli</h2>

<!-- REPEAT FOR EACH P0 -->
<h3>[SEC-REQ-001]: [TITLE]</h3>
<table>
  <tr><th>Risk Skoru</th><td class="p0">[N] (CRITICAL)</td><th>Kaynak Bulgular</th><td>[IDs]</td></tr>
  <tr><th>Sahip</th><td>[team]</td><th>Hedef Tarih</th><td>Go-live öncesi</td></tr>
  <tr><th>Regulatory Ceza</th><td>[YES | NO | UNCLEAR]</td><th></th><td></td></tr>
</table>
<p><strong>Gereksinim:</strong> [what must be implemented]</p>
<p><strong>Kabul Kriterleri:</strong></p>
<ul>
  <li>☐ [criterion 1]</li>
  <li>☐ [criterion 2]</li>
  <li>☐ [criterion 3]</li>
</ul>

<!-- P1 HIGH -->
<div class="page-break"></div>
<h2><span class="tag-high">P1</span> Yüksek Öncelikli — 30 Gün İçinde</h2>

<!-- REPEAT FOR EACH P1 (same structure as P0) -->
<h3>[SEC-REQ-xxx]: [TITLE]</h3>
<table>
  <tr><th>Risk Skoru</th><td class="p1">[N] (HIGH)</td><th>Kaynak Bulgular</th><td>[IDs]</td></tr>
  <tr><th>Sahip</th><td>[team]</td><th>Hedef Tarih</th><td>+30 gün</td></tr>
</table>
<p><strong>Gereksinim:</strong> [what must be implemented]</p>
<p><strong>Kabul Kriterleri:</strong></p>
<ul>
  <li>☐ [criterion 1]</li>
  <li>☐ [criterion 2]</li>
</ul>

<!-- P2 MEDIUM -->
<div class="page-break"></div>
<h2><span class="tag-medium">P2</span> Orta Öncelikli — 90 Gün İçinde</h2>

<!-- REPEAT FOR EACH P2 (abbreviated) -->
<h3>[SEC-REQ-xxx]: [TITLE]</h3>
<table>
  <tr><th>Risk Skoru</th><td>[N] (MEDIUM)</td><th>Kaynak Bulgular</th><td>[IDs]</td></tr>
  <tr><th>Sahip</th><td>[team]</td><th>Hedef Tarih</th><td>+90 gün</td></tr>
</table>
<p><strong>Gereksinim:</strong> [what must be implemented]</p>

<!-- FULL REQUIREMENTS TABLE -->
<div class="page-break"></div>
<h2>Gereksinimler Özet Tablosu</h2>
<table>
  <tr>
    <th>ID</th>
    <th>Başlık</th>
    <th>Kaynak</th>
    <th>Risk Skoru</th>
    <th>Seviye</th>
    <th>Öncelik</th>
    <th>Sahip</th>
    <th>Tarih</th>
  </tr>
  <!-- REPEAT FOR EACH REQUIREMENT -->
  <tr class="[p0|p1|p2]">
    <td>[SEC-REQ-xxx]</td>
    <td>[title]</td>
    <td>[source_ids]</td>
    <td>[score]</td>
    <td>[CRITICAL|HIGH|MEDIUM|LOW]</td>
    <td><span class="tag-[blocker|high|medium]">[P0|P1|P2]</span></td>
    <td>[team]</td>
    <td>[date]</td>
  </tr>
</table>

<!-- SIGN-OFF CHECKLIST -->
<div class="page-break"></div>
<h2>İmza Kontrol Listesi</h2>
<table>
  <tr>
    <th>Gereksinim ID</th>
    <th>Başlık</th>
    <th>Öncelik</th>
    <th>Sahip</th>
    <th>Tamamlandı</th>
    <th>Tarih</th>
  </tr>
  <!-- REPEAT FOR P0 ONLY -->
  <tr class="p0">
    <td>[SEC-REQ-xxx]</td>
    <td>[title]</td>
    <td><span class="tag-blocker">P0</span></td>
    <td>[team]</td>
    <td>☐</td>
    <td>_____________</td>
  </tr>
</table>

<!-- DISCLAIMER -->
<div class="disclaimer">
  <strong>Önemli Not:</strong> Bu belge SecOps Pipeline /sec-project-requirements tarafından otomatik
  üretilmiştir. Gereksinimler; tehdit modeli, OWASP analizi, mevzuat uyum ve iç kontrol değerlendirme
  bulgularına dayanır. Bu belge, profesyonel sızma testi ve bağımsız güvenlik denetiminin yerine geçmez.
  Go-live kararı ve nihai imza /sec-signoff çıktısındaki yetkili imzacılara aittir.
</div>

</body>
</html>
```

---

## LLM Instructions (for Phase 7 in both skills)

1. Use the template above for the respective document.
2. Replace all `[PLACEHOLDER]` values with actual content from the assessment.
3. Apply row classes (`p0`, `p1`, `p2`, `critical`, `high`, `medium`, `low`) based on actual severity/priority.
4. Apply `posture-red`, `posture-amber`, or `posture-green` class based on Gate result.
5. Insert the Shared CSS block inside `<style>` tags in `<head>`.
6. Remove template comments (`<!-- REPEAT ... -->`, `<!-- INSERT ... -->`).
7. Use the `Write` tool to save the file.
8. The file opens directly in Microsoft Word via File → Open.

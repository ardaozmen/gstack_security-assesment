# Word Output Standard — Claude Web

The LLM produces the HTML templates below **as artifacts**.
Microsoft Word opens `.html` files natively.

Both artifacts use the **same CSS** — defined below.

---

## Shared CSS

Insert inside `<style>` tags in `<head>` of each HTML artifact:

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

Produced by `/sec-threat-model` in Step 7.
Section headings and content should be written in the user's language.

```html
<!DOCTYPE html>
<html lang="[USER_LANGUAGE_CODE]">
<head>
  <meta charset="UTF-8">
  <title>Threat Model — [PROJECT_NAME]</title>
  <!-- INSERT SHARED CSS HERE -->
</head>
<body>

<div class="cover">
  <h1>Threat Model Report</h1>
  <div class="meta">
    <strong>[Project label]:</strong> [PROJECT_NAME]<br>
    <strong>[Date label]:</strong> [ISO_DATE]<br>
    <strong>[Methodology label]:</strong> STRIDE<br>
    <strong>[Prepared by label]:</strong> Security Assessment Pipeline /sec-threat-model
  </div>
</div>

<h2>[Executive Summary heading]</h2>
<p>[2–3 sentences: most critical threats, overall risk level, recommended priority action]</p>

<table>
  <tr><th>[Total]</th><th>[Critical]</th><th>[High]</th><th>[Medium]</th><th>[Low]</th></tr>
  <tr><td>[N]</td><td>[N]</td><td>[N]</td><td>[N]</td><td>[N]</td></tr>
</table>

<h2>[Scope Reference heading]</h2>
<ul>
  <li><strong>[Applications label]:</strong> [list]</li>
  <li><strong>[Data Stores label]:</strong> [list]</li>
  <li><strong>[Trust Boundaries label]:</strong> [list]</li>
  <li><strong>[Sensitive Data label]:</strong> [list]</li>
</ul>

<div class="page-break"></div>
<h2>[STRIDE Matrix heading]</h2>
<table>
  <tr>
    <th>[Asset]</th><th>Spoofing</th><th>Tampering</th>
    <th>Repudiation</th><th>Info Disclosure</th><th>DoS</th><th>EoP</th>
  </tr>
  <!-- One row per asset — class: critical / high / medium / low -->
  <tr class="[level]">
    <td>[asset]</td><td>[finding/N/A]</td><td>[finding/N/A]</td>
    <td>[finding/N/A]</td><td>[finding/N/A]</td><td>[finding/N/A]</td><td>[finding/N/A]</td>
  </tr>
</table>

<h2>[Data Flow Threats heading]</h2>
<table>
  <tr><th>[Flow]</th><th>[Threat]</th><th>[Category]</th><th>[Level]</th><th>[Description]</th></tr>
  <!-- One row per threat -->
  <tr class="[level]">
    <td>[flow]</td><td>[threat]</td><td>[STRIDE]</td>
    <td><span class="tag-[level]">[CRITICAL/HIGH/MEDIUM/LOW]</span></td>
    <td>[description]</td>
  </tr>
</table>

<div class="page-break"></div>
<h2>[Trust Boundary Violations heading]</h2>
<!-- One block per boundary -->
<h3>[BOUNDARY_NAME]</h3>
<p><strong>[Scenario label]:</strong> [description]</p>
<p><strong>[Level label]:</strong> <span class="tag-[level]">[LEVEL]</span></p>
<p><strong>[Attack path label]:</strong> [brief]</p>

<div class="page-break"></div>
<h2>[Attack Trees heading]</h2>
<!-- One block per tree -->
<h3>THREAT-[ID]: [TITLE] — [Risk Score label]: [N]</h3>
<pre>
[Goal label]: [goal]
├── [Path A label]: [title]
│   ├── A1: [step] — [difficulty label]: [low/medium/high]
│   └── A2: [step] — [difficulty label]: [low/medium/high]
└── [Path B label]: [title]
    └── B1: [step] — [difficulty label]: [low/medium/high]
</pre>

<div class="page-break"></div>
<h2>[Threat Register heading]</h2>
<table>
  <tr><th>ID</th><th>[Title]</th><th>[Asset]</th><th>STRIDE</th>
      <th>[Likelihood]</th><th>[Impact]</th><th>[Score]</th><th>[Level]</th></tr>
  <!-- One row per threat -->
  <tr class="[level]">
    <td>THREAT-[ID]</td><td>[title]</td><td>[asset]</td><td>[category]</td>
    <td>[1-5]</td><td>[1-5]</td><td>[score]</td>
    <td><span class="tag-[level]">[LEVEL]</span></td>
  </tr>
</table>

<div class="disclaimer">
  [Disclaimer in user's language: this document was automatically produced by the Security Assessment Pipeline /sec-threat-model, based on the provided scope information; it does not directly analyze source code or real system configuration; it is not a substitute for professional penetration testing.]
</div>

</body>
</html>
```

---

## project-requirements.html

Produced by `/sec-project-requirements` in Step 7.
Section headings and content should be written in the user's language.

```html
<!DOCTYPE html>
<html lang="[USER_LANGUAGE_CODE]">
<head>
  <meta charset="UTF-8">
  <title>Security Requirements — [PROJECT_NAME]</title>
  <!-- INSERT SHARED CSS HERE -->
</head>
<body>

<div class="cover">
  <h1>Security Requirements Document</h1>
  <div class="meta">
    <strong>[Project label]:</strong> [PROJECT_NAME]<br>
    <strong>[Date label]:</strong> [ISO_DATE]<br>
    <strong>[Prepared by label]:</strong> Security Assessment Pipeline /sec-project-requirements<br>
    <strong>[Coverage label]:</strong> [which skills ran]
  </div>
</div>

<h2>[Executive Summary heading]</h2>
<p>
  <strong>[Security Posture label]:</strong>
  <span class="posture-[red|amber|green]">[🔴 RED | 🟡 AMBER | 🟢 GREEN]</span>
</p>
<p>[2–3 sentence rationale — for a non-technical reader]</p>

<h3>[What does this project do? heading]</h3>
<p>[2 sentences]</p>

<h3>[Top 3 Requirements heading]</h3>
<ol>
  <li><strong>[SEC-REQ-001]</strong> [title] — [plain description]</li>
  <li><strong>[SEC-REQ-002]</strong> [title] — [plain description]</li>
  <li><strong>[SEC-REQ-003]</strong> [title] — [plain description]</li>
</ol>

<h3>[Summary heading]</h3>
<table>
  <tr><th>[Level]</th><th>[Count]</th></tr>
  <tr class="critical"><td><span class="tag-critical">CRITICAL</span></td><td>[N]</td></tr>
  <tr class="high"><td><span class="tag-high">HIGH</span></td><td>[N]</td></tr>
  <tr class="medium"><td><span class="tag-medium">MEDIUM</span></td><td>[N]</td></tr>
  <tr><td>LOW</td><td>[N]</td></tr>
</table>

<div class="page-break"></div>
<h2><span class="tag-critical">CRITICAL</span> [Requirements heading] — Risk: 20–25</h2>

<!-- One block per critical requirement -->
<h3>[SEC-REQ-001]: [TITLE]</h3>
<table>
  <tr><th>[Risk Score]</th><td>[N] (CRITICAL)</td><th>[Source Findings]</th><td>[IDs]</td></tr>
  <tr><th>[Owner]</th><td>[team]</td><th>[Priority]</th><td>1 — Critical</td></tr>
</table>
<p><strong>[Requirement label]:</strong> [what must be implemented]</p>
<p><strong>[Acceptance Criteria label]:</strong></p>
<ul>
  <li>☐ [criterion 1]</li>
  <li>☐ [criterion 2]</li>
</ul>

<div class="page-break"></div>
<h2><span class="tag-high">HIGH</span> [Requirements heading] — Risk: 12–19</h2>
<!-- Same structure -->

<div class="page-break"></div>
<h2><span class="tag-medium">MEDIUM</span> [Requirements heading] — Risk: 6–11</h2>
<!-- Same structure, abbreviated -->

<div class="page-break"></div>
<h2>[Requirements Summary Table heading]</h2>
<table>
  <tr><th>ID</th><th>[Title]</th><th>[Source]</th><th>[Risk]</th><th>[Level]</th><th>[Owner]</th></tr>
  <!-- One row per requirement — class: critical / high / medium -->
  <tr class="[level]">
    <td>[SEC-REQ-xxx]</td><td>[title]</td><td>[source]</td>
    <td>[score]</td><td><span class="tag-[level]">[LEVEL]</span></td><td>[owner]</td>
  </tr>
</table>

<h2>[Assessment Coverage heading]</h2>
<table>
  <tr><th>[Skill]</th><th>[Status]</th></tr>
  <tr><td>/sec-threat-model</td><td>[Loaded / Missing]</td></tr>
  <tr><td>/sec-owasp</td><td>[Loaded / Missing]</td></tr>
  <tr><td>/sec-regulatory</td><td>[Loaded / Missing]</td></tr>
  <tr><td>/sec-igrc</td><td>[Loaded / Missing]</td></tr>
</table>

<div class="disclaimer">
  [Disclaimer in user's language: this document was automatically produced by the Security Assessment Pipeline /sec-project-requirements, based on threat model, OWASP analysis, regulatory compliance, and internal control findings; it is not a substitute for professional penetration testing or independent security audit.]
</div>

</body>
</html>
```

---

## Artifact Generation Instructions

- Replace all `[PLACEHOLDER]` values with actual content from the analysis.
- Write all section headings and content in the user's language.
- Apply row classes (`critical`, `high`, `medium`, `low`) based on actual levels.
- Apply posture class (`posture-red`, `posture-amber`, `posture-green`) based on result.
- Insert the Shared CSS block inside `<style>` tags in `<head>`.
- Remove all template comments and placeholder labels.
- Artifact type: `text/html`

# Pipeline Modes

## Mode Matrix

| Mod | Adımlar | Amaç |
|---|---|---|
| `full` | `/sec-scope` → `/sec-threat-model` → `/sec-owasp` ‖ `/sec-regulatory` → `/sec-igrc` → `/sec-risk-report` → `/sec-signoff` | Tam degerlendirme |
| `fast` | `/sec-scope` → `/sec-owasp` → `/sec-risk-report` | Hizli teknik risk resmi |
| `compliance` | `/sec-scope` → `/sec-regulatory` → `/sec-igrc` → `/sec-risk-report` → `/sec-signoff` | Mevzuat odakli denetim |
| `resume` | Son FAIL adimindan devam | Yarida kalan kosuyu surdur |

### Full Mode — Paralel Akış

```
/sec-scope
      │
      ▼
/sec-threat-model
 ┌────┴──────────────────┐
 ▼                        ▼
/sec-owasp       /sec-regulatory
 │                        │
 │                   /sec-igrc
 │                        │
 └──────────┬─────────────┘
            ▼
   /sec-risk-report
            │
            ▼
     /sec-signoff
```

## Parametreler

- `mode=<full|fast|compliance>`
- `retry_from=<skill_id>` — örn. `retry_from=sec-owasp`
- `force_refresh=<true|false>`

## Örnekler

- `/sec-autoplan`
- `/sec-autoplan mode=fast`
- `/sec-autoplan mode=compliance force_refresh=true`
- `/sec-autoplan resume`
- `/sec-autoplan retry_from=sec-owasp`

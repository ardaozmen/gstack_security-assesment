# Pipeline Modes

## Mode Matrix

| Mod | Adımlar |
|---|---|
| `full` | `/sec-scope` → `/sec-threat-model` → `/sec-owasp` ‖ `/sec-regulatory` → `/sec-igrc` → `/sec-project-requirements` → `/sec-signoff` |
| `fast` | `/sec-scope` → `/sec-owasp` → `/sec-project-requirements` |
| `compliance` | `/sec-scope` → `/sec-regulatory` → `/sec-igrc` → `/sec-project-requirements` → `/sec-signoff` |
| `resume` | Son FAIL adimindan devam |

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
/sec-project-requirements
            │
            ▼
     /sec-signoff
```

### Post-Pipeline (opsiyonel)

```
/sec-signoff bittikten sonra:

/sec-retro   ← cross-project learnings, geçmişle karşılaştırma
```

## Parametreler

- `mode=<full|fast|compliance>`
- `retry_from=<skill_id>` — örn. `retry_from=sec-owasp`
- `force_refresh=<true|false>`

## Örnekler

- `/security-assessment`
- `/security-assessment mode=fast`
- `/security-assessment mode=compliance force_refresh=true`
- `/security-assessment resume`
- `/security-assessment retry_from=sec-owasp`
- `/sec-retro`

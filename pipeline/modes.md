# Pipeline Modes

## Mode Matrix

| Mode | Steps | Amaç |
|---|---|---|
| `full` | `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7` | Tam degerlendirme |
| `fast` | `1 -> 3 -> 6` | Hizli teknik risk resmi |
| `compliance` | `1 -> 4 -> 5 -> 6 -> 7` | Mevzuat odakli denetim |
| `resume` | Son FAIL adimindan devam | Yarida kalan kosuyu surdur |

## Parametreler

- `mode=<full|fast|compliance>`
- `retry_from=<step_no>`
- `force_refresh=<true|false>`

## Ornekler

- `/sec-autoplan`
- `/sec-autoplan mode=fast`
- `/sec-autoplan mode=compliance force_refresh=true`
- `/sec-autoplan resume`
- `/sec-autoplan retry_from=3`


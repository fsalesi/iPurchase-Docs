# INQUIRY_NOTES_MATCHES - iPurchase System Setting

**Category:** Reporting & Inquiry

When searching requisitions by using the notes field, use 'matches' vs 'contains', matches can be much slower but more flexible.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INQUIRY_NOTES_MATCHES |
| **Category** | Reporting & Inquiry |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_NOTES_MATCHES'
```
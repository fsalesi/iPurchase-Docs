# UP_ONLY_APP_LEVEL_EXCLUDED - iPurchase System Setting

**Category:** Change Orders

Comma-separated approval levels. Approval levels to exclude from UP_ONLY rule evaluation.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | UP_ONLY_APP_LEVEL_EXCLUDED |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UP_ONLY_APP_LEVEL_EXCLUDED'
```

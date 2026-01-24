# QX_CODEPAGE - iPurchase System Setting

**Category:** Qxtend Integration

Character encoding for Qxtend communication.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QX_CODEPAGE |
| **Category** | Qxtend Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QX_CODEPAGE'
```

# TERMS_DISPLAY - iPurchase System Setting

**Category:** Uncategorized

This setting will display the supplier terms on the requisition header.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TERMS_DISPLAY |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TERMS_DISPLAY'
```

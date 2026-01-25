# NUMERIC_FORMAT_SEPARATOR - iPurchase System Setting

**Category:** Uncategorized

Usually a comma

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NUMERIC_FORMAT_SEPARATOR |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | , |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NUMERIC_FORMAT_SEPARATOR'
```

### Related Settings

- [NUMERIC_FORMAT_DECIMAL](NUMERIC_FORMAT_DECIMAL.md)
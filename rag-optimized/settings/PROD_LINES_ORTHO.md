# PROD_LINES_ORTHO - iPurchase System Setting

**Category:** Custom/Product Management

Product line categorization for Ortho business unit.

### How It Works

This setting configures custom/product management behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PROD_LINES_ORTHO |
| **Category** | Custom/Product Management |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PROD_LINES_ORTHO'
```

### Related Settings

- [PROD_LINES_DERMIS](PROD_LINES_DERMIS.md)
- [PROD_LINES_WOUND_CARE](PROD_LINES_WOUND_CARE.md)

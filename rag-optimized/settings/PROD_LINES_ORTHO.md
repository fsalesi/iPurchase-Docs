# PROD_LINES_ORTHO - iPurchase System Setting

**Category:** Custom/Product Management

Product line categorization for Ortho business unit. Customer-specific.

### How It Works

See the description above for valid values and usage.

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

# PROD_LINES_WOUND_CARE - iPurchase System Setting

**Category:** Custom/Product Management

Product line categorization for Wound Care business unit. Customer-specific.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PROD_LINES_WOUND_CARE |
| **Category** | Custom/Product Management |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PROD_LINES_WOUND_CARE'
```
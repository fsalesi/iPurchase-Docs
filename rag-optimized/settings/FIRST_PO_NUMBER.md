# FIRST_PO_NUMBER - iPurchase System Setting

**Category:** Purchase Orders

Numeric.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | FIRST_PO_NUMBER |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | 1 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'FIRST_PO_NUMBER'
```
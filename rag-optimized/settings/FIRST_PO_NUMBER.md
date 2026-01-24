# FIRST_PO_NUMBER - iPurchase System Setting

**Category:** Purchase Orders

Numeric. Starting purchase order number for sequential PO numbering.

### How It Works

See the description above for details on how this setting affects system behavior.

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
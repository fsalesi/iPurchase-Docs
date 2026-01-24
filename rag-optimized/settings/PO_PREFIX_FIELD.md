# PO_PREFIX_FIELD - iPurchase System Setting

**Category:** Purchase Orders

Can be either 'Entity' or any fields on the requisition header table. This will allow you to create different prefix or number scheme for different sites

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PREFIX_FIELD |
| **Category** | Purchase Orders |
| **Owner** | entities |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PREFIX_FIELD'
```

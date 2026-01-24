# PO_SIGNATURE_ON_REPRINT - iPurchase System Setting

**Category:** Purchase Orders

This setting allows the administrator to print a signature on a reprint of a Purchase Order.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_SIGNATURE_ON_REPRINT |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_SIGNATURE_ON_REPRINT'
```

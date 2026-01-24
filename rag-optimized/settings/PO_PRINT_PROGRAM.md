# PO_PRINT_PROGRAM - iPurchase System Setting

**Category:** Purchase Orders

Progress program If you have a custom purchase order print program then enter the Progress program name here.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_PROGRAM |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | us/po/poporp03.p |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_PROGRAM'
```

# PO_BLANKET_PRINT_PROGRAM - iPurchase System Setting

**Category:** Purchase Orders

QAD program name which prints blankets, should not be modified.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_BLANKET_PRINT_PROGRAM |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | us/po/poblrp03.p |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_BLANKET_PRINT_PROGRAM'
```

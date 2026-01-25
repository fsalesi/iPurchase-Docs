# PO_BLANKET_PRINT_PROGRAM - iPurchase System Setting

**Category:** Purchase Orders

QAD program name which prints blankets, should not be modified.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

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

### Related Settings

- [PO_BREAK_BY](PO_BREAK_BY.md)
- [PO_CONFIRMATION_RESPONSE](PO_CONFIRMATION_RESPONSE.md)
- [PO_DO_NOT_PRINT](PO_DO_NOT_PRINT.md)
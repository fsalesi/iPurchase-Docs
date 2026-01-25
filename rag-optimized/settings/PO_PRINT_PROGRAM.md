# PO_PRINT_PROGRAM - iPurchase System Setting

**Category:** Purchase Orders

Progress program If you have a custom purchase order print program then enter the Progress program name here.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

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

### Related Settings

- [PO_BLANKET_PRINT_PROGRAM](PO_BLANKET_PRINT_PROGRAM.md)
- [PO_BREAK_BY](PO_BREAK_BY.md)
- [PO_CONFIRMATION_RESPONSE](PO_CONFIRMATION_RESPONSE.md)

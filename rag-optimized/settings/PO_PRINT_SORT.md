# PO_PRINT_SORT - iPurchase System Setting

**Category:** Purchase Orders

This setting determines the value which will be used to sort the Purchase Order on the PO Print screen.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_SORT |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | LINE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_SORT'
```

### Related Settings

- [PO_BLANKET_PRINT_PROGRAM](PO_BLANKET_PRINT_PROGRAM.md)
- [PO_BREAK_BY](PO_BREAK_BY.md)
- [PO_CONFIRMATION_RESPONSE](PO_CONFIRMATION_RESPONSE.md)
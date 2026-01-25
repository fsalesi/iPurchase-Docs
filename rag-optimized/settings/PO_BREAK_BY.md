# PO_BREAK_BY - iPurchase System Setting

**Category:** Purchase Orders

Comma separated list of fields on a requisition that will be used to split the requisition into multiple PO's.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_BREAK_BY |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | xxreqd_vendor |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_BREAK_BY'
```

### Related Settings

- [PO_BLANKET_PRINT_PROGRAM](PO_BLANKET_PRINT_PROGRAM.md)
- [PO_CONFIRMATION_RESPONSE](PO_CONFIRMATION_RESPONSE.md)
- [PO_DO_NOT_PRINT](PO_DO_NOT_PRINT.md)

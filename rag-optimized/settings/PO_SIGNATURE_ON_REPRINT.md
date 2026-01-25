# PO_SIGNATURE_ON_REPRINT - iPurchase System Setting

**Category:** Purchase Orders

This setting allows the administrator to print a signature on a reprint of a Purchase Order.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

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

### Related Settings

- [PO_BLANKET_PRINT_PROGRAM](PO_BLANKET_PRINT_PROGRAM.md)
- [PO_BREAK_BY](PO_BREAK_BY.md)
- [PO_CONFIRMATION_RESPONSE](PO_CONFIRMATION_RESPONSE.md)
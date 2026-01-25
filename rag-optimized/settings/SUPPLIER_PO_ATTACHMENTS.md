# SUPPLIER_PO_ATTACHMENTS - iPurchase System Setting

**Category:** Purchase Orders

Comma-Separated List of paths and files.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_PO_ATTACHMENTS |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_PO_ATTACHMENTS'
```

### Related Settings

- [SUPPLIER_PO_MERGE_ATTACHMENTS](SUPPLIER_PO_MERGE_ATTACHMENTS.md)
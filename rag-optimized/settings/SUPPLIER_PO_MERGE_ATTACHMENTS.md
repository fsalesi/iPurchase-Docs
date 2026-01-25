# SUPPLIER_PO_MERGE_ATTACHMENTS - iPurchase System Setting

**Category:** Purchase Orders

This setting is where the filename, with the full path to the pdf file or a space delimited list of pdf files that are to be merged in to the PO PDF file which is printed.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_PO_MERGE_ATTACHMENTS |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_PO_MERGE_ATTACHMENTS'
```

### Related Settings

- [SUPPLIER_PO_ATTACHMENTS](SUPPLIER_PO_ATTACHMENTS.md)

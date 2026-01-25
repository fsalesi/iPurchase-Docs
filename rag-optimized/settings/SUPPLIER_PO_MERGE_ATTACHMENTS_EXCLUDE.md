# SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE - iPurchase System Setting

**Category:** Catalog & Vendors

Comma-separated suppliers.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE'
```

### Related Settings

- [SUPPLIER_CONFIRMATION](SUPPLIER_CONFIRMATION.md)
- [SUPPLIER_SEARCH_MATCHES](SUPPLIER_SEARCH_MATCHES.md)

# SUPPLIER_SEARCH_MATCHES - iPurchase System Setting

**Category:** Catalog & Vendors

If set to True then a user can search for a supplier using any character in the suppliers name.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_SEARCH_MATCHES |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_SEARCH_MATCHES'
```

### Related Settings

- [SUPPLIER_CONFIRMATION](SUPPLIER_CONFIRMATION.md)
- [SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE](SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE.md)

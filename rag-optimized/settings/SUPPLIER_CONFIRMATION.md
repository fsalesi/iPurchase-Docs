# SUPPLIER_CONFIRMATION - iPurchase System Setting

**Category:** Catalog & Vendors

TRUE | FALSE.

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
| **Setting Name** | SUPPLIER_CONFIRMATION |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_CONFIRMATION'
```

### Related Settings

- [SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE](SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE.md)
- [SUPPLIER_SEARCH_MATCHES](SUPPLIER_SEARCH_MATCHES.md)
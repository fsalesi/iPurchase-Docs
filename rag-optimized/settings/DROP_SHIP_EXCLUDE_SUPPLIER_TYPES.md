# DROP_SHIP_EXCLUDE_SUPPLIER_TYPES - iPurchase System Setting

**Category:** Catalog & Vendors

Comma-Separated list of Supplier Types that should not show in the drop ship search.

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DROP_SHIP_EXCLUDE_SUPPLIER_TYPES |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DROP_SHIP_EXCLUDE_SUPPLIER_TYPES'
```
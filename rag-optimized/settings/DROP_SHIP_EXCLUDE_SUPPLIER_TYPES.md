# DROP_SHIP_EXCLUDE_SUPPLIER_TYPES - iPurchase System Setting

**Category:** Catalog & Vendors

Comma-Separated list of Supplier Types that should not show in the drop ship search. For example you may want to exclude employee addresses

### How It Works

See the description above for details on how this setting affects system behavior.

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
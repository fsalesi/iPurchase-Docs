# DROP_SHIP_EXCLUDE_SUPPLIER_TYPES - iPurchase System Setting

**Category:** Catalog & Vendors

Comma-Separated list of Supplier Types that should not show in the drop ship search. For example you may want to exclude employee addresses

**Common questions this answers:**
- What is DROP_SHIP_EXCLUDE_SUPPLIER_TYPES?
- What does DROP_SHIP_EXCLUDE_SUPPLIER_TYPES do?
- What is the default value for DROP_SHIP_EXCLUDE_SUPPLIER_TYPES?
- How do I configure DROP_SHIP_EXCLUDE_SUPPLIER_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DROP_SHIP_EXCLUDE_SUPPLIER_TYPES |
| **Category** | Catalog & Vendors |
| **Owner** |  |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DROP_SHIP_EXCLUDE_SUPPLIER_TYPES'
```

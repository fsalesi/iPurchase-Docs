# CATALOG_EXCEPTION_REQ_TYPE - iPurchase System Setting

**Category:** Catalog & Vendors

If left blank the catalog exception requisition type should be set to "Catalog Exception".

### How It Works

This setting controls catalog functionality, affecting how users browse and select items from supplier catalogs.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_EXCEPTION_REQ_TYPE |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_EXCEPTION_REQ_TYPE'
```

### Related Settings

- [CATALOG_ACCESS_[Supplier NBR]](CATALOG_ACCESS_[Supplier NBR].md)
- [CATALOG_CAN_DELETE](CATALOG_CAN_DELETE.md)
- [CATALOG_CAN_RATE](CATALOG_CAN_RATE.md)
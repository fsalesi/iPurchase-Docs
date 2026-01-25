# CATALOG_DISPLAY_ROWS - iPurchase System Setting

**Category:** Catalog & Vendors

This setting will allow the administrator to decide how many rows of items to display on a catalog requisition.

### How It Works

This setting controls catalog functionality, affecting how users browse and select items from supplier catalogs.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_DISPLAY_ROWS |
| **Category** | Catalog & Vendors |
| **Owner** | Power Users |
| **Default Value** | 25 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_DISPLAY_ROWS'
```

### Related Settings

- [CATALOG_ACCESS_[Supplier NBR]](<CATALOG_ACCESS_[Supplier NBR].md>)
- [CATALOG_CAN_DELETE](CATALOG_CAN_DELETE.md)
- [CATALOG_CAN_RATE](CATALOG_CAN_RATE.md)

# CATALOG_CAN_RATE - iPurchase System Setting

**Category:** Catalog & Vendors

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | users can rate catalog items |
| **FALSE** | Disables this feature |

### How It Works

This setting controls catalog functionality, affecting how users browse and select items from supplier catalogs.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_CAN_RATE |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_CAN_RATE'
```

### Related Settings

- [CATALOG_ACCESS_[Supplier NBR]](CATALOG_ACCESS_[Supplier NBR].md)
- [CATALOG_CAN_DELETE](CATALOG_CAN_DELETE.md)
- [CATALOG_CART_SHOW_DETAILS](CATALOG_CART_SHOW_DETAILS.md)
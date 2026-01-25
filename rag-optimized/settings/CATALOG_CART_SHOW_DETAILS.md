# CATALOG_CART_SHOW_DETAILS - iPurchase System Setting

**Category:** Catalog & Vendors

This setting will show supplier, lead time, manufacturer, and UOM in the cart for a catalog if set to true.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting controls catalog functionality, affecting how users browse and select items from supplier catalogs.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_CART_SHOW_DETAILS |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_CART_SHOW_DETAILS'
```

### Related Settings

- [CATALOG_ACCESS_[Supplier NBR]](<CATALOG_ACCESS_[Supplier NBR].md>)
- [CATALOG_CAN_DELETE](CATALOG_CAN_DELETE.md)
- [CATALOG_CAN_RATE](CATALOG_CAN_RATE.md)

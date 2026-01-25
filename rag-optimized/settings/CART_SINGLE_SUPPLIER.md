# CART_SINGLE_SUPPLIER - iPurchase System Setting

**Category:** Catalog & Vendors

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | shopping cart is restricted to items from a single supplier |
| **FALSE** | Disables this feature |

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CART_SINGLE_SUPPLIER |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CART_SINGLE_SUPPLIER'
```
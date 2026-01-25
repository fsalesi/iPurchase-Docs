# VALIDATE_SUP_ITEM - iPurchase System Setting

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
| **Setting Name** | VALIDATE_SUP_ITEM |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'VALIDATE_SUP_ITEM'
```
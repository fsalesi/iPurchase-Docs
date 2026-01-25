# ITEM_ADD_DESC2_ALLOW_BLANK - iPurchase System Setting

**Category:** Requisitions

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | allows adding catalog items with blank secondary description |
| **FALSE** | Disables this feature |

### How It Works

This permission setting controls whether users can perform specific actions within the system.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ITEM_ADD_DESC2_ALLOW_BLANK |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ITEM_ADD_DESC2_ALLOW_BLANK'
```
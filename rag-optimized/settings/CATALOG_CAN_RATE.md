# CATALOG_CAN_RATE - iPurchase System Setting

**Category:** Catalog & Vendors

TRUE | FALSE. If TRUE, users can rate catalog items. Related: CATALOG_SHOW_RATING

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

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
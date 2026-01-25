# MC_BEFORE_NOTES - iPurchase System Setting

**Category:** Purchase Orders

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | places master comments before line notes on PO |
| **FALSE** | Disables this feature |

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MC_BEFORE_NOTES |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MC_BEFORE_NOTES'
```
# BUYER_MOD - iPurchase System Setting

**Category:** Purchase Orders

TRUE | FALSE. If TRUE, allows the buyer field to be modified during requisition copy and PO creation. If FALSE, buyer field is locked.

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
| **Setting Name** | BUYER_MOD |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUYER_MOD'
```
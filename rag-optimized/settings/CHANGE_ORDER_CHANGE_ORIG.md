# CHANGE_ORDER_CHANGE_ORIG - iPurchase System Setting

**Category:** Change Orders

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | allows changing the originator (xxreq_userid) field on purchase order change orders |
| **FALSE** | Disables this feature |

### How It Works

This setting configures change orders behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CHANGE_ORDER_CHANGE_ORIG |
| **Category** | Change Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CHANGE_ORDER_CHANGE_ORIG'
```
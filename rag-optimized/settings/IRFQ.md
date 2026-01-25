# IRFQ - iPurchase System Setting

**Category:** RFQ Management

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures rfq management behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IRFQ |
| **Category** | RFQ Management |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IRFQ'
```
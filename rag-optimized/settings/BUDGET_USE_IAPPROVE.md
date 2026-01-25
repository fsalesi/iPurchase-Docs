# BUDGET_USE_IAPPROVE - iPurchase System Setting

**Category:** iApprove Integration

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | uses iApprove system for budget workflows instead of iPurchase budget module |
| **FALSE** | Disables this feature |

### How It Works

This setting configures iapprove integration behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_USE_IAPPROVE |
| **Category** | iApprove Integration |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_USE_IAPPROVE'
```
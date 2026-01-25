# BUDGET_HIDE_RECEIPTS - iPurchase System Setting

**Category:** Receiving

Do not show nor use the Receipts column on Budgets.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This display setting controls what information is visible to users in the interface.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_HIDE_RECEIPTS |
| **Category** | Receiving |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_HIDE_RECEIPTS'
```
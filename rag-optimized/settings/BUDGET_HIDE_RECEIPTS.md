# BUDGET_HIDE_RECEIPTS - iPurchase System Setting

**Category:** Receiving

Do not show nor use the Receipts column on Budgets.

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
| **Setting Name** | BUDGET_HIDE_RECEIPTS |
| **Category** | Receiving |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_HIDE_RECEIPTS'
```
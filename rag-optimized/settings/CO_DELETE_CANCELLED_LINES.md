# CO_DELETE_CANCELLED_LINES - iPurchase System Setting

**Category:** Change Orders

TRUE | FALSE. If TRUE, permanently deletes cancelled lines on change orders. If FALSE, lines remain with cancelled status.

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
| **Setting Name** | CO_DELETE_CANCELLED_LINES |
| **Category** | Change Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_DELETE_CANCELLED_LINES'
```
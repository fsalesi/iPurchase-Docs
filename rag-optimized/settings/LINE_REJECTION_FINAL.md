# LINE_REJECTION_FINAL - iPurchase System Setting

**Category:** Uncategorized

If USE_LINE_APPROVALS = TRUE then you can also set whether or not any items which were previously rejected, can be re-approved by a subsequent approver.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LINE_REJECTION_FINAL |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LINE_REJECTION_FINAL'
```
# DISCREPANCY_DELETE_HIDE - iPurchase System Setting

**Category:** Uncategorized

If set to TRUE, will not show deleted items in the discrepancy report

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
| **Setting Name** | DISCREPANCY_DELETE_HIDE |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DISCREPANCY_DELETE_HIDE'
```
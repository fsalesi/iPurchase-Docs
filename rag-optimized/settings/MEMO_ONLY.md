# MEMO_ONLY - iPurchase System Setting

**Category:** Uncategorized

If this setting is true, then a user will not be allowed to order an item# which exists in the part master (pt_mstr) table.

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
| **Setting Name** | MEMO_ONLY |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MEMO_ONLY'
```
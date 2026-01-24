# SHOW_RULE_INFO - iPurchase System Setting

**Category:** Uncategorized

This setting will show the approval rule name when hovering over the Level or Seq field in the Approval History Tab.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SHOW_RULE_INFO |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_RULE_INFO'
```

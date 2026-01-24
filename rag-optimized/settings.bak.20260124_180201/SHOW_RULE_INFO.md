# SHOW_RULE_INFO - iPurchase System Setting

**Category:** Uncategorized

This setting will show the approval rule name when hovering over the Level or Seq field in the Approval History Tab.

**Common questions this answers:**
- What is SHOW_RULE_INFO?
- What does SHOW_RULE_INFO do?
- What is the default value for SHOW_RULE_INFO?
- How do I configure SHOW_RULE_INFO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SHOW_RULE_INFO |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_RULE_INFO'
```

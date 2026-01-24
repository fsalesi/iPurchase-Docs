# AUDIT_TRAIL_ACTION_LIST - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is AUDIT_TRAIL_ACTION_LIST?
- What does AUDIT_TRAIL_ACTION_LIST do?
- What is the default value for AUDIT_TRAIL_ACTION_LIST?
- How do I configure AUDIT_TRAIL_ACTION_LIST?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TRAIL_ACTION_LIST |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | ,Create,Delete,Write |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TRAIL_ACTION_LIST'
```

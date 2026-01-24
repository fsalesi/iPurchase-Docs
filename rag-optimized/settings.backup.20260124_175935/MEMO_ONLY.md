# MEMO_ONLY - iPurchase System Setting

**Category:** Uncategorized

If this setting is true, then a user will not be allowed to order an item# which exists in the part master (pt_mstr) table.

**Common questions this answers:**
- What is MEMO_ONLY?
- What does MEMO_ONLY do?
- What is the default value for MEMO_ONLY?
- How do I configure MEMO_ONLY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MEMO_ONLY |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MEMO_ONLY'
```

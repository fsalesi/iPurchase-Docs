# OOF_LIMIT_BY_DOLLARS - iPurchase System Setting

**Category:** Uncategorized

A setting of True will only allow a user to delegate to another user who has at least the same dollar approval level.

**Common questions this answers:**
- What is OOF_LIMIT_BY_DOLLARS?
- What does OOF_LIMIT_BY_DOLLARS do?
- What is the default value for OOF_LIMIT_BY_DOLLARS?
- How do I configure OOF_LIMIT_BY_DOLLARS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_LIMIT_BY_DOLLARS |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_LIMIT_BY_DOLLARS'
```

# SHOW_ALLOCATION_CODES - iPurchase System Setting

**Category:** Uncategorized

True/false to Show/Hide allocation codes in the account dropdown in req line maintenance.

**Common questions this answers:**
- What is SHOW_ALLOCATION_CODES?
- What does SHOW_ALLOCATION_CODES do?
- What is the default value for SHOW_ALLOCATION_CODES?
- How do I configure SHOW_ALLOCATION_CODES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SHOW_ALLOCATION_CODES |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_ALLOCATION_CODES'
```

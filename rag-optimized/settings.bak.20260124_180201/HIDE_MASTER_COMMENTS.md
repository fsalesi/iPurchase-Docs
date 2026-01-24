# HIDE_MASTER_COMMENTS - iPurchase System Setting

**Category:** Uncategorized

Comma separated list of User ID's or Group ID's that will not get the master comments functionality. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is HIDE_MASTER_COMMENTS?
- What does HIDE_MASTER_COMMENTS do?
- What is the default value for HIDE_MASTER_COMMENTS?
- How do I configure HIDE_MASTER_COMMENTS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | HIDE_MASTER_COMMENTS |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'HIDE_MASTER_COMMENTS'
```

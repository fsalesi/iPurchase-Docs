# LOCK_OUT_MINUTES - iPurchase System Setting

**Category:** Uncategorized

The number of minutes a user will be locked out after failing to login more than the value of setting FAILED_LOGIN_ATTEMPTS

**Common questions this answers:**
- What is LOCK_OUT_MINUTES?
- What does LOCK_OUT_MINUTES do?
- What is the default value for LOCK_OUT_MINUTES?
- How do I configure LOCK_OUT_MINUTES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOCK_OUT_MINUTES |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | 10 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOCK_OUT_MINUTES'
```

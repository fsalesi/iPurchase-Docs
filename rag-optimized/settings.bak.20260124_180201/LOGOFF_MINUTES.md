# LOGOFF_MINUTES - iPurchase System Setting

**Category:** Uncategorized

Enter how many minutes of inactivity the system will wait until it logs a user off.

**Common questions this answers:**
- What is LOGOFF_MINUTES?
- What does LOGOFF_MINUTES do?
- What is the default value for LOGOFF_MINUTES?
- How do I configure LOGOFF_MINUTES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGOFF_MINUTES |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | 0 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGOFF_MINUTES'
```

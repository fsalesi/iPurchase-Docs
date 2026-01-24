# ALLOW_FEEDBACK - iPurchase System Setting

**Category:** User Management

Can-Do list. Users/groups allowed to submit feedback through the application interface.

**Common questions this answers:**
- What is ALLOW_FEEDBACK?
- What does ALLOW_FEEDBACK do?
- What is the default value for ALLOW_FEEDBACK?
- How do I configure ALLOW_FEEDBACK?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_FEEDBACK |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_FEEDBACK'
```

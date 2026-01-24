# ALLOW_BUG - iPurchase System Setting

**Category:** User Management

Can-Do list. Users/groups allowed to submit bug reports through the application interface.

**Common questions this answers:**
- What is ALLOW_BUG?
- What does ALLOW_BUG do?
- What is the default value for ALLOW_BUG?
- How do I configure ALLOW_BUG?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_BUG |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_BUG'
```

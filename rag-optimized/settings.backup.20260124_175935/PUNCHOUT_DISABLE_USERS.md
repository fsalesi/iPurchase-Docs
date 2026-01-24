# PUNCHOUT_DISABLE_USERS - iPurchase System Setting

**Category:** Catalog & Vendors

Can-Do list. Users/groups who are NOT allowed to use punchout functionality.

**Common questions this answers:**
- What is PUNCHOUT_DISABLE_USERS?
- What does PUNCHOUT_DISABLE_USERS do?
- What is the default value for PUNCHOUT_DISABLE_USERS?
- How do I configure PUNCHOUT_DISABLE_USERS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_DISABLE_USERS |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_DISABLE_USERS'
```

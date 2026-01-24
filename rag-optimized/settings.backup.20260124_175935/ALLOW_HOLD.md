# ALLOW_HOLD - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's who are allowed to put a requisition on hold while it is pending. Asterisk indicates everyone, a blank indicates no one. Example: It would go on hold...

**Common questions this answers:**
- What is ALLOW_HOLD?
- What does ALLOW_HOLD do?
- What is the default value for ALLOW_HOLD?
- How do I configure ALLOW_HOLD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_HOLD |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_HOLD'
```

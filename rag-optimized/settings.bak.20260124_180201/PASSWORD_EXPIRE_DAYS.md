# PASSWORD_EXPIRE_DAYS - iPurchase System Setting

**Category:** Security & Authentication

This setting allows the administrator to set how often passwords need to be reset.

**Common questions this answers:**
- What is PASSWORD_EXPIRE_DAYS?
- What does PASSWORD_EXPIRE_DAYS do?
- What is the default value for PASSWORD_EXPIRE_DAYS?
- How do I configure PASSWORD_EXPIRE_DAYS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PASSWORD_EXPIRE_DAYS |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | 45 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PASSWORD_EXPIRE_DAYS'
```

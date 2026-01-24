# FAILED_LOGIN_ATTEMPTS - iPurchase System Setting

**Category:** Security & Authentication

Identifies how many consecutive failed login attempts will be allowed before disabling a user

**Common questions this answers:**
- What is FAILED_LOGIN_ATTEMPTS?
- What does FAILED_LOGIN_ATTEMPTS do?
- What is the default value for FAILED_LOGIN_ATTEMPTS?
- How do I configure FAILED_LOGIN_ATTEMPTS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | FAILED_LOGIN_ATTEMPTS |
| **Category** | Security & Authentication |
| **Owner** | Power Users |
| **Default Value** | 3 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'FAILED_LOGIN_ATTEMPTS'
```

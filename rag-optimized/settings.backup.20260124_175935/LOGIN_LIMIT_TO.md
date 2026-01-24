# LOGIN_LIMIT_TO - iPurchase System Setting

**Category:** Security & Authentication

Comma separated list of User ID's or Group ID's that are allowed to login to the system. This setting is used for when putting the system in Admin mode (upgrade or new release). Asterisk indicates ...

**Common questions this answers:**
- What is LOGIN_LIMIT_TO?
- What does LOGIN_LIMIT_TO do?
- What is the default value for LOGIN_LIMIT_TO?
- How do I configure LOGIN_LIMIT_TO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_LIMIT_TO |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_LIMIT_TO'
```

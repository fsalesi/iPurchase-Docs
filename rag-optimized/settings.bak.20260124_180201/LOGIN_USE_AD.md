# LOGIN_USE_AD - iPurchase System Setting

**Category:** Security & Authentication

Auto login user if using NTLM Active Directory security.

**Common questions this answers:**
- What is LOGIN_USE_AD?
- What does LOGIN_USE_AD do?
- What is the default value for LOGIN_USE_AD?
- How do I configure LOGIN_USE_AD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_USE_AD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_USE_AD'
```

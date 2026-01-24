# LOGIN_HIDE_FORGOT_PASSWORD - iPurchase System Setting

**Category:** Security & Authentication

Hide the Forgot Password link on the login screen

**Common questions this answers:**
- What is LOGIN_HIDE_FORGOT_PASSWORD?
- What does LOGIN_HIDE_FORGOT_PASSWORD do?
- What is the default value for LOGIN_HIDE_FORGOT_PASSWORD?
- How do I configure LOGIN_HIDE_FORGOT_PASSWORD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_HIDE_FORGOT_PASSWORD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_HIDE_FORGOT_PASSWORD'
```

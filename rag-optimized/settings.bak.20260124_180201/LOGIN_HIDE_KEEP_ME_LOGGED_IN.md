# LOGIN_HIDE_KEEP_ME_LOGGED_IN - iPurchase System Setting

**Category:** Security & Authentication

Hide the Keep me logged in link on the login screen

**Common questions this answers:**
- What is LOGIN_HIDE_KEEP_ME_LOGGED_IN?
- What does LOGIN_HIDE_KEEP_ME_LOGGED_IN do?
- What is the default value for LOGIN_HIDE_KEEP_ME_LOGGED_IN?
- How do I configure LOGIN_HIDE_KEEP_ME_LOGGED_IN?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_HIDE_KEEP_ME_LOGGED_IN |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_HIDE_KEEP_ME_LOGGED_IN'
```

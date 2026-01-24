# LOGIN_HIDE_REQUEST_ACCESS - iPurchase System Setting

**Category:** Security & Authentication

Hide the Request Access link on the login screen

**Common questions this answers:**
- What is LOGIN_HIDE_REQUEST_ACCESS?
- What does LOGIN_HIDE_REQUEST_ACCESS do?
- What is the default value for LOGIN_HIDE_REQUEST_ACCESS?
- How do I configure LOGIN_HIDE_REQUEST_ACCESS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_HIDE_REQUEST_ACCESS |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_HIDE_REQUEST_ACCESS'
```

# LOGIN_HIDE_EMAIL_HELPDESK - iPurchase System Setting

**Category:** Email Configuration

Hide the Email Helpdesk link on the login screen

**Common questions this answers:**
- What is LOGIN_HIDE_EMAIL_HELPDESK?
- What does LOGIN_HIDE_EMAIL_HELPDESK do?
- What is the default value for LOGIN_HIDE_EMAIL_HELPDESK?
- How do I configure LOGIN_HIDE_EMAIL_HELPDESK?
- How does LOGIN_HIDE_EMAIL_HELPDESK affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_HIDE_EMAIL_HELPDESK |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_HIDE_EMAIL_HELPDESK'
```

# EMAIL_HELPDESK - iPurchase System Setting

**Category:** Email Configuration

Helpdesk Email Address Enter the email address for the helpdesk. Used on login screen as well as all emails.

**Common questions this answers:**
- What is EMAIL_HELPDESK?
- What does EMAIL_HELPDESK do?
- What is the default value for EMAIL_HELPDESK?
- How do I configure EMAIL_HELPDESK?
- How does EMAIL_HELPDESK affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_HELPDESK |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_HELPDESK'
```

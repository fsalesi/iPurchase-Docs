# EMAIL_REGISTRATIONS - iPurchase System Setting

**Category:** Email Configuration

Email addresses (comma-separated). Recipients of new user registration notifications.

**Common questions this answers:**
- What is EMAIL_REGISTRATIONS?
- What does EMAIL_REGISTRATIONS do?
- What is the default value for EMAIL_REGISTRATIONS?
- How do I configure EMAIL_REGISTRATIONS?
- How does EMAIL_REGISTRATIONS affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_REGISTRATIONS |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_REGISTRATIONS'
```

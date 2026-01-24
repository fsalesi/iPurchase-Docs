# EMAILS_TO - iPurchase System Setting

**Category:** Email Configuration

Comma-separated email address(s) where all emails from the service will be sent to. This overrides the actual user's email addresses.

**Common questions this answers:**
- What is EMAILS_TO?
- What does EMAILS_TO do?
- What is the default value for EMAILS_TO?
- How do I configure EMAILS_TO?
- How does EMAILS_TO affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAILS_TO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAILS_TO'
```

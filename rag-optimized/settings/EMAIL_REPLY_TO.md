# EMAIL_REPLY_TO - iPurchase System Setting

**Category:** Email Configuration

Email address. Reply-to address used in system-generated emails. If blank, uses FROM address.

**Common questions this answers:**
- What is EMAIL_REPLY_TO?
- What does EMAIL_REPLY_TO do?
- What is the default value for EMAIL_REPLY_TO?
- How do I configure EMAIL_REPLY_TO?
- How does EMAIL_REPLY_TO affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_REPLY_TO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_REPLY_TO'
```

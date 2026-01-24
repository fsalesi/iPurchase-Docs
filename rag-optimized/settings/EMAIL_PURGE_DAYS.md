# EMAIL_PURGE_DAYS - iPurchase System Setting

**Category:** Email Configuration

How often iPurchase will purge emails that have error-ed . Value is in days.

**Common questions this answers:**
- What is EMAIL_PURGE_DAYS?
- What does EMAIL_PURGE_DAYS do?
- What is the default value for EMAIL_PURGE_DAYS?
- How do I configure EMAIL_PURGE_DAYS?
- How does EMAIL_PURGE_DAYS affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PURGE_DAYS |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | 30 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PURGE_DAYS'
```

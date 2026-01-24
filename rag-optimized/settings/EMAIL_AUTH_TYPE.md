# EMAIL_AUTH_TYPE - iPurchase System Setting

**Category:** Email Configuration

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is EMAIL_AUTH_TYPE?
- What does EMAIL_AUTH_TYPE do?
- What is the default value for EMAIL_AUTH_TYPE?
- How do I configure EMAIL_AUTH_TYPE?
- How does EMAIL_AUTH_TYPE affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_AUTH_TYPE |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_AUTH_TYPE'
```

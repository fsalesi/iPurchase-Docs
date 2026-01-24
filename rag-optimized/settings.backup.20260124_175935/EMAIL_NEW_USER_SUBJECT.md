# EMAIL_NEW_USER_SUBJECT - iPurchase System Setting

**Category:** Email Configuration

This setting allows the administrator to set the subject for the new user email.

**Common questions this answers:**
- What is EMAIL_NEW_USER_SUBJECT?
- What does EMAIL_NEW_USER_SUBJECT do?
- What is the default value for EMAIL_NEW_USER_SUBJECT?
- How do I configure EMAIL_NEW_USER_SUBJECT?
- How does EMAIL_NEW_USER_SUBJECT affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_NEW_USER_SUBJECT |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_NEW_USER_SUBJECT'
```

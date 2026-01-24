# EMAIL_PASSWORD_CHANGE_BODY - iPurchase System Setting

**Category:** Email Configuration

This setting allows the administrator to set the body of an email when the administrator changes a password.  Special token is $PASSWORD.

**Common questions this answers:**
- What is EMAIL_PASSWORD_CHANGE_BODY?
- What does EMAIL_PASSWORD_CHANGE_BODY do?
- What is the default value for EMAIL_PASSWORD_CHANGE_BODY?
- How do I configure EMAIL_PASSWORD_CHANGE_BODY?
- How does EMAIL_PASSWORD_CHANGE_BODY affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PASSWORD_CHANGE_BODY |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PASSWORD_CHANGE_BODY'
```

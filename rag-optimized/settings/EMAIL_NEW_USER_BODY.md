# EMAIL_NEW_USER_BODY - iPurchase System Setting

**Category:** Email Configuration

This setting allows the administrator to set the body of the email that is sent to users when a new user is created. Special tokens that can be inserted in email are $User ID, $PASSWORD, $URL.  The...

**Common questions this answers:**
- What is EMAIL_NEW_USER_BODY?
- What does EMAIL_NEW_USER_BODY do?
- What is the default value for EMAIL_NEW_USER_BODY?
- How do I configure EMAIL_NEW_USER_BODY?
- How does EMAIL_NEW_USER_BODY affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_NEW_USER_BODY |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_NEW_USER_BODY'
```

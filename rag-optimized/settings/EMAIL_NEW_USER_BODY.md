# EMAIL_NEW_USER_BODY - iPurchase System Setting

**Category:** Email Configuration

This setting allows the administrator to set the body of the email that is sent to users when a new user is created. Special tokens that can be inserted in email are $User ID, $PASSWORD, $URL.  These tokens will be substituted with the actual values.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_NEW_USER_BODY |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_NEW_USER_BODY'
```

# EMAIL_PASSWORD_CHANGE_BODY - iPurchase System Setting

**Category:** Email Configuration

This setting allows the administrator to set the body of an email when the administrator changes a password.  Special token is $PASSWORD.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PASSWORD_CHANGE_BODY |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PASSWORD_CHANGE_BODY'
```
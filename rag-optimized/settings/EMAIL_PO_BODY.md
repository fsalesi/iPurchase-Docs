# EMAIL_PO_BODY - iPurchase System Setting

**Category:** Email Configuration

Allows the administrator to create a custom email body for new PO.

### How It Works

This setting defines the email body content. You can use HTML formatting and dynamic tokens that are replaced with actual values when the email is sent.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_BODY |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | This should be line one. <br><br> |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_BODY'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
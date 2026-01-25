# EMAIL_PO_BODY_REVISION - iPurchase System Setting

**Category:** Email Configuration

Allows the administrator to create a custom email body for PO revision emails.

### How It Works

This setting defines the email body content. You can use HTML formatting and dynamic tokens that are replaced with actual values when the email is sent.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_BODY_REVISION |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_BODY_REVISION'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)

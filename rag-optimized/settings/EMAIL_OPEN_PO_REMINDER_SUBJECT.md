# EMAIL_OPEN_PO_REMINDER_SUBJECT - iPurchase System Setting

**Category:** Email Configuration

Configuration setting for email configuration.

### How It Works

This setting customizes the subject line for outgoing emails. Choose text that clearly identifies the email purpose to improve open rates and avoid spam filters.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_OPEN_PO_REMINDER_SUBJECT |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | Open POs in IPurchase |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_OPEN_PO_REMINDER_SUBJECT'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
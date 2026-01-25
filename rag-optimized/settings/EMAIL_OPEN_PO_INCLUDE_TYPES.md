# EMAIL_OPEN_PO_INCLUDE_TYPES - iPurchase System Setting

**Category:** Email Configuration

Configuration setting for email configuration.

### How It Works

This email-related setting controls how iPurchase communicates with users via email notifications.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_OPEN_PO_INCLUDE_TYPES |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | !Inventory,* |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_OPEN_PO_INCLUDE_TYPES'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
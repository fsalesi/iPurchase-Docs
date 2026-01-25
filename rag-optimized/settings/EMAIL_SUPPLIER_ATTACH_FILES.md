# EMAIL_SUPPLIER_ATTACH_FILES - iPurchase System Setting

**Category:** Email Configuration

This setting determines whether attachments are added to the email that will go to the supplier when the requisition is approved.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This email-related setting controls how iPurchase communicates with users via email notifications.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_ATTACH_FILES |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_ATTACH_FILES'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
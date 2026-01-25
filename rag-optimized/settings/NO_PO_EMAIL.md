# NO_PO_EMAIL - iPurchase System Setting

**Category:** Email Configuration

Technical - Do Not Modify without consulting ISS

### How It Works

This email-related setting controls how iPurchase communicates with users via email notifications.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_PO_EMAIL |
| **Category** | Email Configuration |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_PO_EMAIL'
```

### Related Settings

- [NO_CHANGE_EMAIL](NO_CHANGE_EMAIL.md)
- [NO_EMAILS](NO_EMAILS.md)
- [NO_EMAIL_REQ_BODY](NO_EMAIL_REQ_BODY.md)
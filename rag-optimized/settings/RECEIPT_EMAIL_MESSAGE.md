# RECEIPT_EMAIL_MESSAGE - iPurchase System Setting

**Category:** Email Configuration

Custom message text for receipt notification emails.

### How It Works

This email-related setting controls how iPurchase communicates with users via email notifications.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RECEIPT_EMAIL_MESSAGE |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RECEIPT_EMAIL_MESSAGE'
```

### Related Settings

- [RECEIPT_EMAIL_REQ_TYPES](RECEIPT_EMAIL_REQ_TYPES.md)
- [RECEIPT_EMAIL_SUBJECT](RECEIPT_EMAIL_SUBJECT.md)
- [RECEIPT_EMAIL_TO](RECEIPT_EMAIL_TO.md)

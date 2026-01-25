# RECEIPT_EMAIL_TO - iPurchase System Setting

**Category:** Email Configuration

Email addresses for receipt notifications.

### How It Works

Configure email recipients for this notification type. Multiple addresses can be comma-separated.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RECEIPT_EMAIL_TO |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RECEIPT_EMAIL_TO'
```

### Related Settings

- [RECEIPT_EMAIL_MESSAGE](RECEIPT_EMAIL_MESSAGE.md)
- [RECEIPT_EMAIL_REQ_TYPES](RECEIPT_EMAIL_REQ_TYPES.md)
- [RECEIPT_EMAIL_SUBJECT](RECEIPT_EMAIL_SUBJECT.md)

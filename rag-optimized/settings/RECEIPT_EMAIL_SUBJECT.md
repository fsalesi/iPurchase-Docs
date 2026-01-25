# RECEIPT_EMAIL_SUBJECT - iPurchase System Setting

**Category:** Email Configuration

Email subject for receipt notifications.

### How It Works

This setting customizes the subject line for outgoing emails. Choose text that clearly identifies the email purpose to improve open rates and avoid spam filters.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RECEIPT_EMAIL_SUBJECT |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | Receipt Notification |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RECEIPT_EMAIL_SUBJECT'
```

### Related Settings

- [RECEIPT_EMAIL_MESSAGE](RECEIPT_EMAIL_MESSAGE.md)
- [RECEIPT_EMAIL_REQ_TYPES](RECEIPT_EMAIL_REQ_TYPES.md)
- [RECEIPT_EMAIL_TO](RECEIPT_EMAIL_TO.md)
# RECEIPT_EMAIL_MESSAGE - iPurchase System Setting

**Category:** Email Configuration

Custom message text for receipt notification emails.

### How It Works

See the description above for valid values and usage.

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

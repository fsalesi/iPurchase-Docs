# EMAIL_SUPPLIER_CONFIRMATION_REMINDER_TEXT - iPurchase System Setting

**Category:** Email Configuration

Custom text included in supplier confirmation reminder emails.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_CONFIRMATION_REMINDER_TEXT |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_CONFIRMATION_REMINDER_TEXT'
```
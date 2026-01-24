# EMAIL_OPEN_PO_REMINDER_TEXT - iPurchase System Setting

**Category:** Email Configuration

Configuration setting for iPurchase.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_OPEN_PO_REMINDER_TEXT |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | Below is a list of your open purchase orders |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_OPEN_PO_REMINDER_TEXT'
```
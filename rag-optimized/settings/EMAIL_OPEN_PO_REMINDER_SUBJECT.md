# EMAIL_OPEN_PO_REMINDER_SUBJECT - iPurchase System Setting

**Category:** Email Configuration



### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_OPEN_PO_REMINDER_SUBJECT |
| **Category** | Email Configuration |
| **Owner** |  |
| **Default Value** | Open POs in IPurchase |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_OPEN_PO_REMINDER_SUBJECT'
```

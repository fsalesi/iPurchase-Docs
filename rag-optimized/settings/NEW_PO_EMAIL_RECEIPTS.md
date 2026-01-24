# NEW_PO_EMAIL_RECEIPTS - iPurchase System Setting

**Category:** Email Configuration

This setting determines if delivery receipts and read receipts are requested from the recipient's mail server when the email which includes the new PO attached is sent. To turn off this functionality set this value to "no,no" without the quotes. This is a two part setting comma-separated, no spaces around comma. The first part is a yes or no value indicating whether or not to ask for a delivery receipt. The second part is also yes or no indicating whether or not to ask for a delivery receipt. This setting can't be left blank.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NEW_PO_EMAIL_RECEIPTS |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | no,no |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NEW_PO_EMAIL_RECEIPTS'
```

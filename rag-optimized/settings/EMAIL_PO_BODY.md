# EMAIL_PO_BODY - iPurchase System Setting

**Category:** Email Configuration

Allows the administrator to create a custom email body for new PO.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_BODY |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | This should be line one. <br><br> |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_BODY'
```

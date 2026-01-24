# EMAIL_SUPPLIER_ATTACH_FILES - iPurchase System Setting

**Category:** Email Configuration

This setting determines whether attachments are added to the email that will go to the supplier when the requisition is approved.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_ATTACH_FILES |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_ATTACH_FILES'
```

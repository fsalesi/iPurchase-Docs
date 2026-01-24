# EMAIL_SUPPLIER_CONFIRMATION_TEXT - iPurchase System Setting

**Category:** Email Configuration

This is the text that is to be inserted above the link which is included in the supplier email PO program. The default is "Please click the link to confirm acceptance of the Purchase Order".

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_CONFIRMATION_TEXT |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_CONFIRMATION_TEXT'
```
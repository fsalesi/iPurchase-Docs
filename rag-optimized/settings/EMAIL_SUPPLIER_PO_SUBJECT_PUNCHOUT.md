# EMAIL_SUPPLIER_PO_SUBJECT_PUNCHOUT - iPurchase System Setting

**Category:** Email Configuration

This text will be used as the subject of the email going to the supplier. If you'd like the PO number(s) to appear in the subject, add the text "$NBR" without the quotes in the position that you want the PO number to appear.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO_SUBJECT_PUNCHOUT |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | Punchout Purchase Order - $NBR |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO_SUBJECT_PUNCHOUT'
```
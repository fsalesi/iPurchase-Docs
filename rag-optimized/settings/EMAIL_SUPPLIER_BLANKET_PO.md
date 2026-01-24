# EMAIL_SUPPLIER_BLANKET_PO - iPurchase System Setting

**Category:** Email Configuration

This setting determines whether or not an email is automatically sent to a supplier when the blanket order requisition is approved.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_BLANKET_PO |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_BLANKET_PO'
```

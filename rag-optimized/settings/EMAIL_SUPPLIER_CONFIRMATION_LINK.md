# EMAIL_SUPPLIER_CONFIRMATION_LINK - iPurchase System Setting

**Category:** Email Configuration

Determines if confirmation link is included in the PO email that is automatically sent to the supplier. It will also determine if the 'Include Confirmation Link' is displayed as an option on the manual 'Email PO' form in the requisition workbench.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_CONFIRMATION_LINK |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_CONFIRMATION_LINK'
```

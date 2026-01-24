# EMAIL_SUPPLIER_CONFIRMATION_TEXT - iPurchase System Setting

**Category:** Email Configuration

This is the text that is to be inserted above the link which is included in the supplier email PO program. The default is "Please click the link to confirm acceptance of the Purchase Order".

**Common questions this answers:**
- What is EMAIL_SUPPLIER_CONFIRMATION_TEXT?
- What does EMAIL_SUPPLIER_CONFIRMATION_TEXT do?
- What is the default value for EMAIL_SUPPLIER_CONFIRMATION_TEXT?
- How do I configure EMAIL_SUPPLIER_CONFIRMATION_TEXT?
- How does EMAIL_SUPPLIER_CONFIRMATION_TEXT affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_CONFIRMATION_TEXT |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_CONFIRMATION_TEXT'
```

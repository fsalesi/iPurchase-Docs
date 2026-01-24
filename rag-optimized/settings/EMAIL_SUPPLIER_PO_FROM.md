# EMAIL_SUPPLIER_PO_FROM - iPurchase System Setting

**Category:** Email Configuration

This is the email address to be used as the "From" field on the email. This can be a static email address or one of $xxreq_buyer, $xxreq_User ID, $xxreq_obo. If this field is left blank then the se...

**Common questions this answers:**
- What is EMAIL_SUPPLIER_PO_FROM?
- What does EMAIL_SUPPLIER_PO_FROM do?
- What is the default value for EMAIL_SUPPLIER_PO_FROM?
- How do I configure EMAIL_SUPPLIER_PO_FROM?
- How does EMAIL_SUPPLIER_PO_FROM affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO_FROM |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | $xxreq_buyer |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO_FROM'
```

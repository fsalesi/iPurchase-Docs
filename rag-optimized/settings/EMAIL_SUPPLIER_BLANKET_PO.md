# EMAIL_SUPPLIER_BLANKET_PO - iPurchase System Setting

**Category:** Email Configuration

This setting determines whether or not an email is automatically sent to a supplier when the blanket order requisition is approved.

**Common questions this answers:**
- What is EMAIL_SUPPLIER_BLANKET_PO?
- What does EMAIL_SUPPLIER_BLANKET_PO do?
- What is the default value for EMAIL_SUPPLIER_BLANKET_PO?
- How do I configure EMAIL_SUPPLIER_BLANKET_PO?
- How does EMAIL_SUPPLIER_BLANKET_PO affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_BLANKET_PO |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_BLANKET_PO'
```

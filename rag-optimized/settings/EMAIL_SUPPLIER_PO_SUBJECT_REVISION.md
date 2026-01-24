# EMAIL_SUPPLIER_PO_SUBJECT_REVISION - iPurchase System Setting

**Category:** Email Configuration

This text will be used as the subject of the email going to the supplier. If you'd like the PO number(s) to appear in the subject, add the text "$NBR" without the quotes in the position that you wa...

**Common questions this answers:**
- What is EMAIL_SUPPLIER_PO_SUBJECT_REVISION?
- What does EMAIL_SUPPLIER_PO_SUBJECT_REVISION do?
- What is the default value for EMAIL_SUPPLIER_PO_SUBJECT_REVISION?
- How do I configure EMAIL_SUPPLIER_PO_SUBJECT_REVISION?
- How does EMAIL_SUPPLIER_PO_SUBJECT_REVISION affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO_SUBJECT_REVISION |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | Purchase Order Revision - $NBR |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO_SUBJECT_REVISION'
```

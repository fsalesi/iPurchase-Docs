# EMAIL_SUPPLIER_PO_CC - iPurchase System Setting

**Category:** Email Configuration

This is a list of email address(s) of whom to carbon copy the supplier email to when the PO is created.  A value of "BUYER" will copy the associated buyer which is set on the requisition. If a user...

**Common questions this answers:**
- What is EMAIL_SUPPLIER_PO_CC?
- What does EMAIL_SUPPLIER_PO_CC do?
- What is the default value for EMAIL_SUPPLIER_PO_CC?
- How do I configure EMAIL_SUPPLIER_PO_CC?
- How does EMAIL_SUPPLIER_PO_CC affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO_CC |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | $xxreq_buyer,$xxreq_obo,$xxreq_userid |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO_CC'
```

# EMAIL_SUPPLIER_ATTACH_FILES - iPurchase System Setting

**Category:** Email Configuration

This setting determines whether attachments are added to the email that will go to the supplier when the requisition is approved.

**Common questions this answers:**
- What is EMAIL_SUPPLIER_ATTACH_FILES?
- What does EMAIL_SUPPLIER_ATTACH_FILES do?
- What is the default value for EMAIL_SUPPLIER_ATTACH_FILES?
- How do I configure EMAIL_SUPPLIER_ATTACH_FILES?
- How does EMAIL_SUPPLIER_ATTACH_FILES affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_ATTACH_FILES |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_ATTACH_FILES'
```

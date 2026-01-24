# INQUIRY_LAST_REV_DEFAULT - iPurchase System Setting

**Category:** Reporting & Inquiry

Setting this to true will check the Last Revision Only in the requisition inquiry. This is useful when you only want to see the requisition for the last revision of a PO. As opposed to all the requ...

**Common questions this answers:**
- What is INQUIRY_LAST_REV_DEFAULT?
- What does INQUIRY_LAST_REV_DEFAULT do?
- What is the default value for INQUIRY_LAST_REV_DEFAULT?
- How do I configure INQUIRY_LAST_REV_DEFAULT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INQUIRY_LAST_REV_DEFAULT |
| **Category** | Reporting & Inquiry |
| **Owner** |  |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_LAST_REV_DEFAULT'
```

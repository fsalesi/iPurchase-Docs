# EMAIL_SUPPLIER_ATTACH_LINKS - iPurchase System Setting

**Category:** Email Configuration

This setting determines whether attachments to a requisition are sent to the supplier as links in the email.

**Common questions this answers:**
- What is EMAIL_SUPPLIER_ATTACH_LINKS?
- What does EMAIL_SUPPLIER_ATTACH_LINKS do?
- What is the default value for EMAIL_SUPPLIER_ATTACH_LINKS?
- How do I configure EMAIL_SUPPLIER_ATTACH_LINKS?
- How does EMAIL_SUPPLIER_ATTACH_LINKS affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_ATTACH_LINKS |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_ATTACH_LINKS'
```

# MAX_UPLOAD_MB - iPurchase System Setting

**Category:** Uncategorized

Maximum size in megabytes for attachments.

**Common questions this answers:**
- What is MAX_UPLOAD_MB?
- What does MAX_UPLOAD_MB do?
- What is the default value for MAX_UPLOAD_MB?
- How do I configure MAX_UPLOAD_MB?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MAX_UPLOAD_MB |
| **Category** | Uncategorized |
| **Owner** | IT |
| **Default Value** | 10 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MAX_UPLOAD_MB'
```

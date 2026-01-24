# FILE_UPLOAD_TYPES - iPurchase System Setting

**Category:** System Configuration

Comma-separated file extensions. Allowed file types for document uploads (e.g., pdf,doc,docx,xlsx).

**Common questions this answers:**
- What is FILE_UPLOAD_TYPES?
- What does FILE_UPLOAD_TYPES do?
- What is the default value for FILE_UPLOAD_TYPES?
- How do I configure FILE_UPLOAD_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | FILE_UPLOAD_TYPES |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'FILE_UPLOAD_TYPES'
```

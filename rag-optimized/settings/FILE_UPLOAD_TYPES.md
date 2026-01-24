# FILE_UPLOAD_TYPES - iPurchase System Setting

**Category:** System Configuration

Comma-separated file extensions. Allowed file types for document uploads (e.g., pdf,doc,docx,xlsx).

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | FILE_UPLOAD_TYPES |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'FILE_UPLOAD_TYPES'
```
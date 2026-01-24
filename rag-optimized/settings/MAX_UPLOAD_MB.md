# MAX_UPLOAD_MB - iPurchase System Setting

**Category:** Uncategorized

Maximum size in megabytes for attachments.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MAX_UPLOAD_MB |
| **Category** | Uncategorized |
| **Owner** | IT |
| **Default Value** | 10 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MAX_UPLOAD_MB'
```
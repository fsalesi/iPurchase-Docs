# FILE_UPLOAD_TYPES - iPurchase System Setting

**Category:** System Configuration

Comma-separated file extensions.

### How It Works

This setting configures system configuration behavior in iPurchase.

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
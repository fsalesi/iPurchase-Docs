# ARCHIVE_FOLDER - iPurchase System Setting

**Category:** Uncategorized

This should not be changed unless advised by ISS Group This is a temporary storage area for requisitions being transferred to or from the production and archive systems

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ARCHIVE_FOLDER |
| **Category** | Uncategorized |
| **Owner** | IT |
| **Default Value** | archive |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ARCHIVE_FOLDER'
```

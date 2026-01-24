# BACKUP_DB_KEEP_DAYS - iPurchase System Setting

**Category:** Uncategorized

How many days worth of iPurchase database backups to keep

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BACKUP_DB_KEEP_DAYS |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | 7 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BACKUP_DB_KEEP_DAYS'
```

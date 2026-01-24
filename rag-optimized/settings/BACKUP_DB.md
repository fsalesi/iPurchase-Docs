# BACKUP_DB - iPurchase System Setting

**Category:** Uncategorized

iPurchase provides a rudimentary backup system. List the full pathname and database name of the iPurchase database

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BACKUP_DB |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | ../db/ipurchase.db |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BACKUP_DB'
```
# BACKUP_DB - iPurchase System Setting

**Category:** Uncategorized

iPurchase provides a rudimentary backup system. List the full pathname and database name of the iPurchase database

**Common questions this answers:**
- What is BACKUP_DB?
- What does BACKUP_DB do?
- What is the default value for BACKUP_DB?
- How do I configure BACKUP_DB?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BACKUP_DB |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | ../db/ipurchase.db |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BACKUP_DB'
```

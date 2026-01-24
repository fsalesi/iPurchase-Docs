# CAT_IMPORT_DIR - iPurchase System Setting

**Category:** Uncategorized

The administrator will choose a folder on application server where catalog files will be dropped (when catalogs are sent directly from supplier - not supported in base).

**Common questions this answers:**
- What is CAT_IMPORT_DIR?
- What does CAT_IMPORT_DIR do?
- What is the default value for CAT_IMPORT_DIR?
- How do I configure CAT_IMPORT_DIR?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CAT_IMPORT_DIR |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CAT_IMPORT_DIR'
```

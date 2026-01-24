# CAT_IMPORT_DIR - iPurchase System Setting

**Category:** Uncategorized

The administrator will choose a folder on application server where catalog files will be dropped (when catalogs are sent directly from supplier - not supported in base).

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CAT_IMPORT_DIR |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CAT_IMPORT_DIR'
```
# CATALOG_SHOW_PICTURES - iPurchase System Setting

**Category:** Catalog & Vendors

If true, images of items will appear in catalogs.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_SHOW_PICTURES |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_SHOW_PICTURES'
```

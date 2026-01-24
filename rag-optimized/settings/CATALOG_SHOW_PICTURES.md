# CATALOG_SHOW_PICTURES - iPurchase System Setting

**Category:** Catalog & Vendors

If true, images of items will appear in catalogs.

**Common questions this answers:**
- What is CATALOG_SHOW_PICTURES?
- What does CATALOG_SHOW_PICTURES do?
- What is the default value for CATALOG_SHOW_PICTURES?
- How do I configure CATALOG_SHOW_PICTURES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_SHOW_PICTURES |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_SHOW_PICTURES'
```

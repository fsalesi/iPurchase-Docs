# CATALOG_SHOW_DETAILS - iPurchase System Setting

**Category:** Catalog & Vendors

If true, the catalog screen will display supplier, lead time, minimum quantity.

**Common questions this answers:**
- What is CATALOG_SHOW_DETAILS?
- What does CATALOG_SHOW_DETAILS do?
- What is the default value for CATALOG_SHOW_DETAILS?
- How do I configure CATALOG_SHOW_DETAILS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_SHOW_DETAILS |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_SHOW_DETAILS'
```

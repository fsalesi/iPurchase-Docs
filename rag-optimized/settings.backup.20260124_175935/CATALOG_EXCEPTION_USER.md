# CATALOG_EXCEPTION_USER - iPurchase System Setting

**Category:** Catalog & Vendors

Can-Do list. Users/groups exempt from catalog-only purchasing restrictions. Can create requisitions outside catalog.

**Common questions this answers:**
- What is CATALOG_EXCEPTION_USER?
- What does CATALOG_EXCEPTION_USER do?
- What is the default value for CATALOG_EXCEPTION_USER?
- How do I configure CATALOG_EXCEPTION_USER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_EXCEPTION_USER |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_EXCEPTION_USER'
```

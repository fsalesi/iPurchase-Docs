# CATALOG_SORT - iPurchase System Setting

**Category:** Catalog & Vendors

This setting gives the administrator the option to choose the sort by in a catalog requisition

**Common questions this answers:**
- What is CATALOG_SORT?
- What does CATALOG_SORT do?
- What is the default value for CATALOG_SORT?
- How do I configure CATALOG_SORT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_SORT |
| **Category** | Catalog & Vendors |
| **Owner** | ISS |
| **Default Value** | List:by uCatalog.uDomain by uCatalog.SupplierPart:Part Number (Ascending),by uCatalog.uDomain by uCatalog.SupplierPart desc:Part Number (Descending),by uCatalog.UnitPrice:Price (Low to High),by uCatalog.UnitPrice desc:Price (High to Low) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_SORT'
```

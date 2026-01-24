# CATALOG_USE_CART - iPurchase System Setting

**Category:** Catalog & Vendors

Comma Separated list of User ID's or Group ID's that will use the catalog functionality in the "New Catalog Req" screen. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is CATALOG_USE_CART?
- What does CATALOG_USE_CART do?
- What is the default value for CATALOG_USE_CART?
- How do I configure CATALOG_USE_CART?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_USE_CART |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_USE_CART'
```

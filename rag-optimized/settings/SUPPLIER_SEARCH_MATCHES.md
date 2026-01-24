# SUPPLIER_SEARCH_MATCHES - iPurchase System Setting

**Category:** Catalog & Vendors

If set to True then a user can search for a supplier using any character in the suppliers name.  If set to True, the supplier lookup will run slower.

**Common questions this answers:**
- What is SUPPLIER_SEARCH_MATCHES?
- What does SUPPLIER_SEARCH_MATCHES do?
- What is the default value for SUPPLIER_SEARCH_MATCHES?
- How do I configure SUPPLIER_SEARCH_MATCHES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_SEARCH_MATCHES |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_SEARCH_MATCHES'
```

# NEW_SUPPLIER_NBRS - iPurchase System Setting

**Category:** Catalog & Vendors

Comma separated list of supplier numbers which should not allow final approval.

**Common questions this answers:**
- What is NEW_SUPPLIER_NBRS?
- What does NEW_SUPPLIER_NBRS do?
- What is the default value for NEW_SUPPLIER_NBRS?
- How do I configure NEW_SUPPLIER_NBRS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NEW_SUPPLIER_NBRS |
| **Category** | Catalog & Vendors |
| **Owner** |  |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NEW_SUPPLIER_NBRS'
```

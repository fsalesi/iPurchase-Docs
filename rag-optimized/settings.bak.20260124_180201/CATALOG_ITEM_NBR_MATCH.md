# CATALOG_ITEM_NBR_MATCH - iPurchase System Setting

**Category:** Catalog & Vendors

A user can search a catalog using either matches or contains criteria.  If set to True then the system will use the Match functionality. Matches:  If the item number is 12345 then you should be abl...

**Common questions this answers:**
- What is CATALOG_ITEM_NBR_MATCH?
- What does CATALOG_ITEM_NBR_MATCH do?
- What is the default value for CATALOG_ITEM_NBR_MATCH?
- How do I configure CATALOG_ITEM_NBR_MATCH?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_ITEM_NBR_MATCH |
| **Category** | Catalog & Vendors |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_ITEM_NBR_MATCH'
```

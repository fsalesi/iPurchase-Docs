# CATALOG_ITEM_NBR_MATCH - iPurchase System Setting

**Category:** Catalog & Vendors

A user can search a catalog using either matches or contains criteria.  If set to True then the system will use the Match functionality. Matches:  If the item number is 12345 then you should be able to search by using 345. Contains: You have to use the beginning part of the item number i.e. "123". Contains is faster but only searches the beginning of the word. Matches is slow but will search anywhere in the item number. If you have thousands of catalog items in your database then this will make the searching unusable

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_ITEM_NBR_MATCH |
| **Category** | Catalog & Vendors |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_ITEM_NBR_MATCH'
```

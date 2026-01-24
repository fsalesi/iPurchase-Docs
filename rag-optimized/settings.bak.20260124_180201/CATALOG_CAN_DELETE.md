# CATALOG_CAN_DELETE - iPurchase System Setting

**Category:** Catalog & Vendors

Comma Separated list of User ID's or Group ID's that are allowed to delete catalogs.  Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is CATALOG_CAN_DELETE?
- What does CATALOG_CAN_DELETE do?
- What is the default value for CATALOG_CAN_DELETE?
- How do I configure CATALOG_CAN_DELETE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_CAN_DELETE |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | admin |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_CAN_DELETE'
```

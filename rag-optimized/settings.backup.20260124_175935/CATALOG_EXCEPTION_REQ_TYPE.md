# CATALOG_EXCEPTION_REQ_TYPE - iPurchase System Setting

**Category:** Catalog & Vendors

If left blank the catalog exception requisition type should be set to "Catalog Exception". The administrator can change the name of the requisition type assigned to 'Catalog Exception' in this sett...

**Common questions this answers:**
- What is CATALOG_EXCEPTION_REQ_TYPE?
- What does CATALOG_EXCEPTION_REQ_TYPE do?
- What is the default value for CATALOG_EXCEPTION_REQ_TYPE?
- How do I configure CATALOG_EXCEPTION_REQ_TYPE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_EXCEPTION_REQ_TYPE |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_EXCEPTION_REQ_TYPE'
```

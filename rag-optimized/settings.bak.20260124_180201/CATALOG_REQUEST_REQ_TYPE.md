# CATALOG_REQUEST_REQ_TYPE - iPurchase System Setting

**Category:** Catalog & Vendors

Technical - Do Not Modify

**Common questions this answers:**
- What is CATALOG_REQUEST_REQ_TYPE?
- What does CATALOG_REQUEST_REQ_TYPE do?
- What is the default value for CATALOG_REQUEST_REQ_TYPE?
- How do I configure CATALOG_REQUEST_REQ_TYPE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_REQUEST_REQ_TYPE |
| **Category** | Catalog & Vendors |
| **Owner** | ISS |
| **Default Value** | Catalog Request |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_REQUEST_REQ_TYPE'
```

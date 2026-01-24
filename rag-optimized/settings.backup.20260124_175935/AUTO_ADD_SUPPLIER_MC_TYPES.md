# AUTO_ADD_SUPPLIER_MC_TYPES - iPurchase System Setting

**Category:** Catalog & Vendors

In QAD master comments, there is a reference number to identify a master comment, if this reference number equals the suppler then the master comment will be added to the requisition automatically ...

**Common questions this answers:**
- What is AUTO_ADD_SUPPLIER_MC_TYPES?
- What does AUTO_ADD_SUPPLIER_MC_TYPES do?
- What is the default value for AUTO_ADD_SUPPLIER_MC_TYPES?
- How do I configure AUTO_ADD_SUPPLIER_MC_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_ADD_SUPPLIER_MC_TYPES |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | PO |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_ADD_SUPPLIER_MC_TYPES'
```

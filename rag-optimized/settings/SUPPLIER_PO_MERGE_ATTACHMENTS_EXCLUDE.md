# SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE - iPurchase System Setting

**Category:** Catalog & Vendors

Comma-separated suppliers. Suppliers excluded from attachment merging.

**Common questions this answers:**
- What is SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE?
- What does SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE do?
- What is the default value for SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE?
- How do I configure SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE'
```

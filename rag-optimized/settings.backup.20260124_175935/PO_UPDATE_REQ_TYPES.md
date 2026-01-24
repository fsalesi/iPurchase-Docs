# PO_UPDATE_REQ_TYPES - iPurchase System Setting

**Category:** Purchase Orders

You can control the list of requisition types that will allow a change order, or * for all requisition types.

**Common questions this answers:**
- What is PO_UPDATE_REQ_TYPES?
- What does PO_UPDATE_REQ_TYPES do?
- What is the default value for PO_UPDATE_REQ_TYPES?
- How do I configure PO_UPDATE_REQ_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_UPDATE_REQ_TYPES |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_REQ_TYPES'
```

# PO_PREFIX - iPurchase System Setting

**Category:** Purchase Orders

Prefix added to purchase order numbers (e.g., PO- results in PO-12345).

**Common questions this answers:**
- What is PO_PREFIX?
- What does PO_PREFIX do?
- What is the default value for PO_PREFIX?
- How do I configure PO_PREFIX?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PREFIX |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PREFIX'
```

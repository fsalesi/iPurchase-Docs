# PO_PRINT_SORT - iPurchase System Setting

**Category:** Purchase Orders

This setting determines the value which will be used to sort the Purchase Order on the PO Print screen.

**Common questions this answers:**
- What is PO_PRINT_SORT?
- What does PO_PRINT_SORT do?
- What is the default value for PO_PRINT_SORT?
- How do I configure PO_PRINT_SORT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_SORT |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | LINE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_SORT'
```

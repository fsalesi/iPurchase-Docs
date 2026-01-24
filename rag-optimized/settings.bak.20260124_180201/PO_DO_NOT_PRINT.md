# PO_DO_NOT_PRINT - iPurchase System Setting

**Category:** Purchase Orders

Does not print the PO when requisition is approved.

**Common questions this answers:**
- What is PO_DO_NOT_PRINT?
- What does PO_DO_NOT_PRINT do?
- What is the default value for PO_DO_NOT_PRINT?
- How do I configure PO_DO_NOT_PRINT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_DO_NOT_PRINT |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_DO_NOT_PRINT'
```

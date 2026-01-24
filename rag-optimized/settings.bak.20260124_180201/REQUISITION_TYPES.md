# REQUISITION_TYPES - iPurchase System Setting

**Category:** Requisitions

Use the prefix "LIST:" followed by a comma-separated list of values. This will tell iPurchase that the specified list is to be used. Example: LIST:expense:Expense Req,Capex,Inventory,etc All the sy...

**Common questions this answers:**
- What is REQUISITION_TYPES?
- What does REQUISITION_TYPES do?
- What is the default value for REQUISITION_TYPES?
- How do I configure REQUISITION_TYPES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQUISITION_TYPES |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | List:Expense:Expense,Capital,Contract,Tooling,Other, |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQUISITION_TYPES'
```

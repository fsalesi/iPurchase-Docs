# FIRST_PO_NUMBER - iPurchase System Setting

**Category:** Purchase Orders

Numeric. Starting purchase order number for sequential PO numbering.

**Common questions this answers:**
- What is FIRST_PO_NUMBER?
- What does FIRST_PO_NUMBER do?
- What is the default value for FIRST_PO_NUMBER?
- How do I configure FIRST_PO_NUMBER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | FIRST_PO_NUMBER |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | 1 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'FIRST_PO_NUMBER'
```

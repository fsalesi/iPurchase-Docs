# PO_PRINT_DOMAIN_IN_FN - iPurchase System Setting

**Category:** Purchase Orders

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is PO_PRINT_DOMAIN_IN_FN?
- What does PO_PRINT_DOMAIN_IN_FN do?
- What is the default value for PO_PRINT_DOMAIN_IN_FN?
- How do I configure PO_PRINT_DOMAIN_IN_FN?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_DOMAIN_IN_FN |
| **Category** | Purchase Orders |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_DOMAIN_IN_FN'
```

# NO_PO_PP - iPurchase System Setting

**Category:** Purchase Orders

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is NO_PO_PP?
- What does NO_PO_PP do?
- What is the default value for NO_PO_PP?
- How do I configure NO_PO_PP?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_PO_PP |
| **Category** | Purchase Orders |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_PO_PP'
```

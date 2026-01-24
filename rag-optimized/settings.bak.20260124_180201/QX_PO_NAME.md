# QX_PO_NAME - iPurchase System Setting

**Category:** Purchase Orders

Name of the qxtend instance for Purchase Orders in this environment

**Common questions this answers:**
- What is QX_PO_NAME?
- What does QX_PO_NAME do?
- What is the default value for QX_PO_NAME?
- How do I configure QX_PO_NAME?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QX_PO_NAME |
| **Category** | Purchase Orders |
| **Owner** |  |
| **Default Value** | QADERP |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QX_PO_NAME'
```

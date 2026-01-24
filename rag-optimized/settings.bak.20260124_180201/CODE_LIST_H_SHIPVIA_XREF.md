# CODE_LIST_H_SHIPVIA_XREF - iPurchase System Setting

**Category:** iApprove Integration

This setting defines a cross-reference between the selected iPurchase ship via, and the code or description that the vendor needs to see on their electronic purchase order. Only applies to Punchout...

**Common questions this answers:**
- What is CODE_LIST_H_SHIPVIA_XREF?
- What does CODE_LIST_H_SHIPVIA_XREF do?
- What is the default value for CODE_LIST_H_SHIPVIA_XREF?
- How do I configure CODE_LIST_H_SHIPVIA_XREF?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_SHIPVIA_XREF |
| **Category** | iApprove Integration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_SHIPVIA_XREF'
```

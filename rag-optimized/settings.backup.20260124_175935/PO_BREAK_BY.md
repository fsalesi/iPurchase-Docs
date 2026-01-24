# PO_BREAK_BY - iPurchase System Setting

**Category:** Purchase Orders

Comma separated list of fields on a requisition that will be used to split the requisition into multiple PO's. Or Comma separated list of fields on a requisition that will be used to consolidate PO...

**Common questions this answers:**
- What is PO_BREAK_BY?
- What does PO_BREAK_BY do?
- What is the default value for PO_BREAK_BY?
- How do I configure PO_BREAK_BY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_BREAK_BY |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | xxreqd_vendor |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_BREAK_BY'
```

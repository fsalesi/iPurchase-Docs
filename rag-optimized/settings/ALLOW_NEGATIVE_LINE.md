# ALLOW_NEGATIVE_LINE - iPurchase System Setting

**Category:** Requisitions

Can-Do list. Users/groups allowed to enter negative quantities on requisition line items. Normally rejected with error message.

**Common questions this answers:**
- What is ALLOW_NEGATIVE_LINE?
- What does ALLOW_NEGATIVE_LINE do?
- What is the default value for ALLOW_NEGATIVE_LINE?
- How do I configure ALLOW_NEGATIVE_LINE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_NEGATIVE_LINE |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_NEGATIVE_LINE'
```

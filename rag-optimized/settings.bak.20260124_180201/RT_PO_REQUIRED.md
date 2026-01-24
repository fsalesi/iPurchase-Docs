# RT_PO_REQUIRED - iPurchase System Setting

**Category:** Purchase Orders

This setting is a list of requisition types that would set the PO Required field to True or Yes.  For example if you do not require a PO for credit card purchases and CREDIT_CARD is a Requisition T...

**Common questions this answers:**
- What is RT_PO_REQUIRED?
- What does RT_PO_REQUIRED do?
- What is the default value for RT_PO_REQUIRED?
- How do I configure RT_PO_REQUIRED?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_PO_REQUIRED |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_PO_REQUIRED'
```

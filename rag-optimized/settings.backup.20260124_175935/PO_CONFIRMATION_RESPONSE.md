# PO_CONFIRMATION_RESPONSE - iPurchase System Setting

**Category:** Purchase Orders

Message to display to the supplier when the supplier confirms receipt of the PO by clicking on the Confirm Receipt link in their email message.

**Common questions this answers:**
- What is PO_CONFIRMATION_RESPONSE?
- What does PO_CONFIRMATION_RESPONSE do?
- What is the default value for PO_CONFIRMATION_RESPONSE?
- How do I configure PO_CONFIRMATION_RESPONSE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_CONFIRMATION_RESPONSE |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_CONFIRMATION_RESPONSE'
```

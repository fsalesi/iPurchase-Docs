# BLANKET_SEND_PO - iPurchase System Setting

**Category:** Purchase Orders

If set to true the PO will be emailed.

**Common questions this answers:**
- What is BLANKET_SEND_PO?
- What does BLANKET_SEND_PO do?
- What is the default value for BLANKET_SEND_PO?
- How do I configure BLANKET_SEND_PO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BLANKET_SEND_PO |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BLANKET_SEND_PO'
```

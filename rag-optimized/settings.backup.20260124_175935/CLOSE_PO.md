# CLOSE_PO - iPurchase System Setting

**Category:** Purchase Orders

Comma Separated list of User ID's or Group ID's that will have the ability to close PO  or  PO line on Purchase order.  Either Line or whole PO can be closed. Close or canceled depends on Receipts....

**Common questions this answers:**
- What is CLOSE_PO?
- What does CLOSE_PO do?
- What is the default value for CLOSE_PO?
- How do I configure CLOSE_PO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CLOSE_PO |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | buyers |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CLOSE_PO'
```

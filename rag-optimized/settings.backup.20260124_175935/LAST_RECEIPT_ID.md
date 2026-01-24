# LAST_RECEIPT_ID - iPurchase System Setting

**Category:** Receiving

iPurchase process receipts in QAD for budgets. It periodically looks for receipts in batch. When implementing you can set the tr_id to start from so that it does not spend time looking at old recei...

**Common questions this answers:**
- What is LAST_RECEIPT_ID?
- What does LAST_RECEIPT_ID do?
- What is the default value for LAST_RECEIPT_ID?
- How do I configure LAST_RECEIPT_ID?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LAST_RECEIPT_ID |
| **Category** | Receiving |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LAST_RECEIPT_ID'
```

# LAST_RECEIPT_ID - iPurchase System Setting

**Category:** Receiving

iPurchase process receipts in QAD for budgets.

### How It Works

This setting configures receiving behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LAST_RECEIPT_ID |
| **Category** | Receiving |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LAST_RECEIPT_ID'
```
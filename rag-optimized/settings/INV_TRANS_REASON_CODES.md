# INV_TRANS_REASON_CODES - iPurchase System Setting

**Category:** Inventory & MRP

Comma-separated reason codes. Valid transaction reason codes for inventory movements.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INV_TRANS_REASON_CODES |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INV_TRANS_REASON_CODES'
```

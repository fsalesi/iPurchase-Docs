# INV_TRANS_TYPES - iPurchase System Setting

**Category:** Inventory & MRP

Comma-separated transaction types.

### How It Works

This setting configures inventory & mrp behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INV_TRANS_TYPES |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INV_TRANS_TYPES'
```

### Related Settings

- [INV_TRANS_REASON_CODES](INV_TRANS_REASON_CODES.md)
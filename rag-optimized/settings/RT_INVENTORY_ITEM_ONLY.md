# RT_INVENTORY_ITEM_ONLY - iPurchase System Setting

**Category:** Requisitions

Comma-separated req types.

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_INVENTORY_ITEM_ONLY |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_INVENTORY_ITEM_ONLY'
```

### Related Settings

- [RT_[Requisition Type]_ACCESS](<RT_[Requisition Type]_ACCESS.md>)
- [RT_[Requisition Type]_ACCOUNT_DEFAULT](<RT_[Requisition Type]_ACCOUNT_DEFAULT.md>)
- [RT_[Requisition Type]_ACCOUNT_RANGE](<RT_[Requisition Type]_ACCOUNT_RANGE.md>)

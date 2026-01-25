# RT_[Requisition Type]_DEFAULT_BUYER - iPurchase System Setting

**Category:** Requisitions

See DEFAULT_BUYER

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_DEFAULT_BUYER |
| **Category** | Requisitions |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_DEFAULT_BUYER'
```

### Related Settings

- [RT_INVENTORY_ITEM_ONLY](RT_INVENTORY_ITEM_ONLY.md)
- [RT_[Requisition Type]_ACCESS](<RT_[Requisition Type]_ACCESS.md>)
- [RT_[Requisition Type]_ACCOUNT_DEFAULT](<RT_[Requisition Type]_ACCOUNT_DEFAULT.md>)

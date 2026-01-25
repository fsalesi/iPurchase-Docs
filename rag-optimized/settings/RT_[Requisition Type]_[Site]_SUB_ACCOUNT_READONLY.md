# RT_[Requisition Type]_[Site]_SUB_ACCOUNT_READONLY - iPurchase System Setting

**Category:** Requisitions

TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]" and site for "[Site]".

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_[Site]_SUB_ACCOUNT_READONLY |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_[Site]_SUB_ACCOUNT_READONLY'
```

### Related Settings

- [RT_INVENTORY_ITEM_ONLY](RT_INVENTORY_ITEM_ONLY.md)
- [RT_[Requisition Type]_ACCESS](RT_[Requisition Type]_ACCESS.md)
- [RT_[Requisition Type]_ACCOUNT_DEFAULT](RT_[Requisition Type]_ACCOUNT_DEFAULT.md)
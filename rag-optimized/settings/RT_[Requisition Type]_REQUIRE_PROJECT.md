# RT_[Requisition Type]_REQUIRE_PROJECT - iPurchase System Setting

**Category:** Requisitions

Comma separated list of requisition types which will require a project code listed.

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_REQUIRE_PROJECT |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_REQUIRE_PROJECT'
```

### Related Settings

- [RT_INVENTORY_ITEM_ONLY](RT_INVENTORY_ITEM_ONLY.md)
- [RT_[Requisition Type]_ACCESS](<RT_[Requisition Type]_ACCESS.md>)
- [RT_[Requisition Type]_ACCOUNT_DEFAULT](<RT_[Requisition Type]_ACCOUNT_DEFAULT.md>)

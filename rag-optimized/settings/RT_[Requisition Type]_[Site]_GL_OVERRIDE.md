# RT_[Requisition Type]_[Site]_GL_OVERRIDE - iPurchase System Setting

**Category:** Requisitions

True or False If you set this setting to TRUE, then all items entered in the line entry screen for the specified requisition type and site combination will have the account, sub-account, and cost center set to the values which QAD would dictate based on the vendor and item.

### How It Works

This setting configures requisitions behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_[Site]_GL_OVERRIDE |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | False  |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_[Site]_GL_OVERRIDE'
```

### Related Settings

- [RT_INVENTORY_ITEM_ONLY](RT_INVENTORY_ITEM_ONLY.md)
- [RT_[Requisition Type]_ACCESS](<RT_[Requisition Type]_ACCESS.md>)
- [RT_[Requisition Type]_ACCOUNT_DEFAULT](<RT_[Requisition Type]_ACCOUNT_DEFAULT.md>)

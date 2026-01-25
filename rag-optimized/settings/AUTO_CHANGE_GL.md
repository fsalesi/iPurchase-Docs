# AUTO_CHANGE_GL - iPurchase System Setting

**Category:** Uncategorized

If your company's GL Account, Sub Account, and CC are set by having defaults at the Requisition or Requisition or Site level, then the GL information will change when you change Requisition Types.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_CHANGE_GL |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_CHANGE_GL'
```

### Related Settings

- [AUTO_ADD_DROPSHIP](AUTO_ADD_DROPSHIP.md)
- [AUTO_ADD_ITEM_MC_TYPES](AUTO_ADD_ITEM_MC_TYPES.md)
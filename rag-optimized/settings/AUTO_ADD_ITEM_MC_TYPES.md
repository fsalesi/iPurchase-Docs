# AUTO_ADD_ITEM_MC_TYPES - iPurchase System Setting

**Category:** Uncategorized

In QAD master comments, there is a reference number to identify a master comment, if this reference number equals the items number then the master comment will be added to the requisition automatically if the corresponding type of master comment is entered into this system setting.

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_ADD_ITEM_MC_TYPES |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | PO |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_ADD_ITEM_MC_TYPES'
```

### Related Settings

- [AUTO_ADD_DROPSHIP](AUTO_ADD_DROPSHIP.md)
- [AUTO_CHANGE_GL](AUTO_CHANGE_GL.md)

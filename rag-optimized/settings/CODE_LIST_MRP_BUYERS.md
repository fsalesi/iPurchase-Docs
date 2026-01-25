# CODE_LIST_MRP_BUYERS - iPurchase System Setting

**Category:** Inventory & MRP

Only use this setting if you want to have a different buyer list show up in the MRP Action Center.

### How It Works

This setting configures inventory & mrp behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_MRP_BUYERS |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_MRP_BUYERS'
```
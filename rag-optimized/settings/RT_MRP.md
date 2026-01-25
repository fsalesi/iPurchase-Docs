# RT_MRP - iPurchase System Setting

**Category:** Inventory & MRP

Comma-separated req types.

### How It Works

This setting configures inventory & mrp behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_MRP |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_MRP'
```
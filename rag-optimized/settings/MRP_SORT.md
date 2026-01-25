# MRP_SORT - iPurchase System Setting

**Category:** Inventory & MRP

Sort field for MRP (Material Requirements Planning) item listings.

### How It Works

This setting configures inventory & mrp behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MRP_SORT |
| **Category** | Inventory & MRP |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MRP_SORT'
```
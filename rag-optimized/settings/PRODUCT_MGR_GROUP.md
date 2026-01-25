# PRODUCT_MGR_GROUP - iPurchase System Setting

**Category:** Custom/Product Management

Group ID for product managers.

### How It Works

This setting configures custom/product management behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PRODUCT_MGR_GROUP |
| **Category** | Custom/Product Management |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PRODUCT_MGR_GROUP'
```
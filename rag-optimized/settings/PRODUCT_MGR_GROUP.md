# PRODUCT_MGR_GROUP - iPurchase System Setting

**Category:** Custom/Product Management

Group ID for product managers. Customer-specific product management setting.

### How It Works

See the description above for valid values and usage.

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

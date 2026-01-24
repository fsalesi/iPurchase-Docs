# PRODUCT_MGR_GROUP - iPurchase System Setting

**Category:** Custom/Product Management

Group ID for product managers. Customer-specific product management setting.

**Common questions this answers:**
- What is PRODUCT_MGR_GROUP?
- What does PRODUCT_MGR_GROUP do?
- What is the default value for PRODUCT_MGR_GROUP?
- How do I configure PRODUCT_MGR_GROUP?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PRODUCT_MGR_GROUP |
| **Category** | Custom/Product Management |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PRODUCT_MGR_GROUP'
```

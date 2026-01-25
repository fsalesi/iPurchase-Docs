# SIG_AVL_REQ_TYPES - iPurchase System Setting

**Category:** Catalog & Vendors

Comma-separated types.

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SIG_AVL_REQ_TYPES |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SIG_AVL_REQ_TYPES'
```
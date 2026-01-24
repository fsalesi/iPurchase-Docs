# AVL_REQ_TYPES - iPurchase System Setting

**Category:** Catalog & Vendors

Comma-separated requisition types. Requisition types that require Approved Vendor List validation. Related: SIG_AVL_REQ_TYPES, USE_SIG_AVL

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AVL_REQ_TYPES |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AVL_REQ_TYPES'
```

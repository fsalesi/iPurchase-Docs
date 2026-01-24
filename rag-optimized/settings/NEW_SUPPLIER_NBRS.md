# NEW_SUPPLIER_NBRS - iPurchase System Setting

**Category:** Catalog & Vendors

Comma separated list of supplier numbers which should not allow final approval.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NEW_SUPPLIER_NBRS |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NEW_SUPPLIER_NBRS'
```
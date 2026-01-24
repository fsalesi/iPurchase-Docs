# PUNCHOUT_RETRY - iPurchase System Setting

**Category:** Catalog & Vendors

Numeric. Number of retry attempts for failed punchout connections.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_RETRY |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | 3 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_RETRY'
```

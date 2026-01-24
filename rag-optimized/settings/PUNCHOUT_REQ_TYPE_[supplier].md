# PUNCHOUT_REQ_TYPE_[supplier] - iPurchase System Setting

**Category:** Catalog & Vendors

This setting allows the administrator to set a default requisition type by supplier for punchout requisitions.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_REQ_TYPE_[supplier] |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_REQ_TYPE_[supplier]'
```
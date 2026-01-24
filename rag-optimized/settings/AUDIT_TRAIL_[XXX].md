# AUDIT_TRAIL_[XXX] - iPurchase System Setting

**Category:** Uncategorized

There are several settings all beginning with "AUDIT_TRAIL". These setting should not be updated as they have to do with the internals of the Audit Trail Inquiry.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TRAIL_[XXX] |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TRAIL_[XXX]'
```
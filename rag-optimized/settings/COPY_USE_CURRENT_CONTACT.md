# COPY_USE_CURRENT_CONTACT - iPurchase System Setting

**Category:** Uncategorized

This setting allows the system to use the current supplier data from the ERP system when a requisition is copied instead of the supplier data coming from the requisition that is being copied.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | COPY_USE_CURRENT_CONTACT |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'COPY_USE_CURRENT_CONTACT'
```

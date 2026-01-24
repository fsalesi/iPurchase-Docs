# ALLOW_NEGATIVE_REQ - iPurchase System Setting

**Category:** User Management

This setting will allow negative total requisition cost if set to True.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_NEGATIVE_REQ |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_NEGATIVE_REQ'
```
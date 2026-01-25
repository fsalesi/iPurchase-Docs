# UP_ONLY_APP_LEVEL_EXCLUDED - iPurchase System Setting

**Category:** Change Orders

Comma-separated approval levels.

### How It Works

This setting configures change orders behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | UP_ONLY_APP_LEVEL_EXCLUDED |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UP_ONLY_APP_LEVEL_EXCLUDED'
```

### Related Settings

- [UP_ONLY_REQ_TYPES](UP_ONLY_REQ_TYPES.md)
- [UP_ONLY_RULE](UP_ONLY_RULE.md)
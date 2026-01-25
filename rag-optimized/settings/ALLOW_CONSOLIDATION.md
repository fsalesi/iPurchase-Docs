# ALLOW_CONSOLIDATION - iPurchase System Setting

**Category:** User Management

This setting allows the administrator to turn On or Off the consolidation feature.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This permission setting controls whether users can perform specific actions within the system.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_CONSOLIDATION |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_CONSOLIDATION'
```

### Related Settings

- [ALLOW_BATCH_PO](ALLOW_BATCH_PO.md)
- [ALLOW_BLANKET_RELEASE](ALLOW_BLANKET_RELEASE.md)
- [ALLOW_BUG](ALLOW_BUG.md)
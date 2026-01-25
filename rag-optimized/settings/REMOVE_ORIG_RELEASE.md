# REMOVE_ORIG_RELEASE - iPurchase System Setting

**Category:** Uncategorized

If set to true, this setting will remove the originator from the approver list on blanket release requisitions.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_ORIG_RELEASE |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_ORIG_RELEASE'
```

### Related Settings

- [REMOVE_ORIGINATOR_FROM_GROUP](REMOVE_ORIGINATOR_FROM_GROUP.md)
- [REMOVE_ORIG_CO](REMOVE_ORIG_CO.md)
# BATCH_CREATE_PO_GROUPS - iPurchase System Setting

**Category:** Purchase Orders

Specifies which groups can use batch PO creation functionality.

### How It Works

Users in listed groups can create multiple POs at once using batch processing. Requires ALLOW_BATCH_PO to be enabled.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| Group list | Members can use batch PO creation |
| `*` (asterisk) | Everyone can use batch creation |
| Blank/empty | No one can use batch creation |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BATCH_CREATE_PO_GROUPS |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BATCH_CREATE_PO_GROUPS'
```

### Related Settings

- [ALLOW_BATCH_PO](ALLOW_BATCH_PO.md) - Enable batch PO functionality

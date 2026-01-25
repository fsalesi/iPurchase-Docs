# ALLOW_REQ_ENTRY - iPurchase System Setting

**Category:** User Management

Controls which users can access the requisition entry screen to create new requisitions.

### How It Works

Users in this list see the "New Requisition" option and can create requisitions. Users not in this list can only view existing requisitions (if permitted).

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone can create requisitions (DEFAULT) |
| Blank/empty | No one can create requisitions |
| User/Group list | Only specified users/groups |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_REQ_ENTRY |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_REQ_ENTRY'
```

### Related Settings

- [ALLOW_BATCH_PO](ALLOW_BATCH_PO.md)
- [ALLOW_BLANKET_RELEASE](ALLOW_BLANKET_RELEASE.md)
- [ALLOW_BUG](ALLOW_BUG.md)

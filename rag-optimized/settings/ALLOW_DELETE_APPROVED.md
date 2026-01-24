# ALLOW_DELETE_APPROVED - iPurchase System Setting

**Category:** Approval Workflow

Controls which users can delete requisitions that have already been approved.

### How It Works

Users/groups in this list can delete approved requisitions. This is a sensitive permission - approved reqs may have POs created against them.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| User/Group list | Specified users/groups can delete approved reqs |
| `*` (asterisk) | Everyone can delete (not recommended) |
| Blank/empty | No one can delete approved reqs |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_DELETE_APPROVED |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_DELETE_APPROVED'
```

### Related Settings

- [ALLOW_DELETE_NOT_SUBMITTED](ALLOW_DELETE_NOT_SUBMITTED.md) - Delete draft requisitions
- [ALLOW_DELETE_PROCESSED](ALLOW_DELETE_PROCESSED.md) - Delete processed (PO created) requisitions

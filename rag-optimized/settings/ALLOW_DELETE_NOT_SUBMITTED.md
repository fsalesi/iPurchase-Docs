# ALLOW_DELETE_NOT_SUBMITTED - iPurchase System Setting

**Category:** User Management

Controls which users can delete requisitions that have not yet been submitted.

### How It Works

Users/groups in this list can delete draft (unsubmitted) requisitions. Typically more permissive than ALLOW_DELETE_APPROVED since no approval workflow has started.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| User/Group list | Specified users/groups can delete drafts |
| `*` (asterisk) | Everyone can delete their own drafts |
| Blank/empty | No one can delete drafts |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_DELETE_NOT_SUBMITTED |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_DELETE_NOT_SUBMITTED'
```

### Related Settings

- [ALLOW_DELETE_APPROVED](ALLOW_DELETE_APPROVED.md) - Delete approved requisitions
- [ALLOW_DELETE_PROCESSED](ALLOW_DELETE_PROCESSED.md) - Delete processed requisitions

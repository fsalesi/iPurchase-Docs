# ALLOW_DELETE_PROCESSED - iPurchase System Setting

**Category:** User Management

Controls which users can delete requisitions that have already been approved and converted to purchase orders. This is a sensitive permission as it allows removal of records that have completed the approval process.

### How It Works

When a user attempts to delete a requisition that has been fully approved and has a PO created, the system checks if the user is in this list. Only users in this list can delete processed requisitions.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone can delete processed requisitions |
| Blank/empty | No one can delete processed requisitions |
| User/Group list | Only specified users or groups can delete |

### Common Questions

- What is ALLOW_DELETE_PROCESSED?
- Who can delete approved requisitions?
- How do I allow admins to delete processed reqs?
- Can I restrict requisition deletion?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_DELETE_PROCESSED |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_DELETE_PROCESSED'
```

### Related Settings

- **ALLOW_DELETE_APPROVED** - Delete approved but not yet processed reqs
- **ALLOW_DELETE_NOT_SUBMITTED** - Delete draft requisitions

# ALLOW_APPROVAL_SIMULATION - iPurchase System Setting

**Category:** Approval Workflow

Controls which users can view approval simulation results. Approval simulation shows who would approve a requisition before it's submitted.

### How It Works

Users in this list can click "Simulate Approval" to see the projected approval path without actually submitting the requisition. Useful for testing approval rules or previewing routing.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone can simulate (DEFAULT) |
| Blank/empty | No one can simulate |
| User/Group list | Only specified users/groups |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVAL_SIMULATION |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVAL_SIMULATION'
```

### Related Settings

- [ALLOW_APPROVER_CHANGES](ALLOW_APPROVER_CHANGES.md)
- [ALLOW_APPROVER_CHANGES_ORIGINATOR](ALLOW_APPROVER_CHANGES_ORIGINATOR.md)
- [ALLOW_APPROVER_CHANGES_REMOVE_APPROVER](ALLOW_APPROVER_CHANGES_REMOVE_APPROVER.md)

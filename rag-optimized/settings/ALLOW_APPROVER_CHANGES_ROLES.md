# ALLOW_APPROVER_CHANGES_ROLES - iPurchase System Setting

**Category:** Approval Workflow

Specifies which groups can add approvers to routing. Members can also remove approvers if ALLOW_APPROVER_CHANGES_REMOVE_APPROVER is enabled.

### How It Works

Any member of a group listed here can add approvers to the approval routing. Requires ALLOW_APPROVER_CHANGES = TRUE.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| Group list | Members of listed groups can add approvers |
| Blank/empty | No one can add approvers via roles |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVER_CHANGES_ROLES |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVER_CHANGES_ROLES'
```

### Related Settings

- [ALLOW_APPROVAL_SIMULATION](ALLOW_APPROVAL_SIMULATION.md)
- [ALLOW_APPROVER_CHANGES](ALLOW_APPROVER_CHANGES.md)
- [ALLOW_APPROVER_CHANGES_ORIGINATOR](ALLOW_APPROVER_CHANGES_ORIGINATOR.md)

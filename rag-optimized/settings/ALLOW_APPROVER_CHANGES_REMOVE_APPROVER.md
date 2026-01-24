# ALLOW_APPROVER_CHANGES_REMOVE_APPROVER - iPurchase System Setting

**Category:** Approval Workflow

Controls who can remove approvers from routing. Uses Can-Do list format. Requires ALLOW_APPROVER_CHANGES = TRUE.

### How It Works

Users/groups in this list can remove approvers from the approval routing. If ALLOW_APPROVER_CHANGES_ORIGINATOR is also TRUE, originators can also remove approvers.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| User/Group list | Specified users/groups can remove approvers |
| Blank/empty | No one can remove approvers |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVER_CHANGES_REMOVE_APPROVER |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVER_CHANGES_REMOVE_APPROVER'
```

### Related Settings

- [ALLOW_APPROVER_CHANGES](ALLOW_APPROVER_CHANGES.md) - Master switch (must be TRUE)
- [ALLOW_APPROVER_CHANGES_ROLES](ALLOW_APPROVER_CHANGES_ROLES.md) - Roles that can add approvers

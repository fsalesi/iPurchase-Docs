# ALLOW_APPROVER_CHANGES - iPurchase System Setting

**Category:** Approval Workflow

Master switch controlling whether approvers can be manually added or removed from approval routing. Also enables Force Approval functionality.

### How It Works

When TRUE, the system allows manual modification of approval routing. Additional settings control who can make changes and what types of changes are allowed.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Enable approver changes and Force Approval (DEFAULT) |
| `FALSE` | Disable all manual approver modifications |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVER_CHANGES |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVER_CHANGES'
```

### Related Settings

- [ALLOW_APPROVER_CHANGES_ORIGINATOR](ALLOW_APPROVER_CHANGES_ORIGINATOR.md) - Let originator make changes
- [ALLOW_APPROVER_CHANGES_REMOVE_APPROVER](ALLOW_APPROVER_CHANGES_REMOVE_APPROVER.md) - Allow removing approvers
- [ALLOW_APPROVER_CHANGES_ROLES](ALLOW_APPROVER_CHANGES_ROLES.md) - Roles that can add approvers
- [FORCE_APPROVAL_ROLE_LIST](FORCE_APPROVAL_ROLE_LIST.md) - Roles that can force approval
- [REMOVE_APPROVER_ROLE_LIST](REMOVE_APPROVER_ROLE_LIST.md) - Roles that can remove approvers

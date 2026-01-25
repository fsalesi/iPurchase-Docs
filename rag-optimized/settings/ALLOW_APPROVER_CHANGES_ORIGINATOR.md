# ALLOW_APPROVER_CHANGES_ORIGINATOR - iPurchase System Setting

**Category:** Approval Workflow

Controls whether the requisition originator can add or remove approvers from routing. Requires ALLOW_APPROVER_CHANGES = TRUE.

### How It Works

When TRUE and ALLOW_APPROVER_CHANGES is also TRUE, the person who created the requisition can modify the approval routing by adding or removing approvers.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Originator can modify approvers (DEFAULT) |
| `FALSE` | Originator cannot modify approvers |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVER_CHANGES_ORIGINATOR |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVER_CHANGES_ORIGINATOR'
```

### Related Settings

- [ALLOW_APPROVAL_SIMULATION](ALLOW_APPROVAL_SIMULATION.md)
- [ALLOW_APPROVER_CHANGES](ALLOW_APPROVER_CHANGES.md)
- [ALLOW_APPROVER_CHANGES_REMOVE_APPROVER](ALLOW_APPROVER_CHANGES_REMOVE_APPROVER.md)

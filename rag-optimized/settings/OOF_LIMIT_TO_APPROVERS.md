# OOF_LIMIT_TO_APPROVERS - iPurchase System Setting

**Category:** Approval Workflow

Restricts Out of Office delegation to only users who are themselves approvers. When enabled, users can only delegate to people who have approval authority.

### How It Works

When TRUE, the system filters the delegate selection list to only show users who appear in approval rules or have approval authority. This ensures delegated approvals go to qualified approvers.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Delegates must be approvers |
| `FALSE` | Delegates can be any user (DEFAULT) |

### Common Questions

- What is OOF_LIMIT_TO_APPROVERS?
- Why can't I select certain users as delegates?
- How do I restrict delegation to approvers only?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_LIMIT_TO_APPROVERS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_LIMIT_TO_APPROVERS'
```

### Related Settings

- [ALLOW_OOF](ALLOW_OOF.md) - Enable Out of Office functionality
- [OOF_LIMIT_BY_DEPT](OOF_LIMIT_BY_DEPT.md) - Restrict delegates to same department
- [OOF_LIMIT_BY_DOLLARS](OOF_LIMIT_BY_DOLLARS.md) - Restrict delegates by approval limit

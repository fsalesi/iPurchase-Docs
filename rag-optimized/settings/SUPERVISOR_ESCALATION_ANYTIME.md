# SUPERVISOR_ESCALATION_ANYTIME - iPurchase System Setting

**Category:** Approval Workflow

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | supervisors can approve/reject anytime, not just when pending |
| **FALSE** | Disables this feature |

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_ESCALATION_ANYTIME |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_ESCALATION_ANYTIME'
```

### Related Settings

- [SUPERVISOR_APPROVAL_FIELD](SUPERVISOR_APPROVAL_FIELD.md)
- [SUPERVISOR_ESCALATION_DAYS](SUPERVISOR_ESCALATION_DAYS.md)
- [SUPERVISOR_ESCALATION_LEVEL](SUPERVISOR_ESCALATION_LEVEL.md)

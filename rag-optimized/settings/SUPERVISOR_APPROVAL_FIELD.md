# SUPERVISOR_APPROVAL_FIELD - iPurchase System Setting

**Category:** Approval Workflow

Field name.

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_APPROVAL_FIELD |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | wus_supervisor |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_APPROVAL_FIELD'
```

### Related Settings

- [SUPERVISOR_ESCALATION_ANYTIME](SUPERVISOR_ESCALATION_ANYTIME.md)
- [SUPERVISOR_ESCALATION_DAYS](SUPERVISOR_ESCALATION_DAYS.md)
- [SUPERVISOR_ESCALATION_LEVEL](SUPERVISOR_ESCALATION_LEVEL.md)
# USE_LINE_APPROVALS - iPurchase System Setting

**Category:** Approval Workflow

This setting determines whether supervisors can approve or reject individual line items.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_LINE_APPROVALS |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_LINE_APPROVALS'
```

### Related Settings

- [USE_APP_AMOUNT_OWN_REQS](USE_APP_AMOUNT_OWN_REQS.md)
- [USE_SUPERVISORS_TO_APPROVE](USE_SUPERVISORS_TO_APPROVE.md)
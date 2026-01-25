# DEFAULT_LINES_TO_APPROVED - iPurchase System Setting

**Category:** Approval Workflow

If using Line Approvals, then setting this to a value of TRUE will set each line to Approved (Green) as the default each time the requisition is submitted for approval.

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
| **Setting Name** | DEFAULT_LINES_TO_APPROVED |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_LINES_TO_APPROVED'
```

### Related Settings

- [DEFAULT_LINES_TO_APPROVED_AUTO](DEFAULT_LINES_TO_APPROVED_AUTO.md)

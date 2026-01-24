# USE_LINE_APPROVALS - iPurchase System Setting

**Category:** Approval Workflow

This setting determines whether supervisors can approve or reject individual line items. Only those line items which are approved will be added to the PO. If there are any items which are neither a...

**Common questions this answers:**
- What is USE_LINE_APPROVALS?
- What does USE_LINE_APPROVALS do?
- What is the default value for USE_LINE_APPROVALS?
- How do I configure USE_LINE_APPROVALS?
- How does USE_LINE_APPROVALS affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_LINE_APPROVALS |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_LINE_APPROVALS'
```

**Related settings:** DEFAULT_LINES_TO_APPROVED, DEFAULT_LINES_TO_APPROVED_AUTO
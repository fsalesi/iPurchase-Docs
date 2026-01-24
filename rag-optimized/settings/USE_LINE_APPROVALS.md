# USE_LINE_APPROVALS - iPurchase System Setting

**Category:** Approval Workflow

This setting determines whether supervisors can approve or reject individual line items. Only those line items which are approved will be added to the PO. If there are any items which are neither approved nor rejected, then the final approval will be disallowed until all items are either approved or rejected.

### How It Works

See the description above for valid values and usage.

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

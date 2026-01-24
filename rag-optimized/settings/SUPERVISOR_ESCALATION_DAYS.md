# SUPERVISOR_ESCALATION_DAYS - iPurchase System Setting

**Category:** Approval Workflow

This is the number of days which must elapse before an approver can Approve or Reject a requisition on behalf of someone else who reports to this given supervisor. See SUPERVISOR_ESCALATION_LEVEL and ALLOW_SUPERVISORS_TO_APPROVE for additional settings related to this one.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_ESCALATION_DAYS |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | 3 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_ESCALATION_DAYS'
```

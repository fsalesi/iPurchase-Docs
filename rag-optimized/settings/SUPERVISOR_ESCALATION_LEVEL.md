# SUPERVISOR_ESCALATION_LEVEL - iPurchase System Setting

**Category:** Approval Workflow

This setting determines how many supervisors up the supervisor tree (organization chart) are allowed to approve or reject a requisition. A value of one will only allow the approver's immediate supervisor to approve. See SUPERVISOR_ESCALATION_DAYS and ALLOW_SUPERVISORS_TO_APPROVE for additional settings related to this one.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_ESCALATION_LEVEL |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 99 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_ESCALATION_LEVEL'
```
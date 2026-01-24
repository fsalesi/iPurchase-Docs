# ALLOW_SUPERVISORS_TO_APPROVE - iPurchase System Setting

**Category:** Approval Workflow

Controls which supervisors can approve or reject requisitions on behalf of their subordinates. This enables a supervisor to step in and handle approvals for employees who report to them, useful when an approver is unavailable or unresponsive.

### How It Works

When enabled, a supervisor can approve or reject requisitions that are pending for any of their direct or indirect reports. This is different from delegation - it doesn't require the subordinate to set up a delegate. The supervisor simply has the authority to act on their behalf based on the organizational hierarchy.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | All supervisors can approve for their subordinates |
| Blank/empty | No supervisor override allowed |
| User/Group list | Only specified users or groups can override (e.g., "managers,directors") |

### Use Case

"My employee is on vacation and has a requisition stuck waiting for their approval. As their manager, I need to approve it to keep the process moving."

### Important Notes

- Creates an audit trail showing who actually approved (supervisor) vs. who was the original approver
- Works in conjunction with SUPERVISOR_ESCALATION_DAYS (waiting period before override is allowed)
- Works in conjunction with SUPERVISOR_ESCALATION_LEVEL (how many levels up can override)
- Separate from delegation - this is authority-based, not delegation-based

### Common Questions

- Can a supervisor approve for their subordinates?
- What is ALLOW_SUPERVISORS_TO_APPROVE?
- How do I enable supervisor override?
- Can managers approve stuck requisitions?
- How does supervisor escalation work?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_SUPERVISORS_TO_APPROVE |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_SUPERVISORS_TO_APPROVE'
```

### Related Settings

- [SUPERVISOR_ESCALATION_DAYS](SUPERVISOR_ESCALATION_DAYS.md) - Days before supervisor can override (default: 3)
- [SUPERVISOR_ESCALATION_LEVEL](SUPERVISOR_ESCALATION_LEVEL.md) - How many levels up can override (default: 99)

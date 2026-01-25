# AUTO_APPROVE_FORWARD - iPurchase System Setting

**Category:** Approval Workflow

Controls whether subsequent approval instances are automatically approved after a user approves once. When enabled, if the same approver appears multiple times in the routing, the system will auto-approve all remaining instances after their first approval.

### How It Works

When a user approves a requisition and they appear again later in the approval chain (either directly or through group membership), the system automatically approves those subsequent instances. This prevents the same person from having to click approve multiple times on the same requisition.

**Important Exception:** The system will NOT auto-approve if the user is the FINAL approver in the chain - they must explicitly click approve for the last step.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `TRUE` | Enable auto-forward for all users |
| `FALSE` | Disable - users must approve each instance manually |
| User/Group list | Enable for specific users/groups only |

### Example

```
Routing: Jane (seq 100) -> Bob (seq 200) -> Jane (seq 300) -> Jane (seq 400 FINAL)

Jane approves at seq 100
-> Seq 300 auto-approved (AUTO_APPROVE_FORWARD)
-> Seq 400 NOT auto-approved (final approver exception - Jane must click)
```

### Group Membership Behavior

- If routing includes a group (e.g., "Managers") and Jane is a member
- Jane's approval satisfies the group requirement
- If Jane appears again later (directly or via another group), auto-forward still applies

### Common Questions

- What is AUTO_APPROVE_FORWARD?
- Why do I have to approve twice?
- How do I enable automatic approval forwarding?
- Why didn't the last approval auto-approve?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_APPROVE_FORWARD |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_APPROVE_FORWARD'
```

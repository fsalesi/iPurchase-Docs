# MULTIPLE_APPROVALS - iPurchase System Setting

**Category:** Approval Workflow

Controls how duplicate approvers are handled when the same user or group appears multiple times in a requisition's approval routing.

### Valid Values

| Value | Behavior |
|-------|----------|
| **KEEP_ALL** | Keep every instance - approver must approve at each occurrence |
| **KEEP_FIRST** | Keep only the first occurrence, remove later duplicates |
| **KEEP_LAST** | Keep only the last occurrence, remove earlier duplicates (DEFAULT) |

### How It Works

When approval rules are evaluated, the same approver may be added to the routing multiple times. For example, if John is both the cost center manager and project manager for a requisition, he could appear twice. This setting determines which approval record(s) are kept.

**Example:**
```
Routing results in: Jane (seq 100), Bob (seq 200), Jane (seq 300)

KEEP_ALL:   Jane approves at 100, Bob at 200, Jane approves again at 300
KEEP_FIRST: Jane approves at 100, Bob at 200 (Jane's seq 300 removed)
KEEP_LAST:  Bob approves at 200, Jane approves at 300 (Jane's seq 100 removed)
```

### Why KEEP_LAST is Recommended

- Later rules typically represent higher authority levels
- Ensures approval at the highest applicable level
- Avoids redundant approvals that slow down processing
- Most organizations want final approval at the highest level, not earliest

### Common Questions

- What is MULTIPLE_APPROVALS?
- What does MULTIPLE_APPROVALS do?
- How do I handle duplicate approvers in routing?
- Why does the same person appear twice in approval routing?
- Should I use KEEP_ALL, KEEP_FIRST, or KEEP_LAST?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MULTIPLE_APPROVALS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | KEEP_LAST |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MULTIPLE_APPROVALS'
```

### Related Settings

- [AUTO_APPROVE_FORWARD](AUTO_APPROVE_FORWARD.md) - Automatically approves future instances after first approval
- **REMOVE_APPROVER_FROM_GROUPS** - Controls group membership handling in routing

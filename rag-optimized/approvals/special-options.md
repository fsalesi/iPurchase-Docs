# Special Approval Rule Options - iPurchase

**Purpose:** Advanced rule options for stop processing, notifications, and temporary changes.

### Stop Processing

When enabled, if this rule matches and is approved, no further rules are evaluated.

**Use Case:** "If the CEO approves, we're done—don't need Board approval too."

| Rule | Approver | Stop | Effect |
|------|----------|------|--------|
| CEO Approval | ceo_group | Yes | If CEO approves, skip remaining rules |
| Board Approval | board_group | No | Only reached if CEO rule doesn't match |

**When to Use:**
- Executive approvals where higher authority supersedes lower
- Special project approvals that bypass normal chain
- Emergency purchase approvals

### Notify Only

Rule generates a notification email but **not** an approval requirement.

**Use Case:** "FYI to Finance for any req over $50K"

| Rule | Approver | Notify Only | Effect |
|------|----------|-------------|--------|
| Finance FYI | finance_notify | Yes | Email sent, no approval needed |

**Important:** Notify-only rules are evaluated AFTER the requisition is fully approved and the PO is created. They don't appear in the approval chain.

**Common Uses:**
- FYI to department heads for large purchases
- Compliance notifications
- Budget tracking alerts

### Active Flag

Temporarily disable a rule without deleting it.

**Use Cases:**
- Testing new rules before going live
- Seasonal changes (holiday policies)
- Temporary policy changes during audits
- Troubleshooting approval issues

**Best Practice:** Instead of deleting rules you might need again, set Active = FALSE.

### Validation Rules (MESSAGE:)

Block submission instead of routing for approval. Set Approver to start with "MESSAGE:".

**Example:**
```
Approver: "MESSAGE:Cost center 8100 requires a project code"
```

**Use Cases:**
- Enforce data quality before routing
- Block prohibited combinations
- Require attachments for certain types

### Common Questions

- How do I make CEO approval the final approval?
- How do I send FYI notifications without requiring approval?
- How do I temporarily disable an approval rule?
- How do I block submission if certain conditions aren't met?

### Related Settings

- [NO_APPROVAL_EMAILS](../settings/NO_APPROVAL_EMAILS.md) - Disable approval emails globally

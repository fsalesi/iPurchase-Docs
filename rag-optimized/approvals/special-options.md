# Special Approval Rule Options - iPurchase

**Purpose:** Advanced rule options: stop processing, notify only, active flag, and validation rules.

### Stop Processing

When enabled, if this rule matches and is approved, no further rules are evaluated.

**Use Case:** "If the CEO approves, we're done—don't need Board approval too."

| Rule | Approver | Stop | Effect |
|------|----------|------|--------|
| CEO Approval | ceo_group | Yes | If CEO approves, skip remaining rules |
| Board Approval | board_group | No | Only reached if CEO rule doesn't match |

### Notify Only

Rule generates a notification email but **not** an approval requirement.

**Use Case:** "FYI to Finance for any req over $50K"

| Rule | Approver | Notify Only | Effect |
|------|----------|-------------|--------|
| Finance FYI | finance_notify | Yes | Email sent, no approval needed |

**Important:** Notify-only rules are evaluated AFTER the requisition is fully approved and the PO is created.

### Active Flag

Temporarily disable a rule without deleting it.

**Use Case:** Testing new rules, seasonal changes, temporary policy changes

---

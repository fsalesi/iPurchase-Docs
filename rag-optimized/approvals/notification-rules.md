# Notification Rules - iPurchase FYI Emails

**Purpose:** Rules that send FYI notifications after approval without requiring approval action (xxapp_notify = TRUE).

### Overview
Rules that don't require approval - recipients are CC'd on final PO email for visibility only.

### Configuration
- Set `xxapp_notify = true` (simple rules) or `xxAR_notify = true` (complex rules)
- Use any sequence number (doesn't matter since evaluated separately)

### Evaluation
1. Ignored completely during approval workflow (Phases 1 & 2)
2. Only evaluated AFTER requisition is fully approved and converted to PO
3. Conditions evaluated against CURRENT req data (after all changes)
4. Matching approvers added as CC recipients on PO notification email

### Use Cases
- "Finance wants to see all POs over $50K" (visibility, not approval)
- "Notify department head of all capital purchases"
- "CC procurement manager on all reqs from specific cost centers"

### Email Recipients
- TO: Originator (OBO) + Buyer
- CC: Anyone matching notification rules

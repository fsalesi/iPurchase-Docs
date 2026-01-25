# Delegation System - iPurchase

**Purpose:** How users can delegate approval authority to others, including out-of-office and chained delegation.

### Overview
Users can designate a delegate to act on their behalf for approvals and other system actions. See delegation-and-permissions.md for complete details.

### Core Mechanism

**Field:** `wus_mstr.wus_delegate`
- User ID of person who can act on your behalf
- One delegate at a time
- Schedule-based (controlled by OOF settings)

### Approval Queue Display

Delegates see both their own and their delegator's requisitions:
- "Pending Peter" - Approving on behalf of Peter
- "Pending Frank" - Approving on behalf of Frank
- No label - Approving as themselves

### Audit Trail

When Bob approves on Jane's behalf:
- `xxreq_audit.xxreq_app_id` = "Jane" (who was required to approve)
- `xxreq_audit.xxreq_actual_approver` = "Bob" (who actually clicked)

### Chained Delegation

**System Setting:** `USE_CHAINED_DELEGATES`
- TRUE: If Jane delegates to Bob, and Bob delegates to Sue, then Sue can act for Jane
- FALSE: Only direct delegation (Sue can act for Bob, but not Jane)

# Supervisor Chain Variables - iPurchase Approval Routing

**Purpose:** Dynamically determine approvers based on the organizational hierarchy ($SUPERVISORS, $FIRST_SUPERVISOR, $LAST_SUPERVISOR).

### Overview

Supervisor chain variables dynamically determine approvers based on the organizational hierarchy defined in user records (wus_supervisor field).

| Variable | Behavior |
|----------|----------|
| `$SUPERVISORS` | Routes up the chain until someone with sufficient approval limit is found |
| `$FIRST_SUPERVISOR` | Routes to immediate supervisor only |
| `$LAST_SUPERVISOR` | Skips to the supervisor with sufficient approval limit |

### Cross-Department Charging Scenario

**Problem:** A purchasing clerk creates a requisition for office supplies that will be charged to 7 different departments. Who approves?

**Solution:** Use `$FIRST_SUPERVISOR` to ensure the requisitioner's supervisor approves first, then route to each department for their portion.

**Example Rule:**

| Rule Name | Approver | Eval Lines | Description |
|-----------|----------|------------|-------------|
| Originator-Supervisor | $FIRST_SUPERVISOR | No | Requisitioner's boss approves first |
| Dept-Approval | $ROLE:Manager | Yes | Each line routes to its cost center's manager |

### Evaluate by Lines vs. Header

**Header (Total Requisition Cost):**
- Amount comparison uses the total requisition value
- One approval record per rule match
- Best for: "Total req over $10K needs VP approval"

**Line (Evaluate Each Line):**
- Each line is evaluated separately
- Can create multiple approval records from one rule
- Best for: Cross-department charging, line-specific approvers

**Example:** $50K requisition with 5 lines across 5 departments

| Setting | Result |
|---------|--------|
| Eval Lines = No | One approval routed based on $50K total |
| Eval Lines = Yes | Five approvals, one per department based on each line's amount |

---

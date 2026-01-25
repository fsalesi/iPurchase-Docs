# Supervisor Chain Variables - iPurchase Approval Routing

**Purpose:** Dynamically determine approvers based on the organizational hierarchy.

Supervisor chain variables route approvals based on the `wus_supervisor` field in user records, automatically following the org chart.

### Available Variables

| Variable | Behavior |
|----------|----------|
| `$SUPERVISORS` | Routes up the chain until someone with sufficient approval limit is found |
| `$FIRST_SUPERVISOR` | Routes to immediate supervisor only |
| `$LAST_SUPERVISOR` | Skips to the supervisor with sufficient approval limit |

### How It Works

The supervisor chain is defined in the `wus_mstr` table. Each user's `wus_supervisor` field points to their manager, creating a hierarchy:

```
Employee (wus_supervisor = "manager1")
  → Manager1 (wus_supervisor = "director1") 
    → Director1 (wus_supervisor = "vp1")
      → VP1 (wus_supervisor = "ceo")
```

### $SUPERVISORS - Full Chain Until Authority Found

Routes through each level until finding someone whose `wus_app_amt` (approval amount limit) is sufficient.

**Example:** $15,000 requisition
- Employee's supervisor (Manager, limit $5,000) - insufficient, continue
- Manager's supervisor (Director, limit $25,000) - sufficient, stops here

### $FIRST_SUPERVISOR - Immediate Manager Only

Always routes to just the immediate supervisor, regardless of amount.

**Use case:** Requisitioner's supervisor should always see the request first, even if they can't fully approve it.

### $LAST_SUPERVISOR - Skip to Final Authority

Jumps directly to the supervisor with sufficient approval authority, skipping intermediate levels.

**Use case:** Fast-track high-dollar approvals to the decision-maker.

### Cross-Department Charging Example

**Problem:** A clerk creates a requisition charged to 7 different departments. Who approves?

**Solution:** 
```
Rule 1: $FIRST_SUPERVISOR (Eval Lines = No)
  → Requisitioner's boss approves first

Rule 2: $ROLE:Manager (Eval Lines = Yes)  
  → Each line routes to its cost center's manager
```

### Evaluate by Lines vs Header

| Setting | Behavior |
|---------|----------|
| **Eval Lines = No** | One approval based on total requisition amount |
| **Eval Lines = Yes** | Separate approval for each line (useful for cross-department) |

### Common Questions

- How do I route approvals based on the org chart?
- What's the difference between $SUPERVISORS and $FIRST_SUPERVISOR?
- How do I handle cross-department requisitions?
- How does the approval limit (wus_app_amt) affect routing?

### Related Fields

- `wus_supervisor` - User's manager (creates the chain)
- `wus_app_amt` - User's approval amount limit

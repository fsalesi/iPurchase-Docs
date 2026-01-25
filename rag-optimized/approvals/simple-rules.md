# Simple Approval Rules (xxapp_mstr) - iPurchase

**Purpose:** Cost center-based approvals with straightforward AND conditions.

Simple rules are stored in the `xxapp_mstr` table and are ideal when:
- Approval is based on cost center ownership
- All conditions must be true (AND logic only)
- You need straightforward "if this, then that" routing
- The bulk of your expense and capital requisitions

### Typical Setup for Expense/Capital Requisitions

For each cost center, you typically need 4-5 rules to handle the approval hierarchy:

**Example: Cost Center 8100 (Marketing Department)**

| Seq | Description | Approver | Min Amount | Max Amount | Cost Center |
|-----|-------------|----------|------------|------------|-------------|
| 200 | CC8100 Supervisor | cc8100_supervisor | $0 | $999.99 | 8100 |
| 250 | CC8100 Manager | cc8100_manager | $1,000 | $4,999.99 | 8100 |
| 300 | CC8100 Director | cc8100_director | $5,000 | $24,999.99 | 8100 |
| 400 | CC8100 VP | cc8100_vp | $25,000 | $99,999.99 | 8100 |

Rules at $100,000+ should typically be handled by Complex Rules for executive approvals.

### Amount Range Strategy

**Approach 1: Strict Ranges (Only Matching Level Approves)**

Set each level's maximum to just below the next level's minimum. A $50,000 requisition would only need VP approval (one approval).

**Approach 2: Open Ranges (Full Chain Approval)**

Set maximum to $9,999,999 for all levels. A $50,000 requisition goes through Supervisor → Manager → Director → VP (four approvals in sequence). Use when you want full visibility up the chain.

### Configuration Tips

**Sequence Number Strategy:** Group rules by approval level, not cost center:
- 200-249: All Supervisors
- 250-299: All Managers  
- 300-399: All Directors
- 400-499: All VPs
- 500+: Executive rules (use Complex Rules)

**Which Cost Field - Header vs Line:**
- **Header**: Compares total requisition amount, creates one approval record
- **Line**: Compares each line item separately, can create multiple approval records (useful for cross-department charging)

### Common Questions

- How do I set up cost center approval rules?
- What's the difference between Header and Line cost evaluation?
- How should I number my approval rule sequences?
- Should all levels approve or just the final authority level?

### Related Settings

- [MULTIPLE_APPROVALS](../settings/MULTIPLE_APPROVALS.md) - How duplicate approvers are handled

# Complex Approval Rules (xxAppRule) - iPurchase

**Purpose:** Executive approvals, OR conditions, and scenarios that can't be handled by simple AND logic.

Complex rules are stored in the `xxAppRule` table (with conditions in `xxAppField`) and are essential when:
- Approval is NOT based on cost center (executive approvals)
- You need OR conditions (this OR that)
- Amount thresholds cross organizational boundaries
- You need line-by-line evaluation with different approvers per line
- Validation rules that block submission

### Executive-Level Approvals

Executives (CFO, CEO, Board) typically don't care about cost centers—they care about **total amount** and **requisition type**.

**Example: Executive Approval Rules**

| Rule Name | Approver | Min Amount | Max Amount | Type |
|-----------|----------|------------|------------|------|
| CFO-Expense | cfo_group | $100,000 | $499,999 | Expense |
| CFO-Capital | cfo_group | $100,000 | $499,999 | Capital |
| CEO-All | ceo_group | $500,000 | $999,999 | * (all types) |
| Board-All | board_group | $1,000,000 | (none) | * (all types) |

**Why Complex Rules for Executives:**
- No cost center filter needed—they approve based on amount alone
- Can use OR conditions if needed
- Keeps executive rules separate from hundreds of cost center rules

### Inventory Requisitions

Inventory requisitions typically follow a simpler, shorter approval path:

| Rule Name | Approver | Min Amount | Max Amount | Type |
|-----------|----------|------------|------------|------|
| INV-Buyer | $xxreq_buyer | $0 | $9,999 | Inventory |
| INV-PurchMgr | purchasing_manager | $10,000 | (none) | Inventory |

Inventory is pre-budgeted (part of production planning), so fewer approval layers = faster procurement.

### Using the Conditions Editor

Complex rules support nested AND/OR logic:

```
AND
├── Type = "Expense" OR Type = "Capital"
├── Amount >= 100000
└── NOT (Cost Center = "8100")  // Exclude CC 8100 which has special rules
```

### Validation Rules

Complex rules can also serve as validation rules that block submission. Set the Approver field to start with "MESSAGE:" to display an error instead of routing for approval.

**Example:** `MESSAGE:Cost center 8100 requires a project code`

### Common Questions

- When should I use Complex Rules vs Simple Rules?
- How do I set up CFO/CEO approval rules?
- How do I create OR conditions in approval rules?
- How do I exclude certain cost centers from a rule?

### Related Tables

- `xxAppRule` - Rule header with approver, amounts, and settings
- `xxAppField` - Condition tree for AND/OR logic

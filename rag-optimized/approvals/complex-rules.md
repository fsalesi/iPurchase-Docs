# Complex Approval Rules (xxAppRule) - iPurchase

**Purpose:** Executive approvals, OR conditions, and scenarios requiring nested AND/OR logic. Stored in xxAppRule/xxAppField tables.

### When to Use

Complex rules are essential when:
- Approval is NOT based on cost center (executive approvals)
- You need OR conditions (this OR that)
- Amount thresholds cross organizational boundaries
- You need line-by-line evaluation with different approvers per line
- Validation rules that block submission

### Executive-Level Approvals

Executives (CFO, CEO, Board) typically don't care about cost centers—they care about **total amount** and **requisition type**.

**Example: Executive Approval Rules**

| Rule Name | Approver | Min Amount | Max Amount | Type | Conditions |
|-----------|----------|------------|------------|------|------------|
| CFO-Expense | cfo_group | $100,000 | $499,999 | Expense | (none - all expense reqs over $100K) |
| CFO-Capital | cfo_group | $100,000 | $499,999 | Capital | (none - all capital reqs over $100K) |
| CEO-All | ceo_group | $500,000 | $999,999 | * | (none - all types over $500K) |
| Board-All | board_group | $1,000,000 | (none) | * | (none - all types over $1M) |

**Why Complex Rules for Executives?**
- No cost center filter needed—they approve based on amount alone
- Can use OR conditions if needed (e.g., "Expense OR Capital")
- Keeps executive rules separate from the hundreds of cost center rules

### Inventory Requisitions

Inventory requisitions typically follow a simpler, shorter approval path:

**Example: Inventory Approval Rules**

| Rule Name | Approver | Min Amount | Max Amount | Type |
|-----------|----------|------------|------------|------|
| INV-Buyer | $xxreq_buyer | $0 | $9,999 | Inventory |
| INV-PurchMgr | purchasing_manager | $10,000 | (none) | Inventory |

**Why Different?**
- Inventory is pre-budgeted (part of production planning)
- Buyer is already accountable for vendor relationships
- Fewer approval layers = faster procurement

### Using the Conditions Editor

Complex rules support nested AND/OR logic through the Conditions Editor:

```
AND
├── Type = "Expense" OR Type = "Capital"
├── Amount >= 100000
└── NOT (Cost Center = "8100")  // Exclude CC 8100 which has special rules
```

---

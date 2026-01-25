# Simple Approval Rules (xxapp_mstr) - iPurchase

**Purpose:** Cost center-based approvals with straightforward AND conditions. Stored in xxapp_mstr table.

### When to Use

Simple rules are ideal when:
- Approval is based on cost center ownership
- All conditions must be true (AND logic only)
- You need simple "if this, then that" routing
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

**Note:** Rules at $100,000+ should typically be handled by Complex Rules (see next section).

### Amount Range Strategy: Two Approaches

There are two valid strategies for setting amount ranges, each with different approval behavior:

#### Approach 1: Strict Ranges (Only Matching Level Approves)

Set each level's maximum to just below the next level's minimum:

| Seq | Approver | Min Amount | Max Amount | Effect |
|-----|----------|------------|------------|--------|
| 200 | Supervisor | $0 | $999.99 | ONLY approves $0-$999.99 |
| 250 | Manager | $1,000 | $4,999.99 | ONLY approves $1K-$4,999.99 |
| 300 | Director | $5,000 | $24,999.99 | ONLY approves $5K-$24,999.99 |
| 400 | VP | $25,000 | $99,999.99 | ONLY approves $25K-$99,999.99 |

**Result for a $50,000 requisition:** Only the VP approves (one approval).

**Use when:** You want the minimum number of approvals—only the level with authority for that amount.

#### Approach 2: Open Ranges (Full Chain Approval)

Set maximum to a very high number (e.g., $9,999,999) for all levels:

| Seq | Approver | Min Amount | Max Amount | Effect |
|-----|----------|------------|------------|--------|
| 200 | Supervisor | $0 | $9,999,999 | Approves ALL amounts |
| 250 | Manager | $1,000 | $9,999,999 | Approves $1K and above |
| 300 | Director | $5,000 | $9,999,999 | Approves $5K and above |
| 400 | VP | $25,000 | $9,999,999 | Approves $25K and above |

**Result for a $50,000 requisition:** Supervisor → Manager → Director → VP (four approvals in sequence).

**Use when:** You want full visibility up the chain. Even though the Supervisor can't unilaterally approve a $50K requisition, they still review and approve as part of the chain. This ensures every level is aware of significant purchases in their area.

#### Choosing the Right Approach

| Consideration | Strict Ranges | Open Ranges |
|---------------|---------------|-------------|
| Number of approvals | Fewer | More |
| Processing time | Faster | Slower |
| Visibility | Only final approver sees it | Entire chain sees it |
| Audit trail | Single approval | Full chain documented |
| Common use | High-volume, low-risk purchases | Significant expenditures requiring oversight |

Many organizations use a **hybrid approach**: strict ranges for routine purchases under $5K, open ranges for larger amounts where chain visibility is valuable.

### The Cost Center Multiplication Problem

With simple rules, you need rules for **each cost center**. If you have:
- 50 cost centers
- 4 approval levels each
- That's **200 rules** just for expense requisitions

This is where Role-Based Approvals can help (see [Role-Based Approvals](#role-based-approvals)).

### Configuration Tips

#### 1. Sequence Number Strategy

Use a consistent sequence numbering scheme that groups rules by **approval level**, not by cost center:

| Sequence Range | Approval Level |
|----------------|----------------|
| 200-249 | All Supervisors |
| 250-299 | All Managers |
| 300-399 | All Directors |
| 400-499 | All VPs |
| 500-599 | CFO (Complex Rules) |
| 600-699 | CEO (Complex Rules) |
| 700-799 | Board (Complex Rules) |
| 900-999 | Default/Safety Net Rules |

**Why this matters:** When a requisition is evaluated, rules are processed in sequence order. By grouping all supervisors together (seq 200-249), all supervisors across all cost centers approve at the same "level" before any managers are considered. This creates a clean, predictable approval flow.

**Example:**
```
Seq 200: CC8100 Supervisor
Seq 201: CC8200 Supervisor  
Seq 202: CC8300 Supervisor
Seq 250: CC8100 Manager
Seq 251: CC8200 Manager
Seq 252: CC8300 Manager
...
```

#### 2. Which Cost Field: Header vs. Line

The `xxapp_which_cost` field determines whether amount thresholds compare against the total requisition or each line item separately. This is critical for cross-department requisitions.

**See:** [Header vs Line Evaluation](header-vs-line-evaluation.md) for detailed explanation and examples.

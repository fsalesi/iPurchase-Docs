# Approval Strategy Guide

A practical guide to implementing approval workflows in iPurchase. This guide explains when to use each approval methodology, provides real-world examples, and helps you design an efficient approval structure for your organization.

---

## Table of Contents

1. [Overview of Approval Methods](#overview-of-approval-methods)
2. [Simple Rules (xxapp_mstr)](#simple-rules-xxapp_mstr)
3. [Complex Rules (xxAppRule)](#complex-rules-xxapprule)
4. [Role-Based Approvals](#role-based-approvals)
5. [Supervisor Chain Variables](#supervisor-chain-variables)
6. [Approver List Behavior](#approver-list-behavior)
7. [Using Groups Effectively](#using-groups-effectively)
8. [Special Rule Options](#special-rule-options)
9. [The Three Default Rules](#the-three-default-rules)
10. [Putting It All Together](#putting-it-all-together)

---

## Overview of Approval Methods

iPurchase provides multiple approval methodologies, each designed for specific scenarios:

| Method | Best For | Screen |
|--------|----------|--------|
| **Simple Rules** | Cost center-based approvals with straightforward AND conditions | Approval Rules - Simple |
| **Complex Rules** | Executive approvals, cross-department scenarios, OR conditions | Approval Rules |
| **Role-Based** | Organization-wide rules based on job function | User Roles + Simple/Complex Rules |
| **Supervisor Chain** | Dynamic routing based on org chart | Complex Rules with $SUPERVISOR variables |

**Key Principle:** Most organizations use a combination of methods. Simple rules handle the bulk of cost center approvals, while complex rules handle executive-level and special cases.

---

## Simple Rules (xxapp_mstr)

### When to Use

Simple rules are ideal when:
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

This setting determines how the rule's amount thresholds are compared:

**Header (Total Requisition Cost)**
- Compares against the **total requisition amount**
- Creates **one approval record** if the rule matches
- Best for: "If the total req exceeds $10K, VP must approve"

**Line (Individual Line Evaluation)**
- Compares against **each line item's amount separately**
- Can create **multiple approval records** from a single rule
- Best for: Cross-department charging, commodity-specific approvals

**Example Scenario:**

A $15,000 requisition with 3 lines:
- Line 1: $8,000 to Cost Center 8100
- Line 2: $5,000 to Cost Center 8200  
- Line 3: $2,000 to Cost Center 8300

**With "Header" setting:**
- Rule checks: Is $15,000 (total) within my amount range?
- Result: One approval based on total

**With "Line" setting:**
- Rule checks each line separately: Is $8,000 within range? Is $5,000? Is $2,000?
- Result: Could generate up to 3 separate approvals (one per line)

**When to use "Line":**
- Cross-department requisitions where each department should approve their portion
- Different approval requirements based on what's being purchased (by UNSPSC code)
- When you need granular control over who approves what

**When to use "Header":**
- Executive-level rules (CFO approves total spend over $100K)
- Most standard cost center approvals
- When you want simpler, faster routing

---

## Complex Rules (xxAppRule)

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

## Role-Based Approvals

### The Solution to Rule Multiplication

Instead of creating rules for every cost center, assign **roles** to users and create **one rule per role**.

### How It Works

1. **Define Roles:** Manager, Director, VP, etc.
2. **Assign Roles to Users:** Each assignment links a user, role, and cost center
3. **Create One Rule:** "Cost Center Manager must approve $1,000 - $4,999"
4. **System Routes Automatically:** Based on the requisition's cost center, finds the user with that role

### Example Setup

**User Role Assignments (User Roles Screen):**

| User | Role | Cost Center |
|------|------|-------------|
| john.smith | Manager | 8100 |
| john.smith | Manager | 8150 |
| mary.jones | Manager | 8200 |
| bob.wilson | Director | 8100 |
| bob.wilson | Director | 8200 |
| sarah.chen | VP | 81* |
| sarah.chen | VP | 82* |

**Important:** Each row is a separate role assignment. If John Smith is the Manager for both CC 8100 and CC 8150, you need **two rows**—one for each cost center. The system looks up "who is the Manager for this specific cost center" when routing.

**Approval Rules:**

| Seq | Description | Approver | Min Amount | Max Amount |
|-----|-------------|----------|------------|------------|
| 250 | CC Manager | $ROLE:Manager | $1,000 | $4,999 |
| 300 | CC Director | $ROLE:Director | $5,000 | $24,999 |
| 400 | CC VP | $ROLE:VP | $25,000 | $99,999 |

**Result:** 3 rules handle the entire organization instead of potentially hundreds!

### Wildcard Cost Centers

Notice Sarah Chen's VP assignments use wildcards: `81*` and `82*`. This means she's the VP approver for:
- All cost centers starting with 81 (8100, 8110, 8150, etc.)
- All cost centers starting with 82 (8200, 8210, 8250, etc.)

This is powerful for executives who oversee entire divisions.

### The Catch: Exception Handling

Role-based rules work beautifully **until one cost center behaves differently**.

**Scenario:** Cost Center 9999 (Executive Office) requires VP approval for everything over $500.

**Solution:**
1. Exclude CC 9999 from the role-based rules using Can-Do syntax: `!9999,*`
2. Create specific rules for CC 9999

**Example:**

| Seq | Description | Approver | Cost Center Filter |
|-----|-------------|----------|-------------------|
| 250 | CC Manager (except 9999) | $ROLE:Manager | !9999,* |
| 255 | CC9999 VP | vp_exec | 9999 |

---

## Supervisor Chain Variables

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

## Approver List Behavior

### Critical: Comma-Separated Lists Require ALL to Approve

**This is commonly misunderstood:**

When the Approver field contains a comma-separated list, **ALL entities in the list must approve**.

| Approver Value | Behavior |
|----------------|----------|
| `finance` | Any ONE member of the "finance" group can approve |
| `$xxreq_userid,finance` | The originator AND someone from finance must BOTH approve |
| `frank,peter,mary` | Frank AND Peter AND Mary must ALL approve |
| `finance,purchasing` | Someone from finance AND someone from purchasing must BOTH approve |

### Single Group = Any Member

When the Approver is a single group, only ONE member of that group needs to approve:

```
Approver: "ap_approvers"
→ Anyone in the ap_approvers group can approve
```

### Multiple Groups = One from Each

When multiple groups are listed, you need ONE approver from EACH group:

```
Approver: "finance,legal"
→ Need approval from someone in finance AND someone in legal
```

### Dynamic Variables in Lists

```
Approver: "$xxreq_userid,$FIRST_SUPERVISOR"
→ The originator AND their supervisor must both approve
```

---

## Using Groups Effectively

### Why Use Groups (Even with One Member)?

**Always use a group in the Approver field, even if it only has one member.**

**Benefits:**

1. **Easy Personnel Changes:** When Bob retires and Jane takes over, just update the group membership—no rule changes needed
2. **Vacation Coverage:** Add a backup approver to the group temporarily
3. **Audit Trail:** Group membership changes are tracked separately from approval rule changes
4. **Future Flexibility:** Easy to add members later without modifying rules

### Example

**Instead of:**
```
Approver: "bob.wilson"  ❌ Bad - hardcoded user
```

**Use:**
```
Approver: "cc8100_director"  ✅ Good - group with Bob as member
```

When Bob leaves:
- ❌ Bad way: Find all rules with "bob.wilson", update each one
- ✅ Good way: Remove Bob from group, add Jane to group—done!

### Group Naming Conventions

| Pattern | Example | Use Case |
|---------|---------|----------|
| `cc[number]_[role]` | cc8100_manager | Cost center-specific roles |
| `[function]_approvers` | ap_approvers | Functional approvers |
| `[level]_approval` | executive_approval | Level-based groups |

---

## Special Rule Options

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

## The Three Default Rules

iPurchase includes three default rules that serve as safety nets:

### 1. Buyer Approval (Sequence ~900)

```
Description: "Buyer must approve"
Approver: $xxreq_buyer
Conditions: Requisition has a buyer assigned
```

**Purpose:** Ensures the assigned buyer reviews and approves before PO creation.

### 2. Originator Cannot Self-Approve (Sequence ~990)

```
Description: "Originator cannot be only approver"
Type: Validation Rule
Conditions: All approvers = originator
```

**Purpose:** Prevents someone from creating and approving their own requisition without oversight.

### 3. Must Have At Least One Approver (Sequence ~999)

```
Description: "Requisition must have at least one approver"
Type: Validation Rule
Conditions: Approval routing is empty
```

**Purpose:** Catches requisitions that fell through the cracks—no rules matched.

**Why These Exist:**
- **Safety Net:** Catches configuration gaps
- **Compliance:** Ensures segregation of duties
- **Audit Requirements:** No requisition should bypass all approvals

---

## Putting It All Together

### Recommended Approval Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    APPROVAL FLOW                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. VALIDATION RULES (Seq -999 to -1)                      │
│     └─ Block submission if conditions not met              │
│                                                             │
│  2. COST CENTER RULES (Seq 200-499)                        │
│     └─ Seq 200-249: Supervisors                            │
│     └─ Seq 250-299: Managers                               │
│     └─ Seq 300-399: Directors                              │
│     └─ Seq 400-499: VPs                                    │
│                                                             │
│  3. EXECUTIVE RULES (Seq 500-799)                          │
│     └─ Seq 500-599: CFO                                    │
│     └─ Seq 600-699: CEO                                    │
│     └─ Seq 700-799: Board                                  │
│                                                             │
│  4. SPECIAL RULES (Seq 800-899)                            │
│     └─ Inventory, special projects, exceptions             │
│                                                             │
│  5. DEFAULT RULES (Seq 900-999)                            │
│     └─ Buyer approval, safety nets                         │
│                                                             │
│  6. NOTIFY RULES (Seq 1000+)                               │
│     └─ FYI notifications after approval                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Example: Complete Expense Requisition Setup

**Simple/Role-Based Rules (Cost Center Level):**
- Seq 200-249: Cost Center supervisors ($0 - $999)
- Seq 250-299: Cost Center managers ($1,000 - $4,999)
- Seq 300-399: Cost Center directors ($5,000 - $24,999)
- Seq 400-499: Cost Center VPs ($25,000 - $99,999)

**Complex Rules (Executive Level):**
- Seq 500: CFO approval ($100,000 - $499,999)
- Seq 600: CEO approval ($500,000 - $999,999)
- Seq 700: Board approval ($1,000,000+)

**Default Rules:**
- Seq 900: Buyer approval
- Seq 990: Self-approval prevention
- Seq 999: Empty routing prevention

### Migration Path: Simple to Role-Based

If you have hundreds of simple rules and want to consolidate:

1. **Identify Patterns:** Which rules follow the same structure?
2. **Create Roles:** Define Manager, Director, VP roles
3. **Assign Users:** Map users to roles for their cost centers (one row per user/cost center combination)
4. **Create Role Rules:** One rule per role level
5. **Handle Exceptions:** Create specific rules for unique cost centers
6. **Disable Old Rules:** Mark old simple rules inactive
7. **Test:** Use Approval Simulation
8. **Clean Up:** Delete old rules after validation

---

## Related Documentation

- [Approval Rules - Complex](../admin/screens/ipurchase-01-approval-rules.md) - Screen documentation
- [Approval Rules - Simple](../admin/screens/ipurchase-02-approval-rules-simple.md) - Screen documentation  
- [User Roles](../admin/screens/ipurchase-03-user-roles.md) - Role assignment screen
- [Approval Systems Reference](approval-systems.md) - Technical details on rule evaluation
- [System Settings Reference](system-settings-reference.md) - Related settings (MULTIPLE_APPROVALS, etc.)

---

*Last Updated: January 2026*

---

## Additional Default Rules

### Buyer as Final Approver

The Buyer approval rule (typically at sequence ~900) ensures the assigned buyer is the **final approver** before the PO is created.

```
Description: "Buyer Final Approval"
Approver: $xxreq_buyer
Sequence: 900
```

**Why Buyer is Last:**
- Buyers work directly with suppliers and know vendor capabilities
- They can verify pricing, lead times, and terms before PO creation
- Final quality check on the requisition before it becomes a purchase order
- Catches any issues that approvers higher in the chain might miss

### On Behalf Of (OBO) Rule

When someone creates a requisition on behalf of another person, the OBO rule ensures the actual budget owner is aware and approves.

```
Description: "OBO must approve when different from creator"
Approver: $xxreq_obo
Conditions: xxreq_userid <> xxreq_obo
```

**Scenario:** An admin assistant (Jane) creates requisitions for their manager (Bob). Even though Jane enters the requisition, Bob is listed as the "On Behalf Of" person because it's his budget.

**Why This Matters:**
- The budget owner (OBO) should always approve their own spending
- Prevents someone from charging to another person's cost center without their knowledge
- Creates accountability—Bob can't claim he didn't know about the purchase
- The rule only triggers when creator ≠ OBO (no duplicate approval when they're the same person)

### Change Order Rule

When a requisition modifies an existing PO (change order), additional approval may be required.

```
Description: "Change Order Approval"
Approver: change_order_approvers (or $xxreq_buyer)
Conditions: xxreq_update_po = TRUE
```

**Change Order Scenarios:**
- Adding lines to an existing PO
- Increasing quantities or prices
- Extending delivery dates
- Modifying terms

**Why Separate Rules:**
- Change orders may need different approvers than original requisitions
- Some organizations require the original approvers to re-approve
- Others have a dedicated change order approval group
- Prevents unauthorized modifications to committed purchases

**Related Settings:**
- `CO_TOLERANCE_PCT` - Percentage change allowed without re-approval
- `CO_TOLERANCE_AMT` - Dollar amount change allowed without re-approval
- `CO_REQUIRE_REAPPROVAL` - Force full re-approval on any change

---

*Last Updated: January 2026*

*Last Updated: January 2026*

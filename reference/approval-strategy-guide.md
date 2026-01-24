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
| 100 | CC8100 Supervisor | john.smith | $0 | $999.99 | 8100 |
| 101 | CC8100 Manager | mary.jones | $1,000 | $4,999.99 | 8100 |
| 102 | CC8100 Director | bob.wilson | $5,000 | $24,999.99 | 8100 |
| 103 | CC8100 VP | sarah.chen | $25,000 | $99,999.99 | 8100 |

**Note:** Rules at $100,000+ should typically be handled by Complex Rules (see next section).

### The Cost Center Multiplication Problem

With simple rules, you need rules for **each cost center**. If you have:
- 50 cost centers
- 4 approval levels each
- That's **200 rules** just for expense requisitions

This is where Role-Based Approvals can help (see [Role-Based Approvals](#role-based-approvals)).

### Configuration Tips

1. **Use Amount Ranges:** Set both minimum and maximum amounts to prevent overlap
2. **Sequence Numbers:** Use a consistent numbering scheme (e.g., 100-199 for CC 8100, 200-299 for CC 8200)
3. **Which Cost Field:** Use "Header" for total requisition cost, "Line" for line-by-line evaluation

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
2. **Assign Roles to Users:** 
   - John Smith is "Manager" for Cost Center 8100
   - Mary Jones is "Manager" for Cost Center 8200
3. **Create One Rule:**
   - "Cost Center Manager must approve $1,000 - $4,999"
   - System automatically routes to the right person based on cost center

### Example Setup

**User Role Assignments (User Roles Screen):**

| User | Role | Cost Center |
|------|------|-------------|
| john.smith | Manager | 8100 |
| mary.jones | Manager | 8200 |
| bob.wilson | Director | 8100,8200 |
| sarah.chen | VP | 81*,82* |

**Approval Rules:**

| Seq | Description | Approver | Min Amount | Max Amount |
|-----|-------------|----------|------------|------------|
| 100 | CC Manager | $ROLE:Manager | $1,000 | $4,999 |
| 200 | CC Director | $ROLE:Director | $5,000 | $24,999 |
| 300 | CC VP | $ROLE:VP | $25,000 | $99,999 |

**Result:** 3 rules instead of potentially hundreds!

### The Catch: Exception Handling

Role-based rules work beautifully **until one cost center behaves differently**.

**Scenario:** Cost Center 9999 (Executive Office) requires VP approval for everything over $500.

**Solution:**
1. Exclude CC 9999 from the role-based rules using Can-Do syntax: `!9999,*`
2. Create specific rules for CC 9999

**Example:**

| Seq | Description | Approver | Cost Center Filter |
|-----|-------------|----------|-------------------|
| 100 | CC Manager (except 9999) | $ROLE:Manager | !9999,* |
| 150 | CC9999 VP | vp_exec | 9999 |

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
│  2. SIMPLE RULES - Cost Center Based (Seq 1-499)           │
│     └─ Supervisor → Manager → Director (by CC)             │
│     └─ OR use Role-Based rules                             │
│                                                             │
│  3. COMPLEX RULES - Executive (Seq 500-799)                │
│     └─ CFO → CEO → Board (by amount, not CC)               │
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

**Simple Rules (Cost Center Level):**
- Seq 100-199: Cost Center supervisors ($0 - $999)
- Seq 200-299: Cost Center managers ($1,000 - $4,999)
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
3. **Assign Users:** Map users to roles for their cost centers
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

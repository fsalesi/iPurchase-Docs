# Role-Based Approvals - iPurchase

**Purpose:** Reduce rule maintenance by using roles instead of creating rules for every cost center.

Instead of creating separate approval rules for every cost center (which can mean hundreds of rules), assign **roles** to users and create **one rule per role**.

### The Problem: Rule Multiplication

With simple rules, you need rules for each cost center:
- 50 cost centers × 4 approval levels = **200 rules** just for expense requisitions

### The Solution: Role-Based Rules

1. **Define Roles:** Manager, Director, VP, etc.
2. **Assign Roles to Users:** Each assignment links a user, role, and cost center
3. **Create One Rule:** "Cost Center Manager must approve $1,000 - $4,999"
4. **System Routes Automatically:** Based on requisition's cost center, finds user with that role

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

**Important:** Each row is a separate assignment. If John manages both CC 8100 and 8150, you need two rows.

**Approval Rules using $ROLE variable:**

| Seq | Description | Approver | Min Amount | Max Amount |
|-----|-------------|----------|------------|------------|
| 250 | CC Manager | $ROLE:Manager | $1,000 | $4,999 |
| 300 | CC Director | $ROLE:Director | $5,000 | $24,999 |
| 400 | CC VP | $ROLE:VP | $25,000 | $99,999 |

**Result:** 3 rules handle the entire organization instead of hundreds!

### Wildcard Cost Centers

Sarah Chen's VP assignments use wildcards (`81*`, `82*`), meaning she's the VP approver for all cost centers starting with 81 or 82. Powerful for executives who oversee entire divisions.

### Handling Exceptions

Role-based rules work until one cost center needs different behavior.

**Example:** Cost Center 9999 (Executive Office) requires VP approval for everything over $500.

**Solution:**
1. Exclude CC 9999 from role-based rules using Can-Do: `!9999,*`
2. Create specific rules for CC 9999

| Seq | Description | Approver | Cost Center Filter |
|-----|-------------|----------|-------------------|
| 250 | CC Manager (except 9999) | $ROLE:Manager | !9999,* |
| 255 | CC9999 VP | vp_exec | 9999 |

### Common Questions

- How do I reduce the number of approval rules?
- How do I assign roles to users for specific cost centers?
- What is the $ROLE variable in approval rules?
- How do I handle cost centers that need different approval rules?

### Related

- User Roles screen for assigning roles
- [ROLES](../settings/ROLES.md) setting - defines available role names

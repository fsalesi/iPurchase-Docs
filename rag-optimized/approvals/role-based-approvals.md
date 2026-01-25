# Role-Based Approvals - iPurchase

**Purpose:** Reduce rule maintenance by using roles instead of creating rules for every cost center.

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

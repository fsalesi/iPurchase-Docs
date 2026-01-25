# Duplicate Approver Handling - iPurchase

**Purpose:** How iPurchase handles when the same person appears multiple times in the approval routing (MULTIPLE_APPROVALS setting).

### MULTIPLE_APPROVALS Setting

Controls what happens when same approver appears multiple times in routing.

**Values:**
- `keep_all`: Keep every instance (approver approves multiple times)
- `keep_first`: Keep only first occurrence, remove later duplicates
- `keep_last`: Keep only last occurrence, remove earlier duplicates (DEFAULT)

**Example:**
```
Routing results in: Jane (seq 100), Bob (seq 200), Jane (seq 300)

keep_all:   Jane approves at 100, Bob at 200, Jane approves again at 300
keep_first: Jane approves at 100, Bob at 200 (Jane's seq 300 removed)
keep_last:  Bob approves at 200, Jane approves at 300 (Jane's seq 100 removed)
```

**Why keep_last is typical:**
- Later rules are usually higher authority
- Want approval at highest applicable level
- Avoids redundant approvals

### AUTO_APPROVE_FORWARD Setting

Automatically approves all future instances of an approver after they approve once.

**Values:**
- TRUE: Enable for all users
- FALSE: Disable
- Can-Do list: Enable for specific users/groups only

**Behavior:**
- User approves at first instance
- System automatically approves all other instances in the chain
- **Exception:** Does NOT auto-approve if user is the FINAL approver (must click explicitly)
- Works even if user appears via group membership

**Example:**
```
Routing: Jane (seq 100), Bob (seq 200), Jane (seq 300), Jane (seq 500 - final)

Jane approves at seq 100:
  → Auto-approves seq 300 (not final)
  → Does NOT auto-approve seq 500 (is final, must click)
```

**Group Membership:**
- If routing contains "Managers" group and Jane is a member
- Jane's approval satisfies the group requirement
- If Jane appears again later, AUTO_APPROVE_FORWARD still applies

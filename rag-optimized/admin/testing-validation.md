# Testing & Validation - iPurchase Administration

**Purpose:** How to test approval rules using approval simulation and validate configuration changes.

### Approval Simulation

**Purpose:** Preview who will approve a requisition before submitting

**Enable:**
```sql
ALLOW_APPROVAL_SIMULATION = "*" (everyone can simulate)
ALLOW_APPROVAL_SIMULATION = "buyers,admins" (restricted)
```

**Use Cases:**
- Test new approval rules before activating
- Troubleshoot unexpected routing
- Train users on approval workflows
- Verify rule changes

### Test Scenarios

**Create Test Requisitions:**
1. Small amount ($100) expense req
2. Medium amount ($5,000) expense req
3. Large amount ($50,000) expense req
4. Capital requisition ($25,000)
5. Multi-cost center requisition
6. Requisition for special project
7. Change order within tolerance
8. Change order exceeding tolerance

**Verify:**
- Correct approvers triggered
- Sequence makes sense
- No missing approvals
- No duplicate approvals (unless intended)
- Stop conditions work correctly
- Validation rules block invalid reqs

### Common Issues

**Rule Not Triggering:**
- Check rule is active
- Verify amount is within min/max range
- Confirm ALL conditions match (AND logic)
- Check if earlier stop condition blocked rule
- For complex rules, trace through condition tree

**Wrong Approver:**
- Check variable substitution (is field populated?)
- Verify group membership
- Check for delegation
- Review MULTIPLE_APPROVALS setting

**Too Many Approvals:**
- Review MULTIPLE_APPROVALS setting (should be keep_last usually)
- Check for redundant rules
- Look for unintended group memberships

**Requisition Stuck:**
- Check for missing approver (user doesn't exist)
- Verify approver has system access
- Look for delegation loops
- Check email notifications

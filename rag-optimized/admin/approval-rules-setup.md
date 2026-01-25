# Approval Rules Setup - iPurchase Administration

**Purpose:** Step-by-step guide to creating and configuring approval rules.

### Rule Strategy

**Start Simple:**
1. Begin with 3-5 basic approval rules
2. Test thoroughly
3. Add complexity only as needed
4. Document each rule's purpose

**Common Starting Rules:**
1. Change Order Rule (default - handles PO modifications)
2. OBO Rule (default - routes to requestor if different from creator)
3. Supervisor Chain Rule (routes through org hierarchy by dollar amount)
4. Department/Cost Center Owner Rule (business unit approval)
5. Buyer Rule (default - final purchasing review)

### Creating Simple Rules (Recommended)

**Use Simple Rules (xxapp_mstr) For:**
- Cost center owner approvals
- Dollar threshold approvals
- Department-specific workflows
- Account or project-based routing
- 90%+ of approval scenarios

**Setup Steps:**
1. Determine sequence number (100, 200, 300, etc.)
2. Identify approver (user, group, or variable like $xxreq_obo)
3. Set amount range (min/max)
4. Set filters (type, domain, cost center, account, etc.)
5. Choose cost evaluation mode (Header or Line)
6. Set stop flag (does this rule end the chain?)
7. Test with approval simulation

**Example: Cost Center Owner Approval**
```
Sequence: 100
Approver: $xxreqd_cc_owner (variable - different owner per cost center)
Amount: $0 - $999,999
Type: * (all types)
Cost Center: * (all cost centers)
Which Cost: Line (evaluate sum of lines matching CC)
Stop: No
Notify: No
Description: Route to cost center owner for approval
```

**Note:** Requires cost center owner field in database or mapping table

### Creating Complex Rules

**Use Complex Rules (xxAppRule) For:**
- OR logic requirements
- Nested conditions  
- Line-by-line approval with different approvers
- Validation rules (pre-submission checks)
- Less than 10% of approval scenarios

**Setup Steps:**
1. Document business logic in plain language first
2. Draw out condition tree (AND/OR structure)
3. Create rule header in xxAppRule
4. Build condition tree in xxAppField
5. Test extensively with approval simulation
6. Document thoroughly (complex rules are hard to understand later)

**Example: Capital Approval Over $50K**
```
Rule Name: Capital_CFO
Sequence: 400
Approver: cfo
Amount: $50,000 - $999,999,999

Conditions (all must be true):
  - xxreq_type eq "Capital"
  
Stop: No
Notify: No
```

Even this simple logic should use complex rules if you need variable substitution or OR conditions.

### Validation Rules

**Purpose:** Block submission if required fields missing or invalid combinations entered

**Setup Steps:**
1. Identify validation requirements
2. Create complex rule with negative sequence (-990, -980, etc.)
3. Set approver to "MESSAGE:Your error message here"
4. Define conditions that trigger the error
5. Test by attempting to submit invalid requisitions

**Example Validations:**

**Capital Requires Justification:**
```
Sequence: -990
Approver: MESSAGE:Capital requisitions require business justification
Conditions: xxreq_type eq "Capital" AND xxreq_justification eq ""
```

**Cost Center 8100 Requires Project:**
```
Sequence: -980
Approver: MESSAGE:Cost center 8100 requires project code
Conditions: xxreqd_cc eq "8100" AND xxreqd_project eq ""
```

**Inventory Requires Part Number:**
```
Sequence: -970
Approver: MESSAGE:Inventory requisitions must include part numbers
Conditions: xxreq_type eq "Inventory" AND xxreqd_part eq ""
```

### Notification Rules

**Purpose:** FYI visibility - recipients CC'd on PO email after approval, no approval action required

**Setup Steps:**
1. Create rule (simple or complex)
2. Set notify flag to TRUE
3. Set any sequence number (doesn't matter)
4. Define conditions and approvers

**Example Notifications:**

**Finance Visibility on Large POs:**
```
Sequence: 950
Approver: finance_director
Amount: $50,000 - $999,999,999
Type: *
Notify: YES
Description: CC Finance Director on POs over $50K
```

**Department Head Visibility:**
```
Sequence: 960
Approver: dept_head
Cost Center: 8100,8200,8300
Notify: YES
Description: CC Department Head on all reqs for their cost centers
```

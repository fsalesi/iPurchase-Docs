# Validation Rules - iPurchase Pre-Submission Checks

**Purpose:** Rules that block requisition submission if conditions are not met. Use MESSAGE: prefix in approver field.

### Overview
Pre-submission checks that block requisition submission if conditions match. Only available in xxAppRule system (not xxapp_mstr).

### Identification
- Approver field starts with "MESSAGE:"
- Example: `xxAR_Approver = "MESSAGE:Cost center 8100 requires project code"`

### Execution
1. Run when user clicks "Submit for Approval"
2. Process BEFORE entering approval workflow
3. Evaluate validation rules in sequence order
4. First rule that matches → Display error message, block submission
5. Only process until first error (don't accumulate multiple errors)
6. If all validations pass → Proceed to approval rule evaluation

### Sequence Convention
Use negative sequence numbers to keep separate from approval rules:
- `-990`: First validation (most critical)
- `-980`: Second validation
- `-970`: Third validation
- etc.

Increment by 10 for easy insertion of new validations between existing ones.

### Examples

**Validation: Cost Center Requires Project**
```
Sequence: -990
Approver: MESSAGE:Cost center 8100 requires a project code
Conditions: xxreqd_cc eq "8100" AND xxreqd_project eq ""
```

**Validation: Capital Needs Justification**
```
Sequence: -980
Approver: MESSAGE:Capital requisitions require business justification
Conditions: xxreq_type eq "Capital" AND xxreq_justification eq ""
```

**Validation: Inventory Needs Part Number**
```
Sequence: -970
Approver: MESSAGE:Inventory requisitions must include part numbers
Conditions: xxreq_type eq "Inventory" AND xxreqd_part eq ""
```

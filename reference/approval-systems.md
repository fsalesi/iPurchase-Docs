# iPurchase Approval Systems - Complete Reference

## Overview

iPurchase uses two parallel approval rule systems that share a common sequence number space. Both systems are evaluated together to determine the complete approval routing for a requisition.

**Two Rule Systems:**
1. **Simple Rules (xxapp_mstr)** - Recommended for most cases - straightforward AND-based logic
2. **Complex Rules (xxAppRule + xxAppField)** - For advanced scenarios requiring nested AND/OR conditions

**Rule Types:**
1. **Approval Rules** - Require active approval from designated approvers
2. **Notification Rules** - FYI only, evaluated after PO creation, recipients CC'd on email
3. **Validation Rules** - Pre-submission checks that block submission if conditions match


## Querying Approval Rules by Domain

### Domain Filtering Logic

Approval rules can be configured to apply to:
1. **All domains**: `xxapp_domain = '*'` or `xxAR_Domain = '*'`
2. **Specific domain**: `xxapp_domain = 'demo1'` or `xxAR_Domain = 'demo1'`

When querying rules for a specific domain, you must check for BOTH patterns:

**Simple Rules Query:**
```sql
SELECT *
FROM PUB.xxapp_mstr
WHERE (xxapp_domain = '*' OR xxapp_domain = 'demo1')
  AND xxapp_active = 1
ORDER BY xxapp_seq
```

**Complex Rules Query:**
```sql
SELECT *
FROM PUB.xxAppRule
WHERE (xxAR_Domain = '*' OR xxAR_Domain = 'demo1')
  AND xxAR_Active = 1
ORDER BY xxAR_AppLevel
```

### Joining Complex Rules with Conditions

When retrieving conditions for a complex rule, the domain field is part of the relationship:

```sql
-- Get rule
SELECT *
FROM PUB.xxAppRule
WHERE xxAR_RuleName = 'MyRule'
  AND (xxAR_Domain = '*' OR xxAR_Domain = 'demo1')

-- Get conditions for that rule
SELECT *
FROM PUB.xxAppField
WHERE xxAF_RuleName = 'MyRule'
  AND xxAF_Domain = xxAR_Domain  -- Domain must match the rule's domain
ORDER BY xxAF_Seq
```

**Important:** The `xxAppField` table includes `xxAF_Domain` to link conditions to their parent rule. A rule and its conditions must have matching domain values.

### Example: Finding All Applicable Rules

```sql
-- Find all rules (simple + complex) that apply to demo1
-- Combined query showing both rule types

-- Simple Rules
SELECT 
  xxapp_seq as sequence,
  'SIMPLE' as rule_type,
  xxapp_id as approver,
  xxapp_description as description,
  xxapp_domain as domain
FROM PUB.xxapp_mstr
WHERE (xxapp_domain = '*' OR xxapp_domain = 'demo1')
  AND xxapp_active = 1

UNION ALL

-- Complex Rules  
SELECT
  xxAR_AppLevel as sequence,
  'COMPLEX' as rule_type,
  xxAR_Approver as approver,
  xxAR_RuleName as description,
  xxAR_Domain as domain
FROM PUB.xxAppRule
WHERE (xxAR_Domain = '*' OR xxAR_Domain = 'demo1')
  AND xxAR_Active = 1

ORDER BY sequence
```

## Approval Rule Evaluation Algorithm

### Phase 1: Complex Rules (xxAppRule)

1. Query xxAppRule rules WHERE (xxAR_Domain = '*' OR xxAR_Domain = [req_domain]) in ascending `xxAR_AppLevel` order
2. For each rule where conditions match:
   - Add approver(s) to approval chain
   - If `xxAR_Eval_Lines = true`, may create multiple approval records (one per matching line)
3. If rule has `xxAR_stop = true`:
   - Record stop sequence number
   - Skip remaining xxAppRule rules with higher sequence numbers
   - Proceed to Phase 2
4. If no stop encountered, set stop sequence to infinity

### Phase 2: Simple Rules (xxapp_mstr)

1. Query xxapp_mstr rules WHERE (xxapp_domain = '*' OR xxapp_domain = [req_domain]) AND xxapp_seq <= stop_sequence_from_phase1
2. Process in ascending `xxapp_seq` order
3. For each rule where conditions match:
   - Add approver(s) to approval chain
4. If rule has `xxapp_stop = true`:
   - Record new stop sequence
   - **Delete any xxAppRule approvers from temp table where `xxAR_AppLevel > xxapp_seq`**
   - Stop evaluation

### Phase 3: Notification Rules (After PO Creation)

1. After requisition is fully approved and converted to PO
2. Process ONLY rules where `xxAR_notify = true` OR `xxapp_notify = true`
3. These rules are completely ignored during approval evaluation (Phases 1 & 2)
4. Matching approvers are added as CC recipients on PO email notification
5. Use case: "Finance wants to see all POs over $50K but doesn't need to approve"

### Important Notes

- Both rule systems share the same sequence number space
- Complex rules are evaluated first, then simple rules (up to stop sequence)
- A stop in either system affects both systems
- Notification rules (`notify = true`) are completely separate - only evaluated after PO creation

### Example Execution

**Scenario: Change Order Rule Triggers**
```
xxAppRule:
  Seq 5: Change Order (stop=true) → Triggers, adds buyer
  Seq 450: CFO Rule → Skipped (beyond stop sequence)

xxapp_mstr:
  Seq 100: Cost Center Owner → Skipped (beyond stop sequence of 5)
  Seq 200: Manager → Skipped
  
Result: Only buyer approves (Change Order rule)
```

**Scenario: Change Order Doesn't Trigger**
```
xxAppRule:
  Seq 5: Change Order → Doesn't match
  Seq 450: CFO Rule (stop=false) → Matches, adds CFO
  No stop encountered, stop_seq = infinity

xxapp_mstr:
  Seq 100: Cost Center Owner → Matches, adds owner
  Seq 200: Manager (over $5K) → Matches, adds manager
  Seq 300: VP (over $50K) → Doesn't match (req is $10K)
  
Result: CFO (seq 450) + Cost Center Owner (seq 100) + Manager (seq 200)
```

**Scenario: Stop in xxapp_mstr**
```
xxAppRule:
  Seq 5: OBO Rule → Matches, adds OBO
  Seq 450: CFO Rule (stop=false) → Matches, adds CFO

xxapp_mstr:
  Seq 100: Cost Center Owner (stop=true) → Matches, adds owner, STOPS
  Seq 200: Manager → Skipped
  
System deletes CFO from temp approval table (seq 450 > 100)
Result: OBO (seq 5) + Cost Center Owner (seq 100)
```

## Simple Rules (xxapp_mstr)

### Overview
Straightforward AND-based rules with Can-Do list matching. Recommended for 90%+ of approval scenarios.

### Rule Structure

A requisition matches a simple rule if ALL of the following are true:
1. Amount is within range (`xxapp_amount` to `xxapp_max_amount`)
2. Domain matches (`xxapp_domain` = "*" or matches requisition domain)
3. Type matches (`xxapp_type` = "*" or matches requisition type)
4. ALL specified filter fields match using Can-Do evaluation:
   - `xxapp_acct` (GL account)
   - `xxapp_cc` (Cost center)
   - `xxapp_sub` (Sub-account)
   - `xxapp_po_site` (PO site)
   - `xxapp_line_site` (Line site)
   - `xxapp_orig` (Originator/OBO - can be user IDs or group IDs)
   - `xxapp_project` (Project)
   - `xxapp_unspsc` (UNSPSC commodity code)

### Cost Evaluation Modes (xxapp_which_cost)

**Header Mode:**
- Evaluate against entire requisition total (`xxreq_cost_gl`)
- Even if rule filters on specific fields (e.g., CC=8100), still uses TOTAL req amount
- Use case: "Any requisition touching cost center 8100 needs approval if whole req is over $X"

**Line Mode:**
- Filter lines that match rule conditions
- Sum `xxreqd_total_gl` for ONLY matching lines
- Compare summed amount against rule thresholds
- Use case: "Approve specifically the 8100 spending if it exceeds $X"

**Example:**
```
Requisition:
  Line 1: $5,000 to CC 8100
  Line 2: $3,000 to CC 8200  
  Line 3: $2,000 to CC 8300
  Total: $10,000

Rule: CC=8100, Amount $4K-$999K, which_cost=Line
  → Matches! Line mode sums only CC 8100 lines = $5K > $4K threshold

Rule: CC=8100, Amount $4K-$999K, which_cost=Header
  → Matches! Header mode uses total = $10K > $4K threshold
```

### Approver Field

Can contain:
- **User ID**: `"john"`
- **Group ID**: `"buyers"` (only one group member needs to approve)
- **Can-Do List**: `"john,mary,buyers"` (any of these can approve)
- **Special Variables**: `$xxreq_obo`, `$xxreq_buyer`, etc. (resolved at runtime)

### Important Limitations

- Cannot create multiple approval records per line
- For line-by-line approval generation, must use xxAppRule with `xxAR_Eval_Lines = true`
- All conditions are AND - cannot express OR logic (need xxAppRule for that)

## Complex Rules (xxAppRule + xxAppField)

### Overview
Nested AND/OR conditional logic using hierarchical tree structure. Use when logic cannot be expressed with simple ANDs.

### When to Use Complex Rules

- Logic requires OR conditions: "Type is Expense OR Capital"
- Nested logic: "(Bill-to is 10000 OR user is Admin) AND (Type is Expense OR Amount > $5000)"
- Line-by-line approval generation: Different approver per line based on field values
- Variable substitution in conditions: Compare field values dynamically

### Rule Structure (xxAppRule)

Defines the rule header:
- `xxAR_RuleName`: Unique rule name
- `xxAR_Domain`: Can be '*' (applies to all domains) or specific domain code. When querying rules, always check: `(xxAR_Domain = '*' OR xxAR_Domain = 'your_domain')`. This field is also part of the relationship key between xxAppRule and xxAppField
- `xxAR_Approver`: Approver ID (supports special variables)
- `xxAR_AppLevel`: Sequence number (shared with xxapp_seq)
- `xxAR_MinAmt`, `xxAR_MaxAmt`: Amount thresholds
- `xxAR_AmtType`: "Header" or "Line" (like xxapp_which_cost)
- `xxAR_Eval_Lines`: TRUE to create multiple approval records per line
- `xxAR_stop`: Stop approval chain after this rule
- `xxAR_notify`: Notification rule only (evaluated after PO creation)

### Condition Tree Structure (xxAppField)

Creates hierarchical AND/OR tree:
- `xxAF_RuleName`: Links to xxAppRule.xxAR_RuleName
- `xxAF_Domain`: Must match the parent rule's `xxAR_Domain` value. Links conditions to their parent rule along with `xxAF_RuleName`. When querying conditions: `WHERE xxAF_RuleName = [rule] AND xxAF_Domain = [rule_domain]`
- `xxAF_Parent`: Parent node's Group number (0 = root)
- `xxAF_Group`: This node's Group number (0 = field condition, >0 = operator node)
- `xxAF_Operand`: "AND"/"OR" for nodes, "eq"/"ge"/"Can-Do"/etc. for conditions
- `xxAF_Table`: Table name (for field conditions)
- `xxAF_Field`: Field name (for field conditions)
- `xxAF_Value`: Comparison value (can include variables like $xxreq_obo)

### Tree Traversal Logic

1. Start at Parent=0 (root node)
2. Root has a Group number and is either AND or OR
3. Find all children where Parent matches root's Group number
4. For each child:
   - If operator node (Field is empty): Recursively evaluate its children
   - If field condition (Group=0): Evaluate the condition
5. Combine child results based on parent's operator:
   - AND: ALL children must be true
   - OR: AT LEAST ONE child must be true
6. Return true/false for entire tree

### Example: Change Order Rule

```
Root: Group 1 (AND) - all children must be true
  ├─ xxreq_update_po eq "true"
  ├─ xxreq_mat_change eq "false"
  └─ xxreq_update_po_tolerance eq "true"

If all three conditions are true → Rule triggers
Approver: $xxreq_userid (the change order creator, typically buyer)
Stop: true (blocks all other approval rules)
Sequence: 5 (very early)
```

### Example: CFO Rule (Inactive)

```
Root: Group 1 (AND)
  ├─ Group 3 (OR) - at least one must be true
  │   ├─ xxreq_bill_to eq "10000"
  │   └─ xxreq_userid Can-Do "!Peter,Admin"
  │
  └─ Group 4 (OR) - at least one must be true
      ├─ Group 2 (OR)
      │   ├─ xxreq_type eq "Inventory"
      │   ├─ xxreq_cost_gl ge "5000"
      │   └─ xxreq_site Not Can-Do "!1000,*"
      │
      └─ xxreq_type In List "Expense,Capital"

Evaluation:
  (Bill-to is 10000 OR user is Admin-except-Peter)
  AND
  (Type is Expense/Capital OR Type is Inventory OR GL≥5000 OR Site≠1000)
```

### Line-by-Line Evaluation (xxAR_Eval_Lines)

When `xxAR_Eval_Lines = true`:
- Rule can create MULTIPLE approval records
- One approval record per line that matches rule conditions
- Approver field should typically use variable that varies by line

**Example:**
```
Rule: Approver = $xxreqd_project_manager
      Eval_Lines = true
      Conditions: xxreqd_project != ""

Requisition:
  Line 1: Project A, PM = John
  Line 2: Project A, PM = John  
  Line 3: Project B, PM = Mary

Without MULTIPLE_APPROVALS setting:
  Creates 3 approval records: John, John, Mary

With MULTIPLE_APPROVALS = keep_last:
  Creates 2 approval records: John (consolidated), Mary
```

### Special Approver Variables

**Supervisor-Based:**
- `$SUPERVISORS`: All supervisors up chain until sufficient approval limit
- `$FIRST_SUPERVISOR`: Immediate supervisor only  
- `$LAST_SUPERVISOR`: Skip to supervisor with sufficient approval limit

**Requisition Field-Based:**
- `$xxreq_userid`: Person who created the requisition
- `$xxreq_obo`: On Behalf Of person (budget owner)
- `$xxreq_buyer`: Assigned buyer

**Line Field-Based (with Eval_Lines=true):**
- Can use any line field: `$xxreqd_project_manager`, `$xxreqd_cc_owner`, etc.

### Variable Substitution in Conditions

Can use `$fieldname` in condition values:
```
Condition: xxreq_userid ne "$xxreq_obo"
Meaning: User who created req is NOT the same as On Behalf Of person
```

## Validation Rules

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

## Default Rules

Every iPurchase implementation includes three default rules. Customers can modify, disable, or replace these.

### 1. Change Order Rule

**Purpose:** Enable efficient PO modifications without full re-approval when changes are minor and within tolerance.

**Configuration:**
- Rule Type: Complex (xxAppRule)
- Sequence: 5 (very early)
- Approver: `$xxreq_userid` (CO creator, typically buyer)
- Stop: true (ends approval chain)
- Active: true

**Trigger Conditions (ALL must be true):**
```
xxreq_update_po = true          (this is a change order)
xxreq_mat_change = false        (NOT a material change)
xxreq_update_po_tolerance = true (within tolerance)
```

**Behavior:**
- Routes only to buyer for quick approval
- Blocks all other approval rules (stop=true)
- See change-orders.md for complete tolerance calculation and material change detection logic

### 2. OBO Rule

**Purpose:** Route to On Behalf Of person when different from creator (e.g., assistant creating req for boss).

**Typical Configuration:**
- Rule Type: Complex (xxAppRule)
- Sequence: 6 (early, after Change Order)
- Approver: `$xxreq_obo`
- Stop: false (continues to other rules)
- Notify: false (approval rule, not notification)

**Trigger Condition:**
```
xxreq_userid ne "$xxreq_obo"
(Creator is NOT the same as On Behalf Of person)
```

**Customer Options:**
- Can configure as approval rule (typical) or notification rule (just FYI)
- Can disable entirely if not needed
- Can modify conditions as needed

### 3. Buyer Rule

**Purpose:** Final approval by purchasing team before PO creation.

**Typical Configuration:**
- Rule Type: Complex (xxAppRule)
- Sequence: 900 (late in chain, after business approvals)
- Approver: `$xxreq_buyer`
- Stop: false
- Notify: false

**Behavior:**
- No conditions (always triggers)
- Buyer reviews vendor, pricing, terms before creating PO
- Final checkpoint before req becomes PO

## Supervisor Approval Chains

### Overview
Special approver variables that automatically route through organizational hierarchy based on approval limits.

### How Supervisor Chains Work

1. Start with OBO person (`xxreq_obo`)
2. Check if OBO's approval limit (`wus_app_amt`) >= requisition amount
3. If insufficient, walk up supervisor chain:
   - Follow `wus_supervisor` field to find supervisor
   - Check supervisor's `wus_app_amt`
   - Continue until finding someone with sufficient approval limit
4. Organization top typically has `wus_app_amt = 9999999999` to ensure chain terminates

### Three Supervisor Variables

**$SUPERVISORS (plural):**
- Creates approval record for ALL supervisors in chain up to and including person with sufficient limit
- Use case: "Everyone in chain needs to approve"

**Example:**
```
Req Amount: $10,000
OBO: Alice (limit $2,000)
  ↓ supervisor
Manager: Bob (limit $5,000)
  ↓ supervisor
Director: Carol (limit $15,000)

Result: Alice → Bob → Carol (all three approve)
Note: May skip Alice if USE_APP_AMOUNT_OWN_REQS = false (typical)
```

**$FIRST_SUPERVISOR:**
- Creates approval record for immediate supervisor only
- Ignores approval limits
- Use case: "Always get direct supervisor approval regardless of amount"

**$LAST_SUPERVISOR:**
- Creates approval record for ONLY the supervisor with sufficient approval limit
- Skips intermediate supervisors
- Use case: "Go straight to the person with authority"

**Example with same org:**
```
Result: Carol only (skips Alice and Bob)
```

### Self-Approval

**System Setting:** `USE_APP_AMOUNT_OWN_REQS`
- Typical value: FALSE
- Controls whether OBO can use their own approval limit on their own requisitions

**If TRUE:**
- OBO with sufficient `wus_app_amt` can self-approve
- Would use OBO Rule conditions to add OBO to approval chain
- Supervisor chain only triggers if OBO limit is insufficient

**If FALSE (typical):**
- OBO cannot self-approve regardless of their approval limit
- Always routes up supervisor chain

### Deprecated Setting

**USE_SUPERVISORS_TO_APPROVE** - DEPRECATED, do not use
- Old way: Global on/off switch for supervisor routing
- New way: Use `$SUPERVISORS`/`$FIRST_SUPERVISOR`/`$LAST_SUPERVISOR` in approval rules with conditions
- New approach is much more flexible: "Use supervisors only for expense reqs over $5K"

## Duplicate Approver Handling

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

## Delegation System

### Overview
Users can designate a delegate to act on their behalf for approvals and other system actions. See delegation-and-permissions.md for complete details.

### Core Mechanism

**Field:** `wus_mstr.wus_delegate`
- User ID of person who can act on your behalf
- One delegate at a time
- Schedule-based (controlled by OOF settings)

### Approval Queue Display

Delegates see both their own and their delegator's requisitions:
- "Pending Peter" - Approving on behalf of Peter
- "Pending Frank" - Approving on behalf of Frank
- No label - Approving as themselves

### Audit Trail

When Bob approves on Jane's behalf:
- `xxreq_audit.xxreq_app_id` = "Jane" (who was required to approve)
- `xxreq_audit.xxreq_actual_approver` = "Bob" (who actually clicked)

### Chained Delegation

**System Setting:** `USE_CHAINED_DELEGATES`
- TRUE: If Jane delegates to Bob, and Bob delegates to Sue, then Sue can act for Jane
- FALSE: Only direct delegation (Sue can act for Bob, but not Jane)

## Supervisor Override

### ALLOW_SUPERVISORS_TO_APPROVE Setting

Can-Do list of users/groups who can approve on behalf of their subordinates.

**Values:**
- `*`: All supervisors can override
- Blank: No supervisors can override
- `"manager1,exec_group"`: Specific users/groups only

**Behavior:**
- Supervisor can approve or reject requisitions for their direct reports
- Use case: "My employee is stuck, I'll just approve it for them"
- Separate from delegation (doesn't require delegate to be set)
- Creates audit trail similar to delegation

## Notification Rules

### Overview
Rules that don't require approval - recipients are CC'd on final PO email for visibility only.

### Configuration
- Set `xxapp_notify = true` (simple rules) or `xxAR_notify = true` (complex rules)
- Use any sequence number (doesn't matter since evaluated separately)

### Evaluation
1. Ignored completely during approval workflow (Phases 1 & 2)
2. Only evaluated AFTER requisition is fully approved and converted to PO
3. Conditions evaluated against CURRENT req data (after all changes)
4. Matching approvers added as CC recipients on PO notification email

### Use Cases
- "Finance wants to see all POs over $50K" (visibility, not approval)
- "Notify department head of all capital purchases"
- "CC procurement manager on all reqs from specific cost centers"

### Email Recipients
- TO: Originator (OBO) + Buyer
- CC: Anyone matching notification rules

## Requisition Types

### Overview
Requisition types are customer-configurable categories that drive approval routing and field restrictions.

**Standard Types (Customizable):**
- Expense - Operating expenses
- Capital - Capital expenditures
- Inventory - Stock/inventory items

**Purpose:**
1. Primary filter in approval rules (most rules filter on type + amount)
2. Control which GL accounts/sub-accounts are allowed/defaulted per type

### Type Configuration (RT_ Settings)

Settings use pattern: `RT_[type]_*` with optional site override: `RT_[type][site]_*`

**Account Control:**
- `RT_[type]_ACCOUNT_RANGE`: Valid accounts (Can-Do list)
- `RT_[type]_ACCOUNT_DEFAULT`: Auto-populate this account
- `RT_[type]_ACCOUNT_READONLY`: Lock field (TRUE/FALSE)

**Sub-Account Control:**
- `RT_[type]_SUB_ACCOUNT_RANGE`: Valid sub-accounts
- `RT_[type]_SUB_ACCOUNT_DEFAULT`: Auto-populate
- `RT_[type]_SUB_ACCOUNT_READONLY`: Lock field

**Other Settings:**
- `RT_[type]_DEPT_DEFAULT`: Default department
- `RT_[type]_DEFAULT_BUYER`: Default buyer for type

**Site Overrides:**
- Same pattern with site code: `RT_EXPENSE_10000_ACCOUNT_RANGE`
- Site-specific setting overrides global type setting

### Example Configurations

**Locked Capital Type:**
```
RT_CAPEX_ACCOUNT_RANGE = "8200"
RT_CAPEX_ACCOUNT_DEFAULT = "8200"
RT_CAPEX_ACCOUNT_READONLY = "TRUE"
RT_CAPEX_DEPT_DEFAULT = "0900"
RT_CAPEX_SUB_ACCOUNT_DEFAULT = "1000"
RT_CAPEX_SUB_ACCOUNT_READONLY = "TRUE"
```
Result: Capital reqs always use account 8200, dept 0900, sub 1000 - users cannot change

**Flexible Expense Type:**
```
RT_EXPENSE_ACCOUNT_RANGE = "8*,rent"
RT_EXPENSE_DEPT_DEFAULT = "2000"
RT_EXPENSE_DEFAULT_BUYER = "Frank"
```
Result: Expense reqs can use any 8xxx account or "rent", defaults to dept 2000 and buyer Frank

**Site-Specific Override:**
```
RT_EXPENSE_ACCOUNT_RANGE = "8*"          (global: any 8xxx)
RT_EXPENSE_11000_ACCOUNT_RANGE = "8200,8300"  (site 11000: only 8200 or 8300)
```

## Approval Routing by Requisition Type

Most approval methodologies use requisition type as primary discriminator:

**Example Approval Paths:**

**Inventory Requisitions:**
```
Seq 100: Materials Manager (any amount)
Seq 200: Operations Director (over $10K)
```

**Expense Requisitions:**
```
Seq 150: Cost Center Owner
Seq 250: Department Manager (over $5K)
Seq 350: VP (over $25K)
```

**Capital Requisitions:**
```
Seq 300: Department Manager (any amount)
Seq 400: Finance Director (over $50K)  
Seq 450: CFO (over $100K)
```

This is why `xxreq_type` is a core field in most approval rule conditions.

## Best Practices

### Rule System Selection

**Use Simple Rules (xxapp_mstr) when:**
- All conditions can be expressed with AND logic
- No need for line-by-line approval generation
- Rule logic is straightforward and easy to explain

**Use Complex Rules (xxAppRule) when:**
- Need OR logic or nested conditions
- Need line-by-line approval with different approver per line
- Need variable substitution in conditions
- Logic is too complex for simple AND conditions

### Sequence Numbering

**Validation Rules:**
- Use negative numbers: -990, -980, -970, etc.
- Increment by 10 for easy insertion

**Approval Rules:**
- Use positive numbers: 5, 100, 200, 300, etc.
- Reserve low numbers (1-10) for special rules like Change Order
- Use increments of 50 or 100 for regular approval rules
- Leave gaps for future rules

**Notification Rules:**
- Any positive sequence (doesn't matter since evaluated separately)
- Consider using 900+ range to group together

### Documentation

**Simple Rules:**
- Description field should clearly explain when rule applies
- Document typical use cases

**Complex Rules:**
- CRITICAL: Document business logic in plain language
- Complex rules are "write-only" - hard to understand later
- Include examples of when rule should trigger
- Document why OR logic was needed (why simple rule wasn't sufficient)

### Maintenance

**Regular Reviews:**
- Review approval rules annually
- Look for rules that are no longer used (inactive)
- Consolidate duplicate logic
- Check for conflicting rules

**Change Management:**
- Test rule changes in dev/test environment first
- Use approval simulation feature to verify routing
- Document what changed and why
- Communicate changes to affected approvers

### System Settings

**Key Settings to Review:**
- `MULTIPLE_APPROVALS` - Usually keep_last
- `AUTO_APPROVE_FORWARD` - Enable for efficiency, but test carefully
- `ALLOW_SUPERVISORS_TO_APPROVE` - Define who can override
- `USE_CHAINED_DELEGATES` - Usually false for security
- Change Order tolerance settings - Match business risk tolerance

## Common Scenarios

### Scenario: Cost Center Owner Approval

**Simple Rule Approach:**
```
Sequence: 100
Approver: $xxreqd_cc_owner
Amount: $0 - $999,999
Type: *
Cost Center: *
Which Cost: Line
Stop: false
```

This works IF there's a field `xxreqd_cc_owner` in the database. Otherwise, need to maintain a mapping table or use complex rule with Can-Do lists.

### Scenario: Supervisor Chain by Amount

**Complex Rule Approach:**
```
Sequence: 200
Approver: $SUPERVISORS
Amount: $5,000 - $999,999
Conditions: xxreq_type eq "Expense"
Stop: false
```

Result: Expense reqs over $5K route through supervisor chain until finding someone with sufficient limit.

### Scenario: Multi-Level Dollar Thresholds

**Multiple Simple Rules:**
```
Seq 100: Manager, $0-$5K, Type: Expense
Seq 200: Director, $5K-$25K, Type: Expense  
Seq 300: VP, $25K-$100K, Type: Expense
Seq 400: CFO, $100K+, Type: Expense
```

With MULTIPLE_APPROVALS = keep_last, a $30K req would only route to VP (not Manager or Director).

### Scenario: Project-Based Approval

**Complex Rule with Eval_Lines:**
```
Sequence: 150
Approver: $xxreqd_project_manager
Eval_Lines: true
Conditions: xxreqd_project ne ""
Stop: false
```

Result: Each line with a project gets routed to that project's PM. Lines without projects skip this rule.

### Scenario: Special Account Requires Additional Approval

**Simple Rule:**
```
Sequence: 250
Approver: finance_director
Amount: $0 - $999,999
Account: 8500,8600
Stop: false
```

Result: Any req using accounts 8500 or 8600 requires Finance Director approval regardless of amount or other factors.

## Troubleshooting

### Rule Not Triggering

**Check:**
1. Is rule active? (`xxapp_active` or `xxAR_Active`)
2. Does amount fall within min/max range?
3. Do ALL conditions match (AND logic for simple rules)?
4. For complex rules, trace through tree evaluation
5. Was rule blocked by earlier stop condition?
6. Is it a notification rule being checked during approval? (Won't trigger)

### Wrong Approver

**Check:**
1. Variable substitution - is field populated correctly?
2. Group membership - is user actually in the group?
3. Delegation - is approver delegating to someone else?
4. MULTIPLE_APPROVALS setting - is correct instance being kept?

### Routing Takes Too Long

**Optimization:**
1. Reduce number of rules (consolidate where possible)
2. Use stop conditions appropriately
3. Order rules by frequency (most common first)
4. Avoid complex rules where simple rules suffice
5. Check for inefficient line-level evaluation

### Duplicate Approvals

**Check:**
1. MULTIPLE_APPROVALS setting - should be keep_last usually
2. Are multiple rules adding same approver?
3. Is AUTO_APPROVE_FORWARD enabled but not working?
4. Check group membership (user appearing both directly and via group)

## Related Documentation

- **technical-schema.md** - Database structure, tables, and fields
- **change-orders.md** - Detailed change order workflow
- **system-settings.md** - Complete settings reference
- **delegation-and-permissions.md** - Delegation and override mechanics
- **admin-guide.md** - Setup procedures and best practices

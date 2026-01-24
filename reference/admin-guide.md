# iPurchase Administrator Guide

## Overview

This guide provides administrative procedures for setting up and managing iPurchase approval workflows, user access, and system configuration.

**Target Audience:** System administrators, procurement managers, IT staff responsible for iPurchase configuration

**Related Documentation:**
- **approval-systems.md** - Complete approval workflow logic and rule types
- **technical-schema.md** - Database structure and query patterns
- **system-settings.md** - System configuration reference
- **delegation-and-permissions.md** - Delegation and permission mechanics
- **change-orders.md** - Change order workflow details

## Getting Started

### System Access

**Administrator Requirements:**
- Admin access to iPurchase application
- Database read access for troubleshooting (via MCP tools)
- Understanding of organization's approval hierarchy and business rules

**Key Administrator Roles:**
- **System Administrator**: Overall system configuration, user management
- **Procurement Manager**: Approval rules, requisition types, vendor setup
- **IT Support**: Database queries, troubleshooting, integrations

### Understanding Your Organization's Needs

Before configuring approval rules, document:

1. **Organizational Structure**
   - Department hierarchy
   - Supervisor/manager relationships
   - Who reports to whom
   - Approval dollar limits by role

2. **Approval Requirements**
   - What types of purchases exist? (Expense, Capital, Inventory, etc.)
   - Who needs to approve what?
   - At what dollar thresholds?
   - Any special requirements? (Projects, cost centers, accounts)

3. **Exceptions & Special Cases**
   - Change orders - when to bypass full approval?
   - Delegation - who can delegate to whom?
   - Supervisor overrides - who can approve for subordinates?
   - Emergency purchases - any expedited workflows?

## User Management

### Creating Users

**Required Information:**
- User ID (wus_id)
- Full name (wus_name)
- Email address (wus_email)
- Supervisor (wus_supervisor) - creates org chart
- Approval dollar limit (wus_app_amt)

**Supervisor Chain Setup:**
1. Start at top of organization (CEO, VP, etc.)
2. Set their supervisor to themselves or leave blank
3. Set very high approval limit (e.g., 9999999999)
4. Work down org chart, setting each person's supervisor
5. Set approval limits appropriate to role

**Example Org Chart:**
```
CEO (limit: $9,999,999)
  ↓ supervisor
VP Finance (limit: $100,000)
  ↓ supervisor
Director (limit: $25,000)
  ↓ supervisor
Manager (limit: $5,000)
  ↓ supervisor  
Employee (limit: $0 or $1,000)
```

### Group Management

**Creating Groups:**
1. Define group in wgr_mstr (group ID and description)
2. Add members in wugr_mstr (user ID → group ID mapping)

**Common Group Types:**
- Department groups: "finance", "operations", "it"
- Role groups: "buyers", "managers", "approvers"
- Special groups: "admin", "power_users"

**Group Usage:**
- Approval rules (only one member needs to approve)
- Permission settings (Can-Do lists)
- Requisition access control

### Setting Approval Limits

**Guidelines:**
- Match approval limits to business risk tolerance
- Consider both individual purchases and cumulative spending
- Review and adjust annually
- Document exceptions (why does this person have higher/lower limit?)

**Example Approval Limits:**
```
Employee: $500 - Can approve own small purchases (if USE_APP_AMOUNT_OWN_REQS = TRUE)
Supervisor: $5,000 - Approve team purchases
Manager: $25,000 - Approve department purchases
Director: $100,000 - Approve division purchases
VP/CFO: $9,999,999 - Approve all purchases
```

## Approval Rules Setup

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

## Requisition Types Configuration

### Standard Types

**Default Types Provided:**
- Expense - Operating expenses
- Capital - Capital expenditures
- Inventory - Stock/inventory items

**Customization:**
- Add types: Service, MRO, Consulting, Travel, etc.
- Rename types: "CapEx" instead of "Capital"
- Delete unused types
- Update REQUISITION_TYPES setting

### Account Restrictions

**Prevent GL Coding Errors:**

**Lock Capital to Asset Accounts:**
```sql
RT_CAPEX_ACCOUNT_RANGE = "1000-1999"
RT_CAPEX_ACCOUNT_DEFAULT = "1500"
RT_CAPEX_ACCOUNT_READONLY = "TRUE"
```

**Allow Expense Account Range:**
```sql
RT_EXPENSE_ACCOUNT_RANGE = "6000-7999,8*"
RT_EXPENSE_ACCOUNT_DEFAULT = "" (no default, user chooses)
RT_EXPENSE_ACCOUNT_READONLY = "FALSE"
```

**Site-Specific Override:**
```sql
RT_EXPENSE_ACCOUNT_RANGE = "8*" (global setting)
RT_EXPENSE_11000_ACCOUNT_RANGE = "8200,8300" (site 11000 more restrictive)
```

### Default Buyers by Type

Assign default buyers based on requisition type:
```sql
RT_EXPENSE_DEFAULT_BUYER = "frank"
RT_CAPITAL_DEFAULT_BUYER = "mary"
RT_INVENTORY_DEFAULT_BUYER = "john"
```

Site overrides:
```sql
RT_EXPENSE_10000_DEFAULT_BUYER = "mike" (site 10000 uses different buyer)
```

## Change Order Configuration

### Tolerance Settings

**Balance efficiency vs control:**
- **Low tolerance** (e.g., $100, 5%) → More re-approvals, tighter control
- **High tolerance** (e.g., $1000, 15%) → Fewer re-approvals, more efficiency

**Recommended Starting Point:**
```sql
PO_UPDATE_TOLERANCE_AMOUNT = "500"
PO_UPDATE_TOLERANCE_PCT = "10"
```

**Review Quarterly:**
- Are too many change orders re-routing? (Tolerance too low)
- Are large changes bypassing approval? (Tolerance too high)
- Adjust based on business risk comfort level

### Material Change Fields

**Header Fields that Trigger Re-Route:**
```sql
CO_HEADER_REROUTE_FIELDS = "xxreq_buyer,xxreq_ship_to,xxreq_vendor"
```

**Line Fields that Trigger Re-Route:**
```sql
CO_ITEM_REROUTE_FIELDS = "xxreqd_cc,xxreqd_acct,xxreqd_sub,xxreqd_part"
```

**New Line Items:**
```sql
CO_ITEM_REROUTE_NEW = "TRUE"  (new lines always re-route)
CO_ITEM_REROUTE_NEW = "FALSE" (new lines OK if within tolerance)
```

**Guidelines:**
- Include fields that represent scope/responsibility changes
- Start conservative (more fields = more re-routes = tighter control)
- Relax based on business feedback

## Delegation Configuration

### Out of Office Settings

**Enable Delegation:**
```sql
ALLOW_OOF = "*" (everyone can delegate)
```

**Restrict Who Can Be Delegates:**
```sql
OOF_LIMIT_TO = "*" (anyone can be delegate)
OOF_LIMIT_TO = "approvers" (only approvers group)
OOF_LIMIT_TO = "" (no one can delegate - feature disabled)
```

**Require Same Department:**
```sql
OOF_LIMIT_BY_DEPT = "TRUE"
```

**Require Equal/Higher Approval Limit:**
```sql
OOF_LIMIT_BY_DOLLARS = "TRUE" (recommended for security)
```

**Delegation Chains:**
```sql
USE_CHAINED_DELEGATES = "FALSE" (recommended - prevents Jane→Bob→Sue chains)
USE_CHAINED_DELEGATES = "TRUE" (allow transitive delegation)
```

**Notification:**
```sql
OOF_NOTIFY_OLD = "TRUE" (email existing pending reqs to delegate immediately)
OOF_ASK_FREQUENCY = numeric value (prompt to remove delegate on login)
```

### Supervisor Override

**Allow Supervisors to Approve for Subordinates:**
```sql
ALLOW_SUPERVISORS_TO_APPROVE = "*" (all supervisors can override)
ALLOW_SUPERVISORS_TO_APPROVE = "managers,directors" (only specific groups)
ALLOW_SUPERVISORS_TO_APPROVE = "" (no supervisor overrides)
```

**Use Case:** Employee is out/stuck, supervisor approves on their behalf

**Security Note:** Audit trail shows both who was required to approve (employee) and who actually approved (supervisor)

## Approval Workflow Settings

### Duplicate Approver Handling

**MULTIPLE_APPROVALS:**
```sql
MULTIPLE_APPROVALS = "keep_last" (RECOMMENDED - approval at highest level)
MULTIPLE_APPROVALS = "keep_first" (approval at lowest level)
MULTIPLE_APPROVALS = "keep_all" (approve at every instance)
```

**Example Impact:**
```
Routing: Jane (seq 100), Bob (seq 200), Jane (seq 300)

keep_last: Bob approves, Jane approves at 300 (higher authority)
keep_first: Jane approves at 100, Bob approves (lower authority)
keep_all: Jane approves twice, Bob approves (redundant)
```

### Auto-Approval

**AUTO_APPROVE_FORWARD:**
```sql
AUTO_APPROVE_FORWARD = "TRUE" (enable for all)
AUTO_APPROVE_FORWARD = "managers,directors" (enable for specific groups)
AUTO_APPROVE_FORWARD = "FALSE" (disable - require click for each approval)
```

**Behavior:** After first approval, auto-approves future instances in same routing
**Exception:** Does NOT auto-approve if final approver (must click explicitly)

**Benefit:** Reduces approval bottlenecks when same person appears multiple times

### Routing Changes

**Allow Approver Changes:**
```sql
ALLOW_APPROVER_CHANGES = "TRUE" (enable manual add/remove of approvers)
ALLOW_APPROVER_CHANGES_ORIGINATOR = "TRUE" (originator can modify)
ALLOW_APPROVER_CHANGES_REMOVE_APPROVER = "buyers,admins" (who can remove)
ALLOW_APPROVER_CHANGES_ROLES = "*" (who can add)
```

**Auto Re-Route on Changes:**
```sql
ALLOW_AUTO_REROUTE = "TRUE" (recalculate routing if approver makes changes)
ALLOWED_DOLLAR_INCREASE = "0.01" (re-route on any dollar increase)
ALLOWED_PERCENT_INCREASE = "5" (re-route if increase >5%)
```

## Testing & Validation

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

## Maintenance & Monitoring

### Regular Reviews

**Quarterly:**
- Review tolerance settings (change orders)
- Check for inactive rules (can be deleted)
- Verify approval limits still appropriate
- Update requisition type settings
- Review permission settings

**Annually:**
- Full approval rule audit
- Org chart validation (supervisors current?)
- User access review (remove termed employees)
- Group membership cleanup
- Documentation update

### Monitoring

**Key Metrics:**
- Average approval time by type/amount
- Number of change orders vs full re-approvals
- Rejection rates (why are reqs being rejected?)
- Delegation usage (are people abusing it?)
- Manual approver changes (are rules not working?)

**Red Flags:**
- Approvals taking longer than expected
- High rejection rates (rules too restrictive or users not trained)
- Frequent manual routing changes (rules need adjustment)
- Many change orders exceeding tolerance (tolerance too low)

### Documentation

**Maintain Documentation For:**
- Approval rule business logic (especially complex rules)
- Why specific settings were chosen
- Organizational changes affecting routing
- Common troubleshooting scenarios
- Contact information for rule owners

**Update When:**
- Adding/modifying approval rules
- Changing system settings
- Reorganizing departments
- Changing business processes

## Security Best Practices

### Permission Settings

**Restrict Dangerous Permissions:**
```sql
ALLOW_DELETE_PROCESSED = "admin_only" (very few users)
ALLOW_APPROVER_CHANGES = "TRUE" (but limit sub-settings)
ALLOW_APPROVER_CHANGES_REMOVE_APPROVER = "buyers,admins"
```

### Delegation Controls

**Prevent Unauthorized Delegation:**
```sql
OOF_LIMIT_BY_DOLLARS = "TRUE" (can't delegate to lower authority)
OOF_LIMIT_BY_DEPT = "TRUE" (can't delegate outside department)
OOF_LIMIT_TO_APPROVERS = "TRUE" (can only delegate to approvers)
USE_CHAINED_DELEGATES = "FALSE" (no delegation chains)
```

### Audit Trail

**Monitor:**
- Who approved what (xxreq_audit.xxreq_actual_approver)
- Delegation activity (who is delegating to whom)
- Manual routing changes (who is adding/removing approvers)
- Deleted requisitions (especially processed ones)

**Review:**
- Unusual approval patterns
- Approvers with very high volumes
- Frequent delegation by same people
- Overuse of supervisor override

## Troubleshooting

### Database Queries

**Find Pending Requisitions:**
```sql
SELECT xxreq_nbr, xxreq_userid, xxreq_obo, xxreq_entry_date, xxreq_cost_gl
FROM PUB.xxreq_mstr
WHERE xxreq_status = 'CONFIRMED'
ORDER BY xxreq_entry_date DESC
```

**Find Approval Bottlenecks:**
```sql
SELECT a.xxreq_app_id, COUNT(*) as pending_count
FROM PUB.xxreq_audit a
JOIN PUB.xxreq_mstr r ON a.xxreq_nbr = r.xxreq_nbr
WHERE r.xxreq_status = 'CONFIRMED'
  AND a.xxreq_status IS NULL
GROUP BY a.xxreq_app_id
ORDER BY pending_count DESC
```

**Find Change Orders:**
```sql
SELECT xxreq_nbr, xxreq_userid, xxreq_entry_date, xxreq_cost_gl, 
       xxreq_mat_change, xxreq_update_po_tolerance
FROM PUB.xxreq_mstr
WHERE xxreq_update_po = TRUE
ORDER BY xxreq_entry_date DESC
```

**Find Active Delegates:**
```sql
SELECT wus_id, wus_name, wus_delegate
FROM PUB.wus_mstr
WHERE wus_delegate IS NOT NULL
  AND wus_delegate != ''
```

### Common Problems

**Problem: Requisition not routing correctly**
**Solution:**
1. Check approval simulation - who SHOULD approve?
2. Check actual routing in xxreq_audit
3. Compare expected vs actual
4. Review rule conditions - do they all match?
5. Check for stop conditions blocking later rules

**Problem: Change order going to full approval when shouldn't**
**Solution:**
1. Check tolerance settings (amount and percentage)
2. Verify fields changed (CO_HEADER/ITEM_REROUTE_FIELDS)
3. Check if new lines added (CO_ITEM_REROUTE_NEW)
4. Verify approval hierarchy hasn't changed
5. Check material change flag in xxreq_mstr

**Problem: User can't submit requisition**
**Solution:**
1. Check ALLOW_REQ_ENTRY permission
2. Look for validation rule errors (MESSAGE: rules)
3. Verify required fields populated
4. Check for supervisor chain issues (no supervisor with sufficient limit)

**Problem: Delegation not working**
**Solution:**
1. Verify wus_delegate field is set
2. Check OOF settings (LIMIT_BY_DOLLARS, LIMIT_BY_DEPT, etc.)
3. Look for delegation chains (USE_CHAINED_DELEGATES)
4. Verify delegate has system access

## Best Practices Summary

### Do's

✓ Start with simple rules, add complexity only when needed
✓ Test thoroughly before activating rules
✓ Document business logic for all rules (especially complex)
✓ Use descriptive rule names and descriptions
✓ Review and update rules regularly
✓ Train users on approval workflows
✓ Monitor approval metrics
✓ Maintain audit trail
✓ Use approval simulation for testing
✓ Keep requisition types simple and intuitive

### Don'ts

✗ Don't create complex rules when simple rules work
✗ Don't skip testing rule changes
✗ Don't leave rules undocumented
✗ Don't set unrealistic tolerance thresholds
✗ Don't allow dangerous permissions broadly
✗ Don't ignore slow approval times
✗ Don't create delegation chains (security risk)
✗ Don't forget to clean up inactive rules
✗ Don't modify default rules without understanding impact
✗ Don't skip regular reviews

## Getting Help

### Internal Resources

- **Technical Documentation**: See related .md files for detailed reference
- **Database Queries**: Use MCP tools for ad-hoc investigation
- **Approval Simulation**: Test routing before submitting
- **System Settings**: Review pf_mstr for current configuration

### External Support

- **ISS Group**: Contact for complex configuration or troubleshooting
- **QAD Support**: For ERP integration issues
- **Vendor Support**: For punchout or catalog issues

### Documentation References

- **approval-systems.md**: Complete approval workflow logic
- **technical-schema.md**: Database structure and queries
- **system-settings.md**: Configuration reference
- **delegation-and-permissions.md**: Delegation mechanics
- **change-orders.md**: Change order workflow details

## Next Steps

1. Review current approval rules and identify improvements
2. Document business logic for all complex rules
3. Test approval routing with simulation
4. Review and update requisition type settings
5. Configure delegation and permission settings
6. Set up monitoring and metrics
7. Train users and approvers
8. Schedule regular reviews

---

*This guide will be expanded based on customer feedback and common implementation scenarios.*

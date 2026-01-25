# User Management - iPurchase Administration

**Purpose:** Creating users, setting up supervisor chains, managing groups, and configuring approval limits.

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

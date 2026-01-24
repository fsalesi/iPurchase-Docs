---
screen_id: users_and_groups
screen_name: Users and Groups
module: Administration
access_level: Administrator
database_tables:
  - wus_mstr
  - wugr_mstr
  - wgr_mstr
related_screens:
  - system_settings
  - approval_rules
  - security
screenshot: ../screenshots/users-and-groups/01-main-screen-user-info-tab.png
last_updated: 2025-01-23
author: Frank Salesi
---

# Users and Groups Screen

## Overview
The Users and Groups screen is the primary interface for managing user accounts in iPurchase. This screen allows administrators to create, modify, and delete user accounts, manage user permissions, assign users to groups, and configure user-specific settings.

## Access Path
Administration → Users and Groups

## Screenshot
![Users and Groups Main Screen](../screenshots/users-and-groups/01-main-screen-user-info-tab.png)

## Screen Layout

The screen consists of three main tabs:
1. **User Info** - User account details and contact information
2. **Groups** - Group membership assignments
3. **iPurchase** - iPurchase-specific settings and permissions

Below the form is a **User Browse** grid showing all users in the system.

---

## Tabs Overview

The Users and Groups screen has three tabs:
1. **User Info** - Basic user account details and contact information
2. **Groups** - Group membership for permissions and license access
3. **iPurchase** - Procurement-specific settings: approval limits, defaults, security restrictions

---

## User Info Tab

### Primary Fields Section (Left Column)

#### Field: User Id
- **Location**: Top left, first field
- **Type**: Text input (read-only when editing existing user)
- **Required**: Yes
- **Validation**: Alphanumeric, case-sensitive, must be unique
- **Database**: `wus_mstr.wus_id`
- **Business Rule**: 
  - Cannot be changed after user creation
  - Used as primary key and foreign key throughout system
  - Case-sensitive for lookups and comparisons
- **Example**: `andyE`, `Frank`, `CEO`

#### Field: Name
- **Location**: Second field in left column
- **Type**: Text input
- **Required**: Yes (indicated by red asterisk)
- **Database**: `wus_mstr.wus_name`
- **Business Rule**: Full name displayed in dropdowns, approval queues, and reports
- **Example**: `Andy Eifrid`, `Frank Salesi`

#### Field: Password Expiration Date
- **Location**: Third field in left column
- **Type**: Date picker
- **Required**: No
- **Format**: MM-DD-YYYY
- **Database**: `wus_mstr.wus_expire_date`
- **Business Rule**: 
  - User must change their password at next login after this date
  - Ignored if using SSO (iPurchase supports any provider that uses OAuth2)
  - If blank, password never expires
- **Example**: `08-24-2080`

#### Field: Disabled
- **Location**: Checkbox below Password Expiration Date
- **Type**: Boolean checkbox
- **Required**: No
- **Database**: `wus_mstr.wus_disable`
- **Business Rule**: 
  - If checked, user cannot login
  - Prevents login without deleting user record
  - Used for inactive employees while preserving history
  - Disabled users cannot be selected in dropdowns

#### Field: Last Login
- **Location**: Fifth field in left column
- **Type**: Display only (read-only)
- **Format**: Date/time
- **Database**: `wus_mstr.wus_last_login`
- **Business Rule**: 
  - System-maintained field
  - Updated automatically on successful login
  - Useful for identifying inactive accounts

#### Field: Create Date
- **Location**: Sixth field in left column
- **Type**: Display only (read-only)
- **Format**: MM-DD-YYYY
- **Database**: `wus_mstr.wus_create_date`
- **Business Rule**: System-maintained, set on user creation
- **Example**: `01-25-2022`

#### Field: Created By
- **Location**: Seventh field in left column
- **Type**: Display only (read-only)
- **Database**: `wus_mstr.wus_create_by`
- **Business Rule**: User ID of administrator who created this account
- **Example**: `Frank`

### Address Section (Middle Column)

#### Field: Address (Line 1)
- **Location**: Top of middle column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_street1`
- **Business Rule**: Optional contact information

#### Field: Address (Line 2)
- **Location**: Second field in middle column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_street2`

#### Field: City
- **Location**: Third field in middle column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_city`

#### Field: State
- **Location**: Fourth field in middle column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_state`

#### Field: Zip Code
- **Location**: Fifth field in middle column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_post`

#### Field: Country
- **Location**: Sixth field in middle column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_country`

### Company and Contact Section (Right Column)

#### Field: Company
- **Location**: Top of right column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_company`
- **Business Rule**: Optional, used for external vendors or contractors

#### Field: Title
- **Location**: Second field in right column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_title`
- **Example**: `CEO`, `Vice President`, `$50K` (custom usage)

#### Field: Email
- **Location**: Third field in right column
- **Type**: Email input
- **Required**: Yes (indicated by red asterisk)
- **Validation**: Must be valid email format
- **Database**: `wus_mstr.wus_email`
- **Business Rule**: 
  - Used for all system notifications
  - Approval emails, requisition updates, etc.
  - Must be unique per user
- **Example**: `AndyEifrid@somewhere.com`

#### Field: Phone
- **Location**: Fourth field in right column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_phone`

#### Field: Mobile
- **Location**: Fifth field in right column
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_fax`

#### Field: Carrier
- **Location**: Sixth field in right column
- **Type**: Dropdown
- **Required**: No
- **Database**: `wus_mstr.wus_carrier`
- **Business Rule**: Used for SMS notifications if configured

#### Field: Domains
- **Location**: Bottom of right column
- **Type**: Text input (comma-separated list)
- **Required**: Yes (indicated by red asterisk)
- **Format**: Comma-separated domain codes or asterisk (*)
- **Database**: `wus_mstr.wus_domains`
- **Business Rule**: 
  - Controls which company/domains user can access
  - `*` = access to all domains
  - `demo1,demo2` = access only to specified domains
  - Used for multi-company installations
  - Critical for data security and segregation
- **Example**: `demo1,demo2,eb2,eb2-1027`

---

## Groups Tab

![Users and Groups - Groups Tab](../screenshots/users-and-groups/02-groups-tab.png)

### Overview
The Groups tab manages user membership in groups. Groups serve two primary purposes:
1. **License Groups** - Control access to iPurchase modules and features
2. **Permission/Approval Groups** - Used in approval rules and data access

### Screen Layout

The tab displays two list boxes with Add/Remove buttons between them:

#### Available Groups (Left Panel)
- Lists all groups the user is NOT currently a member of
- Groups prefixed with `**` are license groups (see License Groups section)
- Select one or more groups, then click **Add →** to assign

#### User Groups (Right Panel)
- Lists all groups the user IS currently a member of
- Select one or more groups, then click **← Remove** to unassign
- Click **View Users** to manage membership from the group perspective

### Tab Buttons

#### Button: New Group
- **Action**: Creates a new group definition
- **Database Impact**: INSERT on `wgr_mstr`

#### Button: View Users
- **Action**: Opens group-centric membership management
- **Behavior**: Shows two list boxes:
  - Left: Users NOT in the selected group
  - Right: Users IN the selected group
- **Use Case**: Easier when adding many users to one group

#### Button: Delete Group
- **Action**: Deletes the selected group
- **Validation**: Cannot delete groups with members or groups referenced in approval rules
- **Database Impact**: DELETE from `wgr_mstr`

### License Groups

License groups (prefixed with `**`) control access to iPurchase modules and features. These groups are automatically created when the LICENSE system setting is configured.

| Group Pattern | Purpose |
|---------------|---------|
| `** iPurchase CORE Access Group` | Required for basic iPurchase login |
| `** iApprove CORE Access Group` | Required for iApprove module access |
| `** iPurchase Budgets Access Group` | Access to Budget module |
| `** iApprove [Module] Access Group` | Access to specific iApprove modules |
| `Admin` | Special group for administrative access |

**Important Notes:**
- License groups are auto-created from the LICENSE setting but **users must be manually added**
- Without CORE access group membership, user cannot login to that module
- Admin group provides administrative access to configuration screens

### Permission/Approval Groups

Non-license groups (without `**` prefix) are used for:
1. **Approval Rules** - Groups can be approvers (any member can approve)
2. **Data Access** - Groups in Can-Do lists for security
3. **Organizational Structure** - Logical groupings for reporting

**Best Practice - Groups in Approval Rules:**
> Rather than setting individual users as approvers in rules, create groups (even groups with one member). When employees change roles or leave, simply update group membership instead of modifying approval rules. This is easier to maintain and audit.

### Database Schema - Groups

```sql
-- Group Master
wgr_mstr
  wgr_id          VARCHAR(20)     PRIMARY KEY     -- Group ID
  wgr_desc        VARCHAR(50)                     -- Group description

-- User-Group Membership
wugr_mstr
  wugr_gr_id      VARCHAR(20)     FK → wgr_mstr   -- Group ID
  wugr_us_id      VARCHAR(10)     FK → wus_mstr   -- User ID
```

### Managing Group Membership

**Two approaches:**

1. **User-Centric** (this screen)
   - Select a user from the browse
   - Go to Groups tab
   - Select groups and click Add/Remove
   - Best when: Setting up a new user

2. **Group-Centric** (View Users button)
   - Select a group
   - Click View Users
   - Select users and click Add/Remove
   - Best when: Adding many users to one group, or when someone leaves

---

## iPurchase Tab

![Users and Groups - iPurchase Tab](../screenshots/users-and-groups/03-ipurchase-tab.png)

### Overview
The iPurchase tab contains procurement-specific settings including approval authority, supervisor hierarchy, and default/security values for requisition fields.

### Organizational Fields (Left Column)

#### Field: Employee Nbr
- **Location**: Top left
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_erp_id`
- **Business Rule**: 
  - Used for potential HR system integration
  - If HR sync is configured, this field links iPurchase users to HR employee records
  - Typically the employee number/ID from the HR system
- **Note**: Contact Anthropic for HR integration configuration

#### Field: Supervisor
- **Location**: Second row, left
- **Type**: Dropdown (User ID lookup)
- **Required**: No
- **Database**: `wus_mstr.wus_supervisor`
- **Business Rule**: 
  - Creates organizational hierarchy for approval routing
  - When approval rules use `$SUPERVISORS`, system walks up this chain
  - Circular references not allowed (cannot be your own grandpa)
  - Used to find approver with sufficient `Approval $` limit
- **Example**: If Frank's supervisor is Mike, and Mike's supervisor is CEO, approval chain is Frank → Mike → CEO

#### Field: Delegate
- **Location**: Third row, left
- **Type**: Dropdown (User ID lookup)
- **Required**: No
- **Database**: `wus_mstr.wus_delegate`
- **Business Rule**: 
  - **Admin-forced delegation** for users unable to set their own
  - Use when: User is out sick, left company suddenly, or incapacitated
  - Delegate can act on behalf of this user (approve their queue, etc.)
  - User-initiated delegation is done through iPurchase screens (not Admin)
- **Best Practice**: 
  > Instead of changing approval rules when someone leaves, set a delegate temporarily. Better yet, use groups in approval rules - remove the departing user from the group and add their replacement.

#### Field: Buyer Code
- **Location**: Fourth row, left
- **Type**: Text input
- **Required**: No
- **Database**: `wus_mstr.wus_erp_initials`
- **Business Rule**: 
  - Identifies user as a buyer in iPurchase
  - **Must match QAD buyer code** for each domain the user has access to
  - Validated at requisition entry time (not at user save)
  - Only buyers valid for the requisition's domain appear in buyer dropdowns
- **Example**: If user is buyer "JKS" in QAD for domains demo1 and demo2, enter "JKS" here. User must exist as buyer JKS in QAD for both domains.

#### Field: Approval $
- **Location**: Fifth row, left
- **Type**: Numeric (currency)
- **Required**: No
- **Default**: 0.00
- **Database**: `wus_mstr.wus_app_amt`
- **Business Rule**: 
  - Maximum amount this user can approve when supervisor chain routing is used
  - `0.00` = **No approval authority** (cannot approve anything via supervisor chain)
  - Value is in **base currency** (typically USD)
  - When `$SUPERVISORS` rule matches, system finds first supervisor in chain with `Approval $` >= requisition amount
- **Multi-Domain Note**: 
  > For multi-domain installations, consider converting all approval amounts to a single currency (e.g., USD). See `USE_SINGLE_CURRENCY` system setting.
- **Example**: If user has Approval $ of 5,000 and requisition is $7,500, approval goes to their supervisor (if supervisor has higher limit)

### Default/Security Fields (Middle and Right Columns)

These fields serve **dual purpose**:
1. **Default Value** - Pre-populates the field on new requisitions
2. **Security Restriction** - Limits which values the user can select

All these fields use the **Progress Can-Do list format** and are stored in `pf_mstr` (not `wus_mstr`).

#### Can-Do List Format

The Can-Do format is a comma-delimited list evaluated left-to-right:
- First entry becomes the **default value**
- `!` prefix means **exclude** this value
- `*` is wildcard (match anything)
- Blank value requires trailing/leading comma

**Examples:**

| Value | Interpretation |
|-------|----------------|
| `8000` | Default=8000, Only 8000 allowed |
| `8000,8001` | Default=8000, 8000 and 8001 allowed |
| `8000,8001,` | Default=8000, 8000/8001/blank allowed (trailing comma) |
| `,8000,8001` | Default=blank, 8000/8001/blank allowed (leading comma) |
| `8000,!8001,8*` | Default=8000, 8000 valid, 8001 excluded, anything starting with 8 valid |
| `5521,!5622,56*,7*,!*` | 5521 valid (default), 5622 excluded, 56xx valid, 7xxx valid, all others invalid |
| `*` | Any value allowed, no default |
| (blank) | No restriction, no default |

#### Field: Dept
- **Location**: Middle column, top
- **Type**: Text (Can-Do list)
- **Database**: `pf_mstr` where `pf_attr = 'Dept'`
- **Business Rule**: Default/allowed department codes for requisitions

#### Field: BillTo
- **Location**: Middle column, second row
- **Type**: Text (Can-Do list)
- **Database**: `pf_mstr` where `pf_attr = 'BillTo'`
- **Business Rule**: Default/allowed Bill-To addresses for requisitions

#### Field: Sub Acct
- **Location**: Middle column, third row
- **Type**: Text (Can-Do list)
- **Database**: `pf_mstr` where `pf_attr = 'Sub Acct'`
- **Business Rule**: Default/allowed sub-account codes for requisitions

#### Field: Default_ShipTo
- **Location**: Right column, top
- **Type**: Text (Can-Do list)
- **Database**: `pf_mstr` where `pf_attr = 'Default_ShipTo'`
- **Business Rule**: Default/allowed Ship-To addresses for requisitions

#### Field: Default_Site
- **Location**: Right column, second row
- **Type**: Text (Can-Do list)
- **Database**: `pf_mstr` where `pf_attr = 'Default_Site'`
- **Business Rule**: Default/allowed site codes for requisitions

#### Field: Default_ReqType
- **Location**: Right column, third row
- **Type**: Text (Can-Do list)
- **Database**: `pf_mstr` where `pf_attr = 'Default_ReqType'`
- **Business Rule**: Default/allowed requisition types (Expense, Capital, Inventory, etc.)

### Database Schema - iPurchase Tab

```sql
-- User Master (organizational fields)
wus_mstr
  wus_erp_id          VARCHAR(20)     -- Employee number (HR integration)
  wus_supervisor      VARCHAR(10)     -- FK → wus_mstr.wus_id
  wus_delegate        VARCHAR(10)     -- FK → wus_mstr.wus_id
  wus_erp_initials    VARCHAR(10)     -- Buyer code (must match QAD)
  wus_app_amt         DECIMAL(15,2)   -- Approval limit (base currency)

-- User Profile Fields (default/security values)
pf_mstr
  pf_us_id            VARCHAR(10)     -- User ID
  pf_group            VARCHAR(20)     -- Always "DEFAULT" for user profiles
  pf_attr             VARCHAR(50)     -- Field name (Dept, BillTo, etc.)
  pf_chr1             VARCHAR(500)    -- Can-Do list value
```

**Query Example - Get User's Department Restriction:**
```sql
SELECT pf_chr1 
FROM PUB.pf_mstr 
WHERE pf_us_id = 'andyE' 
  AND pf_group = 'DEFAULT' 
  AND pf_attr = 'Dept'
```

### System Setting: USER_PROFILE_FIELDS

The fields visible on this tab are controlled by the `USER_PROFILE_FIELDS` system setting.

- **Format**: Comma-delimited list of field names
- **Purpose**: Customize which default/security fields appear
- **Example**: `Dept,BillTo,Sub Acct,Default_ShipTo,Default_Site,Default_ReqType`

If your organization doesn't use certain fields (e.g., Sub Account), remove them from this setting to simplify the interface.

---

## Action Buttons (Below Form)

### Button: Save
- **Icon**: Disk/save icon
- **Action**: Commits user record to database
- **Validation**: 
  - Checks required fields (Name, Email, Domains)
  - Validates email format
  - Checks User ID uniqueness (for new users)
- **Database Impact**: 
  - INSERT on `wus_mstr` (new user)
  - UPDATE on `wus_mstr` (existing user)
- **Keyboard Shortcut**: Ctrl+S (if supported)

### Button: New
- **Icon**: Plus icon
- **Action**: Clears form to create new user
- **Behavior**: Prompts to save if unsaved changes exist

### Button: Delete
- **Icon**: Trash/X icon
- **Action**: Deletes current user record
- **Validation**: 
  - Cannot delete user with pending approvals
  - Cannot delete user referenced in audit trails
  - Confirmation prompt before deletion
- **Database Impact**: DELETE from `wus_mstr`
- **Business Rule**: 
  - Soft delete recommended (use Disabled instead)
  - Hard delete removes user from all historical records

### Button: Copy
- **Icon**: Copy icon
- **Action**: Creates new user by copying current user's settings
- **Behavior**: Prompts for new User ID, copies all other fields

### Button: Set Password
- **Icon**: Key icon
- **Action**: Opens password change dialog
- **Business Rule**: 
  - Administrator can reset user password
  - Password complexity rules apply (if configured)

### Button: Show License
- **Action**: Displays license information for current installation

### Button: Export Users
- **Icon**: Down arrow
- **Action**: Exports user list to CSV or Excel
- **Business Rule**: Exports all visible columns from User Browse grid

### Button: Import Users
- **Icon**: Up arrow
- **Action**: Imports users from CSV or Excel file
- **Business Rule**: 
  - Template must match exact field names
  - Validates all required fields
  - Can create or update users in bulk

### Button: Unlock User
- **Action**: Unlocks user account locked due to failed login attempts
- **Business Rule**: 
  - Only visible/enabled for locked accounts
  - Resets failed login counter

---

## User Browse Grid

See [Admin Browse Grid Component](../components/admin-browse.md) for full documentation on browse functionality including searching, column selection, sorting, pagination, and exporting.

**Default columns for this screen:**

| Column | Database Field | Notes |
|--------|----------------|-------|
| User Id | `wus_id` | Default sort column |
| Name | `wus_name` | |
| Title | `wus_title` | |
| Company | `wus_company` | |
| Mobile | `wus_fax` | Shows checkmark if populated |
| Expire Date | `wus_expire_date` | MM-DD-YYYY format |
| Failed Logins | `wus_failed_logins` | Count of consecutive failures |
| Disabled | `wus_disable` | Shows checkmark if disabled |

---

## Business Rules

### User Creation
1. **User ID must be unique** across all users
2. **Email must be unique** across all users
3. **Domains field is critical** for security - determines data access
4. **Required fields** must be completed before save
5. **User ID cannot be changed** after creation

### User Access Control
1. **Disabled users cannot login** but remain in database
2. **Expired users cannot login** after expiration date
3. **Locked users cannot login** until administrator unlocks
4. **Domain access** determines which requisitions/POs user can see

### Email Notifications
1. **Email field** used for all system notifications
2. **Invalid email** prevents approval notifications from being sent
3. **Email changes** do not affect pending approvals

### Supervisor Hierarchy
1. **Supervisor field** (see iPurchase tab) creates org chart
2. **Approval routing** follows supervisor chain
3. **Circular references** (A→B→A) should be avoided

---

## Database Schema

### Primary Table: wus_mstr (User Master)

```sql
-- User Info Tab Fields
wus_id                VARCHAR(10)     PRIMARY KEY     -- User ID
wus_name              VARCHAR(50)     NOT NULL        -- Full name
wus_email             VARCHAR(100)    NOT NULL        -- Email address
wus_expire_date       DATE                            -- Account expiration
wus_disable           BOOLEAN                         -- Disabled flag
wus_last_login        DATETIME                        -- Last login timestamp
wus_create_date       DATE                            -- Creation date
wus_create_by         VARCHAR(10)                     -- Creator User ID
wus_street1           VARCHAR(100)                    -- Address line 1
wus_street2           VARCHAR(100)                    -- Address line 2
wus_city              VARCHAR(50)                     -- City
wus_state             VARCHAR(2)                      -- State
wus_post              VARCHAR(10)                     -- Zip code
wus_country           VARCHAR(50)                     -- Country
wus_company           VARCHAR(100)                    -- Company
wus_title             VARCHAR(50)                     -- Job title
wus_phone             VARCHAR(20)                     -- Phone number
wus_fax               VARCHAR(20)                     -- Mobile number
wus_carrier           VARCHAR(50)                     -- Mobile carrier
wus_domains           VARCHAR(500)                    -- Accessible domains
wus_failed_logins     INTEGER                         -- Failed login count

-- iPurchase Tab Fields
wus_erp_id            VARCHAR(20)                     -- Employee number (HR integration)
wus_supervisor        VARCHAR(10)     FK → wus_id     -- Supervisor User ID
wus_delegate          VARCHAR(10)     FK → wus_id     -- Delegate User ID
wus_erp_initials      VARCHAR(10)                     -- Buyer code (QAD buyer)
wus_app_amt           DECIMAL(15,2)                   -- Approval limit (base currency)
```

### Group Tables

```sql
-- Group Master
wgr_mstr
  wgr_id              VARCHAR(20)     PRIMARY KEY     -- Group ID
  wgr_desc            VARCHAR(50)                     -- Group description

-- User-Group Membership
wugr_mstr
  wugr_gr_id          VARCHAR(20)     FK → wgr_id     -- Group ID
  wugr_us_id          VARCHAR(10)     FK → wus_id     -- User ID
```

### User Profile Fields (pf_mstr)

```sql
-- Default/Security values for requisition fields
pf_mstr
  pf_us_id            VARCHAR(10)                     -- User ID
  pf_group            VARCHAR(20)                     -- "DEFAULT" for user profiles
  pf_attr             VARCHAR(50)                     -- Field name
  pf_chr1             VARCHAR(500)                    -- Can-Do list value
  
-- Example records for user "andyE":
-- pf_us_id='andyE', pf_group='DEFAULT', pf_attr='Dept', pf_chr1='8000,8001,'
-- pf_us_id='andyE', pf_group='DEFAULT', pf_attr='Default_Site', pf_chr1='MAIN,WEST'
```

---

## Related Screens

- [Group Setup](./02-group-setup.md) - Manage groups and membership
- [Approval Rules](./03-approval-rules.md) - Configure approval workflows
- [System Settings](./04-system-settings.md) - System-wide configuration
- [Security](./05-security.md) - Password policies, login restrictions

---

## Common Issues

### Issue: "User ID already exists"
**Cause**: Attempting to create user with duplicate User ID  
**Solution**: Choose a different User ID or check if user already exists

### Issue: "Email already in use"
**Cause**: Email address assigned to another user  
**Solution**: Each user must have unique email address

### Issue: Cannot login after creating user
**Cause 1**: User marked as Disabled  
**Solution**: Uncheck Disabled checkbox

**Cause 2**: User not in CORE access group  
**Solution**: Add user to `** iPurchase CORE Access Group` on Groups tab

**Cause 3**: Domains field is blank or incorrect  
**Solution**: Set Domains to `*` or specific domain list

**Cause 4**: Password not set  
**Solution**: Use "Set Password" button to create initial password

### Issue: User not receiving approval emails
**Cause 1**: Invalid email address  
**Solution**: Verify email format is correct

**Cause 2**: Email server not configured  
**Solution**: Check System Settings for SMTP configuration

### Issue: User sees "No data available" in requisitions
**Cause**: Domains field doesn't match any requisition domains  
**Solution**: Update Domains field to include correct domain codes

### Issue: User cannot approve requisitions
**Cause 1**: Approval $ is 0.00  
**Solution**: Set appropriate approval amount on iPurchase tab

**Cause 2**: User not in approval routing  
**Solution**: Check approval rules or supervisor chain configuration

### Issue: User can't select certain cost centers
**Cause**: Dept field on iPurchase tab restricts access  
**Solution**: Update Can-Do list in Dept field to include needed values

### Issue: Buyer not appearing in dropdown during req entry
**Cause**: Buyer Code doesn't match QAD buyer for that domain  
**Solution**: Verify buyer code exists in QAD for the requisition's domain

### Issue: User left company, approvals stuck in their queue
**Solution 1**: Set Delegate on iPurchase tab to route to replacement  
**Solution 2 (Better)**: If using groups in approval rules, remove user from group and add replacement

---

## Technical Notes

### Case Sensitivity
- User IDs are **case-sensitive** in database and comparisons
- User `Frank` is different from user `frank`
- Email addresses are typically case-insensitive

### Domain Access Control
- Domains field controls which company data user can access
- Format: `demo1,demo2` or `*` for all
- Used in WHERE clauses: `xxreq_domain IN (user_domains)`
- Critical for multi-company installations

### Performance Considerations
- User Browse grid loads all users on screen load
- For systems with 1000+ users, pagination is essential
- User ID lookups are indexed (primary key)

### Security
- Passwords stored as hashed values (not visible)
- Failed login counter increments on bad password
- Account locks after N failed attempts (configurable)
- Administrator can unlock via "Unlock User" button

---

## Keyboard Shortcuts

- **Ctrl+S**: Save (if supported)
- **Ctrl+N**: New (if supported)
- **Tab**: Move to next field
- **Shift+Tab**: Move to previous field

---

## Tips & Best Practices

### User Management
1. **Use consistent User ID naming convention** (e.g., FirstLast, flast, first.last)
2. **Set expiration dates for temporary users** (contractors, consultants)
3. **Use Disabled instead of Delete** to preserve historical records
4. **Export users regularly** for backup purposes
5. **Review Failed Logins column** to identify potential security issues

### Groups & Approval Rules
6. **Use groups as approvers in rules, not individual users** - even for single-person "groups"
7. **When employees leave**: Update group membership, not approval rules
8. **License groups must be manually populated** after LICENSE setting changes
9. **Create logical groups** for departments, approval levels, or functional areas

### Security & Defaults (iPurchase Tab)
10. **Set Domains carefully** - incorrect setting causes data access issues
11. **Use Can-Do lists to enforce security** - restrict users to their cost centers
12. **Remember leading/trailing commas** in Can-Do lists for blank values
13. **Test new user login and req entry** immediately after setup

### Supervisor & Delegation
14. **Build supervisor chain top-down** - create executives before their reports
15. **Avoid deep supervisor chains** - slows approval routing
16. **Use Delegate for temporary absences** - better than changing rules
17. **Set Approval $ appropriately** - 0.00 means no supervisor-chain approval authority

---

## See Also

- [iPurchase Tab Documentation](./01b-users-and-groups-ipurchase-tab.md) - Approval limits, supervisor settings
- [Groups Tab Documentation](./01c-users-and-groups-groups-tab.md) - Group membership
- [Approval Workflow](../workflows/approval-routing.md) - How user settings affect approvals
- [Database Schema Reference](../technical/database-schema.md) - Complete wus_mstr schema

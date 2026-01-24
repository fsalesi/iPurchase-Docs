---
screen_id: ipurchase_user_roles
screen_name: User Roles
module: iPurchase
access_level: Administrator
database_tables:
  - xxrole_mstr
related_screens:
  - ipurchase_approval_rules
  - ipurchase_approval_rules_simple
screenshot: ../screenshots/ipurchase-user-roles/01-main-screen.png
last_updated: 2025-01-24
author: Frank Salesi
---

# User Roles

## Overview

The User Roles screen defines role-based approver mappings. Instead of hard-coding specific users in approval rules, you can use role variables like `$Cost Center:Manager` that dynamically resolve to the appropriate approver based on the requisition data.

This creates a powerful abstraction layer:
- **Approval Rules** define WHEN approval is needed (e.g., "Cost Center Manager approval required over $5K")
- **User Roles** define WHO fills each role (e.g., "Frank is the Manager for Cost Center 2000")

When personnel change, you only update the User Roles mappings - approval rules remain unchanged.

## How Role Variables Work

Role variables follow the format: `$Type:Role`

**Hard-coded Types** (fixed in system):
- Account
- Cost Center
- Project
- Site
- Sub Account

**Configurable Roles** (defined in ROLES system setting):
- Manager, Director, VP, SVP (or whatever your organization needs)

**Resolution Example:**

```
Requisition Line: Cost Center = 2000

Approval Rule uses: $Cost Center:Manager

System looks up xxrole_mstr:
  WHERE xxrole_domain IN ('*', 'demo1')
    AND xxrole_type = 'Cost Center'
    AND xxrole_value = '2000'
    AND xxrole_role = 'Manager'
  
Returns: xxrole_approver = 'Andy'

Result: Andy is added to approval routing
```

## Access Path

Administration → User Roles

## Screenshot

![User Roles Main Screen](../screenshots/ipurchase-user-roles/01-main-screen.png)

## Screen Layout

The screen consists of:

1. **User Roles** - Role mapping form
2. **User Roles Browse** - Grid listing all role mappings

---

## User Roles Form

### Field: Domain

- **Type**: Dropdown
- **Required**: Yes
- **Options**: All Domains, or specific domain
- **Description**: Which domain this role mapping applies to
- **Database**: `xxrole_domain` (`*` for All Domains)

### Field: Role

- **Type**: Dropdown
- **Required**: Yes
- **Options**: Populated from `ROLES` system setting
- **Description**: The role being assigned (Manager, Director, VP, SVP, etc.)
- **Database**: `xxrole_role`

### Field: Type

- **Type**: Dropdown
- **Required**: Yes
- **Options**: Account, Cost Center, Project, Site, Sub Account (hard-coded)
- **Description**: The dimension this role applies to
- **Database**: `xxrole_type`

### Field: Value

- **Type**: Text input
- **Required**: Yes
- **Description**: The specific value for the Type (e.g., Cost Center number, Account code, Project ID)
- **Database**: `xxrole_value`
- **Examples**: `2000` (Cost Center), `8200` (Account), `Test1` (Project), `10000` (Site)

### Field: Approver

- **Type**: Text with lookup
- **Required**: Yes
- **Description**: User ID or group that fills this role. Click magnifying glass for user/group picker.
- **Database**: `xxrole_approver`

---

## Action Buttons

| Button | Action |
|--------|--------|
| **Save** | Saves the role mapping |
| **New** | Clears form to create a new mapping |
| **Delete** | Deletes the selected mapping |
| **Copy** | Duplicates the mapping (useful for creating similar mappings) |
| **Notes** | Add documentation notes |
| **Audit** | View change history |
| **Import Roles** | Bulk import role mappings from CSV file |

---

## User Roles Browse

### Browse Columns

| Column | Description |
|--------|-------------|
| Domain | Domain or "All Domains" |
| Type | Account, Cost Center, Project, Site, or Sub Account |
| Value | The specific value for the type |
| Approver | User or group assigned to this role |
| Role | Manager, Director, VP, SVP, etc. |

---

## Database Table

**Table: `xxrole_mstr`**

| Field | Type | Description |
|-------|------|-------------|
| `xxrole_domain` | character | Domain (`*` = all domains) |
| `xxrole_type` | character | Type (Account, Cost Center, Project, Site, Sub Account) |
| `xxrole_value` | character | Specific value for the type |
| `xxrole_role` | character | Role name (from ROLES setting) |
| `xxrole_approver` | character | User ID or group |

**Query Example:**
```sql
SELECT xxrole_domain, xxrole_type, xxrole_value, xxrole_role, xxrole_approver
FROM PUB.xxrole_mstr
WHERE xxrole_domain IN ('*', 'demo1')
  AND xxrole_type = 'Cost Center'
ORDER BY xxrole_value, xxrole_role
```

---

## Import Roles

The **Import Roles** button allows bulk importing of role mappings from a CSV file. This is useful for:
- Initial setup with many cost centers/accounts
- Annual updates when organizational changes occur
- Migrating from another system

---

## Examples

### Example 1: Cost Center Management Chain

Define a complete approval chain for Cost Center 2000:

| Domain | Type | Value | Role | Approver |
|--------|------|-------|------|----------|
| All Domains | Cost Center | 2000 | Manager | Andy |
| All Domains | Cost Center | 2000 | Director | Adriel |
| All Domains | Cost Center | 2000 | VP | CFO_Group |

Now approval rules can use:
- `$Cost Center:Manager` → Andy
- `$Cost Center:Director` → Adriel
- `$Cost Center:VP` → CFO_Group

### Example 2: Account-Based Approval

Define approvers by GL Account:

| Domain | Type | Value | Role | Approver |
|--------|------|-------|------|----------|
| All Domains | Account | 8200 | Manager | Frank |
| All Domains | Account | 8200 | Director | Andy |
| All Domains | Account | 8300 | Manager | Peter |
| All Domains | Account | 8300 | Director | Glenn |

### Example 3: Domain-Specific Roles

Different approvers for different domains:

| Domain | Type | Value | Role | Approver |
|--------|------|-------|------|----------|
| demo1 | Cost Center | 2000 | Manager | Andy |
| demo2 | Cost Center | 2000 | Manager | Sarah |

---

## Using Role Variables in Approval Rules

### In Simple Rules (xxapp_mstr)

Set the Approvers field to: `$Cost Center:Manager`

### In Complex Rules (xxAppRule)

Set the User/Group List field to: `$Cost Center:Manager`

### Multiple Role Variables

You can use comma-separated role variables:
`$Cost Center:Manager,$Cost Center:Director`

This adds both the Manager AND Director for the cost center(s) on the requisition.

---

## Tips & Best Practices

1. **Use "All Domains" when possible** - Reduces maintenance if roles are the same across domains

2. **Create complete role chains** - If using `$Cost Center:Manager` and `$Cost Center:Director`, ensure both roles are defined for each cost center

3. **Use groups for shared roles** - If multiple people can approve as "VP", create a group and assign the group as the approver

4. **Document with Notes** - Explain why specific people are assigned to roles

5. **Regular audits** - Review role mappings when personnel change

6. **Handle missing roles** - Configure `ROLE_MISSING_SKIP_LIST` to control behavior when a role mapping doesn't exist

---

## Related System Settings

| Setting | Description |
|---------|-------------|
| **ROLES** | Comma-separated list of role names available in the Role dropdown (e.g., `Manager,Director,VP,SVP`) |
| **ROLE_MISSING_SKIP_LIST** | Types where missing role mappings are silently skipped. If a Type is NOT in this list and has no mapping, approval engine throws an error. |

See [Approval Workflow Settings](../../reference/system-settings-reference.md#approval-workflow) for complete list.

---

## Related Screens

- [Approval Rules (Complex)](./ipurchase-01-approval-rules.md) - Use role variables in complex rules
- [Approval Rules - Simple](./ipurchase-02-approval-rules-simple.md) - Use role variables in simple rules
- [System Settings](./02-system-settings.md) - Configure ROLES and ROLE_MISSING_SKIP_LIST

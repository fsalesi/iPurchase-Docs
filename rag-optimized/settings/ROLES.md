# ROLES - iPurchase System Setting

**Category:** Approval Workflow

Defines the list of role names available for assignment in the User Roles screen, enabling role-based approval routing.

### How It Works

iPurchase supports role-based approval routing using variables like `$Cost Center:Manager` or `$Project:Director`. This setting defines which role names (Manager, Director, VP, etc.) are available.

**Role Variables are constructed as:**
```
$[Type]:[Role]
```

Where:
- **Type** = Cost Center, Account, Project, Sub Account, Site (hard-coded)
- **Role** = Names defined in this ROLES setting

**Example:**
```sql
ROLES = "Manager,Director,VP,SVP,CFO"
```

This enables approval variables like:
- `$Cost Center:Manager` - Manager of the requisition's cost center
- `$Project:Director` - Director assigned to the project
- `$Account:VP` - VP responsible for the GL account

### Valid Values

Comma-separated list of role names. Names should be:
- Meaningful to your organization
- Consistent with your approval hierarchy
- Used in User Roles screen assignments

**Common examples:**
- `Manager,Director,VP,SVP,CFO`
- `Supervisor,Manager,SeniorManager,Director`
- `Owner,Approver,FinalApprover`

### Common Questions

- How do I create role-based approval rules?
- What roles are available in iPurchase?
- How do I add a new approval role?
- How do $Cost Center:Manager variables work?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ROLES |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ROLES'
```

### Related Settings

- [ROLE_MISSING_SKIP_LIST](ROLE_MISSING_SKIP_LIST.md) - Handle missing role mappings

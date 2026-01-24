# FORCE_APPROVAL_ROLE_LIST - iPurchase System Setting

**Category:** Approval Workflow

Comma Separated list of User ID's or Group ID's that are allowed to Force Approve any requisition.  Force Approval bypasses all open approvals and creates a PO. A history of this action is maintained for audit purposes. Allow_Approver_Changes must also be set to TRUE and this group must also be listed in the "Allow_Approver_Changes_Roles" setting. Asterisk indicates everyone, a blank indicates no one.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

### Valid Values

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone/all users |
| Blank/empty | No one/disabled |
| User/Group list | Only specified users/groups |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | FORCE_APPROVAL_ROLE_LIST |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'FORCE_APPROVAL_ROLE_LIST'
```

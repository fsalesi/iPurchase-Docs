# ROLE_MISSING_SKIP_LIST - iPurchase System Setting

**Category:** Approval Workflow

Comma-separated list of Types (Cost Center, Account, Project, Sub Account, Site). If a role mapping is missing for a Type in this list, the approval engine skips that approver silently. If a Type is NOT in this list and has no role mapping, the engine throws an error blocking submission. Example: If Cost Center is in this list and CC 8200 has no Manager defined, the rule skips that approval. If Cost Center is NOT in this list, user gets error: No Manager defined for Cost Center 8200.

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
| **Setting Name** | ROLE_MISSING_SKIP_LIST |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ROLE_MISSING_SKIP_LIST'
```

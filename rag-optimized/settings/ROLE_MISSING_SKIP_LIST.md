# ROLE_MISSING_SKIP_LIST - iPurchase System Setting

**Category:** Approval Workflow

Controls which approval role types are silently skipped when no role mapping exists, versus which types throw an error blocking submission.

### How It Works

iPurchase uses role-based approval variables like `$Cost Center:Manager` or `$Project:Director`. These require role mappings to be defined in the User Roles screen. But what happens when a mapping is missing?

This setting lists the Types (Cost Center, Account, Project, Sub Account, Site) that should be **silently skipped** if no role mapping exists.

**Behavior:**
- Type **IN** this list + no mapping = approver silently skipped, req proceeds
- Type **NOT IN** this list + no mapping = error thrown, submission blocked

**Example:**
```sql
ROLE_MISSING_SKIP_LIST = "Cost Center,Project"
```

- Req uses CC 8200, no Manager defined for 8200 → skip that approver, continue
- Req uses Account 5100, no Manager defined for 5100 → ERROR: "No Manager defined for Account 5100"

### Valid Values

Comma-separated list of role types:
- `Cost Center`
- `Account`
- `Project`
- `Sub Account`
- `Site`

### Common Questions

- Why am I getting "No Manager defined for Cost Center" errors?
- How do I skip missing role mappings instead of blocking submission?
- What happens when a role mapping doesn't exist?
- How do I make certain role types optional?

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

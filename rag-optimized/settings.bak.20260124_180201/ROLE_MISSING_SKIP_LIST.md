# ROLE_MISSING_SKIP_LIST - iPurchase System Setting

**Category:** Approval Workflow

Comma-separated list of Types (Cost Center, Account, Project, Sub Account, Site). If a role mapping is missing for a Type in this list, the approval engine skips that approver silently. If a Type i...

**Common questions this answers:**
- What is ROLE_MISSING_SKIP_LIST?
- What does ROLE_MISSING_SKIP_LIST do?
- What is the default value for ROLE_MISSING_SKIP_LIST?
- How do I configure ROLE_MISSING_SKIP_LIST?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ROLE_MISSING_SKIP_LIST |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ROLE_MISSING_SKIP_LIST'
```

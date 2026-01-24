# ROLES - iPurchase System Setting

**Category:** Approval Workflow

Comma-separated list of role names that can be assigned in the User Roles screen. These roles are combined with hard-coded Types (Account, Cost Center, Project, Site, Sub Account) to create approva...

**Common questions this answers:**
- What is ROLES?
- What does ROLES do?
- What is the default value for ROLES?
- How do I configure ROLES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ROLES |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ROLES'
```

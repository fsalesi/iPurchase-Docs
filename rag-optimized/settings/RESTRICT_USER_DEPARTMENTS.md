# RESTRICT_USER_DEPARTMENTS - iPurchase System Setting

**Category:** User Management

Is the department selection limited to those departments defined in the user's profile?  If the value of this is True then in User Maintenance you should set up the "Default Dept" field as follows....

**Common questions this answers:**
- What is RESTRICT_USER_DEPARTMENTS?
- What does RESTRICT_USER_DEPARTMENTS do?
- What is the default value for RESTRICT_USER_DEPARTMENTS?
- How do I configure RESTRICT_USER_DEPARTMENTS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RESTRICT_USER_DEPARTMENTS |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RESTRICT_USER_DEPARTMENTS'
```

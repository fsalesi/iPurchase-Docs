# RESTRICT_USER_SUB_ACCOUNTS - iPurchase System Setting

**Category:** User Management

Is the Sub Acct selection limited to those sub accounts defined in the user's profile? See RESTRICT_USER_DEPARTMENTS for more information on how to set the Sub Acct field in User Maintenance

**Common questions this answers:**
- What is RESTRICT_USER_SUB_ACCOUNTS?
- What does RESTRICT_USER_SUB_ACCOUNTS do?
- What is the default value for RESTRICT_USER_SUB_ACCOUNTS?
- How do I configure RESTRICT_USER_SUB_ACCOUNTS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RESTRICT_USER_SUB_ACCOUNTS |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RESTRICT_USER_SUB_ACCOUNTS'
```

# OOF_LIMIT_BY_DEPT - iPurchase System Setting

**Category:** GL Accounts & Finance

A setting of True will only allow a user to delegate to another user who shares a same department. A setting of FIRST A setting will only allow a user to delegate to another user who is in the orig...

**Common questions this answers:**
- What is OOF_LIMIT_BY_DEPT?
- What does OOF_LIMIT_BY_DEPT do?
- What is the default value for OOF_LIMIT_BY_DEPT?
- How do I configure OOF_LIMIT_BY_DEPT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_LIMIT_BY_DEPT |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_LIMIT_BY_DEPT'
```

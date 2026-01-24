# EMPLOYMENT_DEPT_LIST - iPurchase System Setting

**Category:** User Management

Comma-separated department codes. Valid departments for user employment records/profiles.

**Common questions this answers:**
- What is EMPLOYMENT_DEPT_LIST?
- What does EMPLOYMENT_DEPT_LIST do?
- What is the default value for EMPLOYMENT_DEPT_LIST?
- How do I configure EMPLOYMENT_DEPT_LIST?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMPLOYMENT_DEPT_LIST |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMPLOYMENT_DEPT_LIST'
```

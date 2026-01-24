# DEPARTMENTS_USE_ORIG - iPurchase System Setting

**Category:** GL Accounts & Finance

This setting allows the administrator to set the drop down list of departments at the line entry. If set to TRUE the list will be based on the originator.  If set to FALSE, the department is set ba...

**Common questions this answers:**
- What is DEPARTMENTS_USE_ORIG?
- What does DEPARTMENTS_USE_ORIG do?
- What is the default value for DEPARTMENTS_USE_ORIG?
- How do I configure DEPARTMENTS_USE_ORIG?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEPARTMENTS_USE_ORIG |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEPARTMENTS_USE_ORIG'
```

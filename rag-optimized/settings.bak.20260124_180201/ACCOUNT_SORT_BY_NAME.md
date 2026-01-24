# ACCOUNT_SORT_BY_NAME - iPurchase System Setting

**Category:** GL Accounts & Finance

A value of true will show the accounts sorted by name. Any other value will sort by number.

**Common questions this answers:**
- What is ACCOUNT_SORT_BY_NAME?
- What does ACCOUNT_SORT_BY_NAME do?
- What is the default value for ACCOUNT_SORT_BY_NAME?
- How do I configure ACCOUNT_SORT_BY_NAME?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_SORT_BY_NAME |
| **Category** | GL Accounts & Finance |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_SORT_BY_NAME'
```

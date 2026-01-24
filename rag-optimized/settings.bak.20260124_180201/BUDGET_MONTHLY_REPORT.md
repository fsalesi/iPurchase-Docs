# BUDGET_MONTHLY_REPORT - iPurchase System Setting

**Category:** GL Accounts & Finance

Can-Do list. Users/groups allowed to access budget monthly reports. Automatically disabled in archive systems.

**Common questions this answers:**
- What is BUDGET_MONTHLY_REPORT?
- What does BUDGET_MONTHLY_REPORT do?
- What is the default value for BUDGET_MONTHLY_REPORT?
- How do I configure BUDGET_MONTHLY_REPORT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_MONTHLY_REPORT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_MONTHLY_REPORT'
```

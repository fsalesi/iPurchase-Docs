# BUDGET_ADMINISTRATOR - iPurchase System Setting

**Category:** GL Accounts & Finance

Comma Separated list of User ID's or Group ID's who are allowed to maintain budgets in iPurchase. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is BUDGET_ADMINISTRATOR?
- What does BUDGET_ADMINISTRATOR do?
- What is the default value for BUDGET_ADMINISTRATOR?
- How do I configure BUDGET_ADMINISTRATOR?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_ADMINISTRATOR |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_ADMINISTRATOR'
```

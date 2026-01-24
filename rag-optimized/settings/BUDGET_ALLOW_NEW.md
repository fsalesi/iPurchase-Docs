# BUDGET_ALLOW_NEW - iPurchase System Setting

**Category:** User Management

Comma Separated list of User ID's or Group ID's who are allowed to create new budgets in iPurchase. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is BUDGET_ALLOW_NEW?
- What does BUDGET_ALLOW_NEW do?
- What is the default value for BUDGET_ALLOW_NEW?
- How do I configure BUDGET_ALLOW_NEW?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BUDGET_ALLOW_NEW |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_ALLOW_NEW'
```

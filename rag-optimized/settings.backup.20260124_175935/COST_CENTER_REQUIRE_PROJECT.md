# COST_CENTER_REQUIRE_PROJECT - iPurchase System Setting

**Category:** GL Accounts & Finance

Can-Do list. Cost centers that require a project code. Validation error if project is blank for these cost centers.

**Common questions this answers:**
- What is COST_CENTER_REQUIRE_PROJECT?
- What does COST_CENTER_REQUIRE_PROJECT do?
- What is the default value for COST_CENTER_REQUIRE_PROJECT?
- How do I configure COST_CENTER_REQUIRE_PROJECT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | COST_CENTER_REQUIRE_PROJECT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'COST_CENTER_REQUIRE_PROJECT'
```

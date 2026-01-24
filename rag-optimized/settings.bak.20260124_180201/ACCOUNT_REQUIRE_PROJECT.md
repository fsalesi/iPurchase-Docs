# ACCOUNT_REQUIRE_PROJECT - iPurchase System Setting

**Category:** GL Accounts & Finance

A list of accounts which will always require a Project Code

**Common questions this answers:**
- What is ACCOUNT_REQUIRE_PROJECT?
- What does ACCOUNT_REQUIRE_PROJECT do?
- What is the default value for ACCOUNT_REQUIRE_PROJECT?
- How do I configure ACCOUNT_REQUIRE_PROJECT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_REQUIRE_PROJECT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_REQUIRE_PROJECT'
```

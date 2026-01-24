# RT_REQUIRE_PROJECT - iPurchase System Setting

**Category:** GL Accounts & Finance

List of requisition typles that require a project code.

**Common questions this answers:**
- What is RT_REQUIRE_PROJECT?
- What does RT_REQUIRE_PROJECT do?
- What is the default value for RT_REQUIRE_PROJECT?
- How do I configure RT_REQUIRE_PROJECT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_REQUIRE_PROJECT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | Capital |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_REQUIRE_PROJECT'
```

# TAX_USAGE_FIELD - iPurchase System Setting

**Category:** GL Accounts & Finance

[LEGACY/OBSOLETE] Field name for tax usage in data upgrades. Commented out in code.

**Common questions this answers:**
- What is TAX_USAGE_FIELD?
- What does TAX_USAGE_FIELD do?
- What is the default value for TAX_USAGE_FIELD?
- How do I configure TAX_USAGE_FIELD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TAX_USAGE_FIELD |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TAX_USAGE_FIELD'
```

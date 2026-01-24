# ACCOUNT_RANGE_CANDO - iPurchase System Setting

**Category:** GL Accounts & Finance

This is a comma separated list of accounts that can be used with iPurchase. The field uses the Progress �Can-Do� function. See Progress help if needed. A sample value can be 5521,!5622,56*,7*,!* Th...

**Common questions this answers:**
- What is ACCOUNT_RANGE_CANDO?
- What does ACCOUNT_RANGE_CANDO do?
- What is the default value for ACCOUNT_RANGE_CANDO?
- How do I configure ACCOUNT_RANGE_CANDO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_RANGE_CANDO |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_RANGE_CANDO'
```

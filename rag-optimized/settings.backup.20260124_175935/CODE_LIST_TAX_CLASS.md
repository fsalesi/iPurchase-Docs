# CODE_LIST_TAX_CLASS - iPurchase System Setting

**Category:** GL Accounts & Finance



**Common questions this answers:**
- What is CODE_LIST_TAX_CLASS?
- What does CODE_LIST_TAX_CLASS do?
- What is the default value for CODE_LIST_TAX_CLASS?
- How do I configure CODE_LIST_TAX_CLASS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_TAX_CLASS |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | comma-separated list of tax classes. List: is not needed on this setting |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_TAX_CLASS'
```

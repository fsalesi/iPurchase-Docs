# DEFAULT_TAX_ENVIRONMENT - iPurchase System Setting

**Category:** GL Accounts & Finance

You can use this to set the Tax Environment field in QAD. If set this will default for all Purchase Orders

**Common questions this answers:**
- What is DEFAULT_TAX_ENVIRONMENT?
- What does DEFAULT_TAX_ENVIRONMENT do?
- What is the default value for DEFAULT_TAX_ENVIRONMENT?
- How do I configure DEFAULT_TAX_ENVIRONMENT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_TAX_ENVIRONMENT |
| **Category** | GL Accounts & Finance |
| **Owner** |  |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_TAX_ENVIRONMENT'
```

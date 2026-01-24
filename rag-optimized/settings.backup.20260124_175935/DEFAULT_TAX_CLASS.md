# DEFAULT_TAX_CLASS - iPurchase System Setting

**Category:** GL Accounts & Finance

You can use this to set the Tax Class field in QAD. If set this will default for all Purchase Orders

**Common questions this answers:**
- What is DEFAULT_TAX_CLASS?
- What does DEFAULT_TAX_CLASS do?
- What is the default value for DEFAULT_TAX_CLASS?
- How do I configure DEFAULT_TAX_CLASS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_TAX_CLASS |
| **Category** | GL Accounts & Finance |
| **Owner** |  |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_TAX_CLASS'
```

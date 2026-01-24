# RT_REQ_TAXABLE - iPurchase System Setting

**Category:** GL Accounts & Finance

Comma-separated req types. Types where tax is calculated. If blank, all types are taxable.

**Common questions this answers:**
- What is RT_REQ_TAXABLE?
- What does RT_REQ_TAXABLE do?
- What is the default value for RT_REQ_TAXABLE?
- How do I configure RT_REQ_TAXABLE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_REQ_TAXABLE |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_REQ_TAXABLE'
```

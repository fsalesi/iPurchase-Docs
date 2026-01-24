# TAX_CUSTOMER - iPurchase System Setting

**Category:** GL Accounts & Finance

Default tax customer code for tax calculations.

**Common questions this answers:**
- What is TAX_CUSTOMER?
- What does TAX_CUSTOMER do?
- What is the default value for TAX_CUSTOMER?
- How do I configure TAX_CUSTOMER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TAX_CUSTOMER |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TAX_CUSTOMER'
```

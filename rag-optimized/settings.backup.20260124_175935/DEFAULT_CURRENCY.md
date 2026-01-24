# DEFAULT_CURRENCY - iPurchase System Setting

**Category:** System Configuration

The administrator can set a default currency for iPurchase.  Must be a valid currency.

**Common questions this answers:**
- What is DEFAULT_CURRENCY?
- What does DEFAULT_CURRENCY do?
- What is the default value for DEFAULT_CURRENCY?
- How do I configure DEFAULT_CURRENCY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_CURRENCY |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_CURRENCY'
```

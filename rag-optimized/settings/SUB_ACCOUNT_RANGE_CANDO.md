# SUB_ACCOUNT_RANGE_CANDO - iPurchase System Setting

**Category:** GL Accounts & Finance

This is the same as ACCOUNT_RANGE_CANDO except this applies to sub accounts. USE RT_....

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUB_ACCOUNT_RANGE_CANDO |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUB_ACCOUNT_RANGE_CANDO'
```

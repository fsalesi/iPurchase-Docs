# CODE_LIST_TAX_CLASS - iPurchase System Setting

**Category:** GL Accounts & Finance



### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_TAX_CLASS |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | comma-separated list of tax classes. List: is not needed on this setting |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_TAX_CLASS'
```

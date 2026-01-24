# ACCOUNT_SORT_BY_NAME - iPurchase System Setting

**Category:** GL Accounts & Finance

A value of true will show the accounts sorted by name. Any other value will sort by number.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_SORT_BY_NAME |
| **Category** | GL Accounts & Finance |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_SORT_BY_NAME'
```

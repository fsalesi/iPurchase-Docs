# SUB_ACCOUNT_SORT_BY_NAME - iPurchase System Setting

**Category:** GL Accounts & Finance

True or False A value of TRUE will show the sub-accounts sorted by name.

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUB_ACCOUNT_SORT_BY_NAME |
| **Category** | GL Accounts & Finance |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUB_ACCOUNT_SORT_BY_NAME'
```

### Related Settings

- [SUB_ACCOUNTS_USE_ORIG](SUB_ACCOUNTS_USE_ORIG.md)
- [SUB_ACCOUNT_RANGE_CANDO](SUB_ACCOUNT_RANGE_CANDO.md)
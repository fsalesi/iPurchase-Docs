# SUB_ACCOUNTS_USE_ORIG - iPurchase System Setting

**Category:** GL Accounts & Finance

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | uses originator's allowed sub-accounts instead of OBO's |
| **FALSE** | Disables this feature |

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUB_ACCOUNTS_USE_ORIG |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUB_ACCOUNTS_USE_ORIG'
```

### Related Settings

- [SUB_ACCOUNT_RANGE_CANDO](SUB_ACCOUNT_RANGE_CANDO.md)
- [SUB_ACCOUNT_SORT_BY_NAME](SUB_ACCOUNT_SORT_BY_NAME.md)
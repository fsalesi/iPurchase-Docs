# ACCOUNT_SORT_BY_NAME - iPurchase System Setting

**Category:** GL Accounts & Finance

A value of true will show the accounts sorted by name.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

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

### Related Settings

- [ACCOUNT_RANGE_CANDO](ACCOUNT_RANGE_CANDO.md)
- [ACCOUNT_REQUIRE_PROJECT](ACCOUNT_REQUIRE_PROJECT.md)
- [ACCOUNT_SHOW_CUSTOMNOTE](ACCOUNT_SHOW_CUSTOMNOTE.md)

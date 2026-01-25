# ACCOUNT_REQUIRE_PROJECT - iPurchase System Setting

**Category:** GL Accounts & Finance

A list of accounts which will always require a Project Code

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_REQUIRE_PROJECT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_REQUIRE_PROJECT'
```

### Related Settings

- [ACCOUNT_RANGE_CANDO](ACCOUNT_RANGE_CANDO.md)
- [ACCOUNT_SHOW_CUSTOMNOTE](ACCOUNT_SHOW_CUSTOMNOTE.md)
- [ACCOUNT_SORT_BY_NAME](ACCOUNT_SORT_BY_NAME.md)

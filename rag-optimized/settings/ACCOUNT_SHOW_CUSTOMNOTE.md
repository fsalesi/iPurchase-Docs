# ACCOUNT_SHOW_CUSTOMNOTE - iPurchase System Setting

**Category:** GL Accounts & Finance

Show the value CustomNote Field on the GL record - only for EE

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This display setting controls what information is visible to users in the interface.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_SHOW_CUSTOMNOTE |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_SHOW_CUSTOMNOTE'
```

### Related Settings

- [ACCOUNT_RANGE_CANDO](ACCOUNT_RANGE_CANDO.md)
- [ACCOUNT_REQUIRE_PROJECT](ACCOUNT_REQUIRE_PROJECT.md)
- [ACCOUNT_SORT_BY_NAME](ACCOUNT_SORT_BY_NAME.md)
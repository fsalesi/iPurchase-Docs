# ACCOUNT_RANGE_CANDO - iPurchase System Setting

**Category:** GL Accounts & Finance

This is a comma separated list of accounts that can be used with iPurchase.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) to specify which users or groups have access.

**Common configurations:**
- `*` - All users/everyone
- (blank) - No one/feature disabled
- `user1,user2` - Specific users only
- `group1,!user1` - Group members except specific user

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_RANGE_CANDO |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_RANGE_CANDO'
```

### Related Settings

- [ACCOUNT_REQUIRE_PROJECT](ACCOUNT_REQUIRE_PROJECT.md)
- [ACCOUNT_SHOW_CUSTOMNOTE](ACCOUNT_SHOW_CUSTOMNOTE.md)
- [ACCOUNT_SORT_BY_NAME](ACCOUNT_SORT_BY_NAME.md)

# SUB_ACCOUNT_RANGE_CANDO - iPurchase System Setting

**Category:** GL Accounts & Finance

This is the same as ACCOUNT_RANGE_CANDO except this applies to sub accounts.

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
| **Setting Name** | SUB_ACCOUNT_RANGE_CANDO |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUB_ACCOUNT_RANGE_CANDO'
```

### Related Settings

- [SUB_ACCOUNTS_USE_ORIG](SUB_ACCOUNTS_USE_ORIG.md)
- [SUB_ACCOUNT_SORT_BY_NAME](SUB_ACCOUNT_SORT_BY_NAME.md)
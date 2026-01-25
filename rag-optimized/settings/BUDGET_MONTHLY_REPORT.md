# BUDGET_MONTHLY_REPORT - iPurchase System Setting

**Category:** GL Accounts & Finance

Can-Do list.

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
| **Setting Name** | BUDGET_MONTHLY_REPORT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_MONTHLY_REPORT'
```

### Related Settings

- [BUDGET_ADMINISTRATOR](BUDGET_ADMINISTRATOR.md)
- [BUDGET_ASST_EDIT](BUDGET_ASST_EDIT.md)
- [BUDGET_HIDE_OTHER](BUDGET_HIDE_OTHER.md)

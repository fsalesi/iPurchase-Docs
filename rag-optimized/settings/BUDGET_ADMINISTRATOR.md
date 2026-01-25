# BUDGET_ADMINISTRATOR - iPurchase System Setting

**Category:** GL Accounts & Finance

Comma Separated list of User ID's or Group ID's who are allowed to maintain budgets in iPurchase.

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
| **Setting Name** | BUDGET_ADMINISTRATOR |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BUDGET_ADMINISTRATOR'
```

### Related Settings

- [BUDGET_ASST_EDIT](BUDGET_ASST_EDIT.md)
- [BUDGET_HIDE_OTHER](BUDGET_HIDE_OTHER.md)
- [BUDGET_MGR_EDIT](BUDGET_MGR_EDIT.md)
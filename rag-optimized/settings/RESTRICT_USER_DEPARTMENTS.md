# RESTRICT_USER_DEPARTMENTS - iPurchase System Setting

**Category:** User Management

Is the department selection limited to those departments defined in the user's profile?  If the value of this is True then in User Maintenance you should set up the "Default Dept" field as follows.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

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
| **Setting Name** | RESTRICT_USER_DEPARTMENTS |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RESTRICT_USER_DEPARTMENTS'
```

### Related Settings

- [RESTRICT_USER_ACCOUNTS](RESTRICT_USER_ACCOUNTS.md)
- [RESTRICT_USER_SUB_ACCOUNTS](RESTRICT_USER_SUB_ACCOUNTS.md)

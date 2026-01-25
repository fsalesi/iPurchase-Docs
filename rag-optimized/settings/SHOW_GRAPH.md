# SHOW_GRAPH - iPurchase System Setting

**Category:** Uncategorized

Comma separated list of User ID's or group ID's that have access to the graphing functionality.

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
| **Setting Name** | SHOW_GRAPH |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | buyers,admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_GRAPH'
```

### Related Settings

- [SHOW_ALLOCATION_CODES](SHOW_ALLOCATION_CODES.md)
- [SHOW_RULE_INFO](SHOW_RULE_INFO.md)

# ALLOWED_EXTENSIONS - iPurchase System Setting

**Category:** Uncategorized

This is a comma separated list of allowed or not-allowed file extensions which can be uploaded to iPurchase.

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
| **Setting Name** | ALLOWED_EXTENSIONS |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | !exe,!dll,!js*,!com,!bat,!lnk,!ws*,!scr,!msi,* |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOWED_EXTENSIONS'
```

### Related Settings

- [ALLOWED_DOMAINS](ALLOWED_DOMAINS.md)

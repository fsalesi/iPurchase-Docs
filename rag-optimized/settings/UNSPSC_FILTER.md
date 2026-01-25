# UNSPSC_FILTER - iPurchase System Setting

**Category:** Uncategorized

To modify this setting to control which UNSPSC codes are available to choose from.

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
| **Setting Name** | UNSPSC_FILTER |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UNSPSC_FILTER'
```
# SHOW_MARGIN - iPurchase System Setting

**Category:** Catalog & Vendors

Can-Do list. Users allowed to see profit margins.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

**Common patterns:**
- `*` - Everyone/all values allowed
- (blank) - No one/feature disabled
- `user1,user2` - Specific users only
- `group1,!user1` - Group members except specific user

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SHOW_MARGIN |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_MARGIN'
```
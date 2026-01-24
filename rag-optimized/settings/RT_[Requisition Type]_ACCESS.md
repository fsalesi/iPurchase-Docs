# RT_[Requisition Type]_ACCESS - iPurchase System Setting

**Category:** Requisitions

Comma separated list of User ID's or Group ID's that are allowed to create a requisition for the given requisition type. Asterisk indicates everyone, a blank indicates no one. All other users will not have access to this requisition type. The user will not be able to see those requisition types as choices in Requisition Maintenance. Furthermore, the requisition inquiry will not show any results for those types of requisitions, and any place requisition types are displayed will also be filtered based on this setting.

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
| **Setting Name** | RT_[Requisition Type]_ACCESS |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_ACCESS'
```
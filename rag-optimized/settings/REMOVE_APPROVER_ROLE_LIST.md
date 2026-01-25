# REMOVE_APPROVER_ROLE_LIST - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of User ID's or Group ID's that are allowed to remove an Approver from any requisition.

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
| **Setting Name** | REMOVE_APPROVER_ROLE_LIST |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_APPROVER_ROLE_LIST'
```

### Related Settings

- [REMOVE_APPROVER_FROM_GROUPS](REMOVE_APPROVER_FROM_GROUPS.md)
- [REMOVE_ORIGINATOR_FROM_GROUP_CO](REMOVE_ORIGINATOR_FROM_GROUP_CO.md)

# LOGIN_GOTO_MNT - iPurchase System Setting

**Category:** Security & Authentication

Comma separated list of User ID's or Group ID's that will always be logged into the requisition workbench. This only applies to non-approvers. Asterisk indicates everyone, a blank indicates no one.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

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
| **Setting Name** | LOGIN_GOTO_MNT |
| **Category** | Security & Authentication |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_GOTO_MNT'
```
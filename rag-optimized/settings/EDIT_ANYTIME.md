# EDIT_ANYTIME - iPurchase System Setting

**Category:** Uncategorized

Comma separated list of User ID's or Group ID's that are allowed to edit a Pending requisition at anytime. Asterisk indicates everyone, a blank indicates no one. There is currently a setting "ALWAYS_ALLOW_REQ_EDITS", which allows the defined users or groups the ability to modify a requisition while it is pending. By default, approvers are only allowed to change a requisition when its their turn to approve. Anyone listed here can modify a requisition at any time. You can also use a value of $xxreq_buyer to indicate that the given buyer on the requisition is allowed to edit anytime.

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
| **Setting Name** | EDIT_ANYTIME |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | buyers |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EDIT_ANYTIME'
```
# PO_UPDATE_GROUPS - iPurchase System Setting

**Category:** Purchase Orders

Comma separated list of User ID's or Group ID's that would be allowed to use the Copy or Update PO functionality (Change Order).  For buyer, set to "$xxreq_buyer".  Asterisk indicates everyone, a blank indicates no one.

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
| **Setting Name** | PO_UPDATE_GROUPS |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | $xxreq_buyer |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_GROUPS'
```
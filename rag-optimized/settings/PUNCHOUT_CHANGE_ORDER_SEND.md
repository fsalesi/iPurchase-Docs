# PUNCHOUT_CHANGE_ORDER_SEND - iPurchase System Setting

**Category:** Change Orders

Send PO revisions automatically to punchout suppliers via cXML. List of Vendor Numbers or * for all. CAN-DO functionality !staples,*

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
| **Setting Name** | PUNCHOUT_CHANGE_ORDER_SEND |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_CHANGE_ORDER_SEND'
```
# ALLOW_RETRANSMIT_PO - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that allow user to manually transmit cXML PO to Punchout supplier.

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
| **Setting Name** | ALLOW_RETRANSMIT_PO |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | buyers |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_RETRANSMIT_PO'
```

### Related Settings

- [ALLOW_BATCH_PO](ALLOW_BATCH_PO.md)
- [ALLOW_BLANKET_RELEASE](ALLOW_BLANKET_RELEASE.md)
- [ALLOW_BUG](ALLOW_BUG.md)

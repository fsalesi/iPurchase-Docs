# INQUIRY_AFTER_REJECT - iPurchase System Setting

**Category:** Reporting & Inquiry

Comma separated list of User ID's or Group ID's that are re-directed to the pending queue once they have rejected a requisition.

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
| **Setting Name** | INQUIRY_AFTER_REJECT |
| **Category** | Reporting & Inquiry |
| **Owner** | Power Users |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_AFTER_REJECT'
```

### Related Settings

- [INQUIRY_LAST_REV_DEFAULT](INQUIRY_LAST_REV_DEFAULT.md)
- [INQUIRY_NOTES_MATCHES](INQUIRY_NOTES_MATCHES.md)
- [INQUIRY_NO_NAME_SEARCH](INQUIRY_NO_NAME_SEARCH.md)

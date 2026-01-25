# RECEIPT_EMAIL_USERS - iPurchase System Setting

**Category:** Email Configuration

Can-Do list.

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
| **Setting Name** | RECEIPT_EMAIL_USERS |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RECEIPT_EMAIL_USERS'
```

### Related Settings

- [RECEIPT_EMAIL_MESSAGE](RECEIPT_EMAIL_MESSAGE.md)
- [RECEIPT_EMAIL_REQ_TYPES](RECEIPT_EMAIL_REQ_TYPES.md)
- [RECEIPT_EMAIL_SUBJECT](RECEIPT_EMAIL_SUBJECT.md)

# INQUIRY_SIMPLE_MODE - iPurchase System Setting

**Category:** Reporting & Inquiry

Comma separated list of User ID's or Group ID's who only gets to see "Views" on inquiry screen and does not see all the filter fields.

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
| **Setting Name** | INQUIRY_SIMPLE_MODE |
| **Category** | Reporting & Inquiry |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_SIMPLE_MODE'
```

### Related Settings

- [INQUIRY_AFTER_REJECT](INQUIRY_AFTER_REJECT.md)
- [INQUIRY_LAST_REV_DEFAULT](INQUIRY_LAST_REV_DEFAULT.md)
- [INQUIRY_NOTES_MATCHES](INQUIRY_NOTES_MATCHES.md)
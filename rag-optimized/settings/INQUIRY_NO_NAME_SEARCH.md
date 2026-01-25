# INQUIRY_NO_NAME_SEARCH - iPurchase System Setting

**Category:** Reporting & Inquiry

If this setting is set to true then when a user searches for a supplier they will not be allowed to search by name, only by supplier number.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures reporting & inquiry behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INQUIRY_NO_NAME_SEARCH |
| **Category** | Reporting & Inquiry |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_NO_NAME_SEARCH'
```

### Related Settings

- [INQUIRY_AFTER_REJECT](INQUIRY_AFTER_REJECT.md)
- [INQUIRY_LAST_REV_DEFAULT](INQUIRY_LAST_REV_DEFAULT.md)
- [INQUIRY_NOTES_MATCHES](INQUIRY_NOTES_MATCHES.md)

# NO_EMAILS - iPurchase System Setting

**Category:** Email Configuration

A value of True will turn off email functionality.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This email-related setting controls how iPurchase communicates with users via email notifications.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_EMAILS |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_EMAILS'
```

### Related Settings

- [NO_CHANGE_EMAIL](NO_CHANGE_EMAIL.md)
- [NO_EMAIL_REQ_BODY](NO_EMAIL_REQ_BODY.md)
- [NO_PO_EMAIL](NO_PO_EMAIL.md)

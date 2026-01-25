# NO_CHANGE_EMAIL - iPurchase System Setting

**Category:** Email Configuration

If an approver changes a requisition and this is set to true, then the originator will not be notified.

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
| **Setting Name** | NO_CHANGE_EMAIL |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_CHANGE_EMAIL'
```

### Related Settings

- [NO_EMAILS](NO_EMAILS.md)
- [NO_EMAIL_REQ_BODY](NO_EMAIL_REQ_BODY.md)
- [NO_PO_EMAIL](NO_PO_EMAIL.md)
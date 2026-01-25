# NO_EMAIL_REQ_BODY - iPurchase System Setting

**Category:** Email Configuration

Do not include the requisition print in emails.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting defines the email body content. You can use HTML formatting and dynamic tokens that are replaced with actual values when the email is sent.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_EMAIL_REQ_BODY |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_EMAIL_REQ_BODY'
```

### Related Settings

- [NO_CHANGE_EMAIL](NO_CHANGE_EMAIL.md)
- [NO_EMAILS](NO_EMAILS.md)
- [NO_PO_EMAIL](NO_PO_EMAIL.md)

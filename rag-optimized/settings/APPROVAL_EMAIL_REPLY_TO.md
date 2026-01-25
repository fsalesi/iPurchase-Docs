# APPROVAL_EMAIL_REPLY_TO - iPurchase System Setting

**Category:** Approval Workflow

Replies to approval email should go to who? Leave blank for originator.

### How It Works

Configure email recipients for this notification type. Multiple addresses can be comma-separated.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPROVAL_EMAIL_REPLY_TO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_EMAIL_REPLY_TO'
```

### Related Settings

- [APPROVAL_INCLUDE_FIELDS](APPROVAL_INCLUDE_FIELDS.md)
- [APPROVAL_METRICS_RED](APPROVAL_METRICS_RED.md)
- [APPROVAL_METRICS_YELLOW](APPROVAL_METRICS_YELLOW.md)

# EMAIL_REQ_BODY_MIN - iPurchase System Setting

**Category:** Email Configuration

When this is TRUE, only the supplier's number and name along with the cost of the requisition are embedded in the email.

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
| **Setting Name** | EMAIL_REQ_BODY_MIN |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_REQ_BODY_MIN'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)

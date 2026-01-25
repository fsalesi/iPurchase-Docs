# EMAIL_PO_TO_FINAL_APPROVER - iPurchase System Setting

**Category:** Email Configuration

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | sends PO creation notification to the final approver on the requisition |
| **FALSE** | Disables this feature |

### How It Works

Configure email recipients for this notification type. Multiple addresses can be comma-separated.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_TO_FINAL_APPROVER |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_TO_FINAL_APPROVER'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
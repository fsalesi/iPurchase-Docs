# EMAIL_NO_REJECT_LINK - iPurchase System Setting

**Category:** Email Configuration

Controls whether approval emails include a direct "Reject" link for one-click rejection.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Hide the reject link from approval emails |
| **FALSE** | Include the reject link in approval emails (DEFAULT) |

### How It Works

By default, approval notification emails include both "Approve" and "Reject" links for quick action. Some organizations prefer to hide the reject link to encourage approvers to log into the system and provide detailed rejection reasons rather than one-click rejections.

**When TRUE:**
- Approvers must log into iPurchase to reject
- Encourages more thoughtful rejections with comments
- Reject link removed from all approval emails

### Common Questions

- How do I remove the reject link from emails?
- Can approvers still reject requisitions?
- Why would I hide the reject link?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_NO_REJECT_LINK |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_NO_REJECT_LINK'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)

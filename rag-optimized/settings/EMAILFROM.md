# EMAILFROM - iPurchase System Setting

**Category:** Email Configuration

Specifies the email address used as the sender (From address) for all emails sent by iPurchase.

### How It Works

All outgoing emails from iPurchase - approval notifications, PO emails, system alerts - use this address as the From field. The address should be valid and monitored, as users may reply to these emails.

### Valid Values

| Value | Example |
|-------|---------|
| Valid email address | `ipurchase@company.com` |
| | `purchasing-noreply@company.com` |

### Requirements

- Must be a valid email format
- Should be an address that can receive replies (if reply functionality is desired)
- May need to be authorized in your email server's relay settings

### Common Questions

- What is EMAILFROM?
- How do I change the sender email address?
- What email address shows on notifications?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAILFROM |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAILFROM'
```

### Related Settings

- [EMAILSERVER](EMAILSERVER.md)
- [EMAILS_TO](EMAILS_TO.md)
- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)

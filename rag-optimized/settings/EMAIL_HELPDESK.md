# EMAIL_HELPDESK - iPurchase System Setting

**Category:** Email Configuration

Helpdesk email address displayed on the login screen and included in system emails for user support.

### How It Works

This email address appears in two key places:
1. **Login screen** - Users can contact support before logging in
2. **Email notifications** - Included via the $HELPDESK token in email templates

Configure this to your IT helpdesk or purchasing support team's email address.

### Valid Values

Valid email address string.

**Example:**
```
EMAIL_HELPDESK = "purchasing-support@company.com"
```

### Common Questions

- How do I add a support contact to the login page?
- What is the $HELPDESK token in emails?
- How do users contact support from iPurchase?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_HELPDESK |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_HELPDESK'
```

### Related Settings

- [EMAIL_HELP_TAG](EMAIL_HELP_TAG.md) - Help text included in emails
- [LOGIN_HIDE_EMAIL_HELPDESK](LOGIN_HIDE_EMAIL_HELPDESK.md) - Hide helpdesk on login

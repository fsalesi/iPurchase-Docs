# EMAILS_TO - iPurchase System Setting

**Category:** Email Configuration

Redirects all outgoing emails to specified addresses instead of the actual recipients. Used for testing and debugging.

### How It Works

When configured, ALL emails from iPurchase are sent to the address(es) specified here instead of the intended recipients. This is extremely useful for:
- **Testing:** Verify email content without spamming real users
- **Development:** Test email templates in non-production environments
- **Debugging:** Capture all emails to diagnose delivery issues

**⚠️ Warning:** When set, NO emails reach their intended recipients. All approval notifications, PO emails, and alerts go to this address instead.

**Example:**
- Normal: Approval email → john.approver@company.com
- With EMAILS_TO=admin@company.com: Approval email → admin@company.com

### Valid Values

Comma-separated email addresses, or blank to disable.

**Examples:**
- `admin@company.com` - Single redirect
- `admin@company.com,test@company.com` - Multiple recipients
- (blank) - Normal operation, emails go to intended recipients

### Common Questions

- How do I test emails without sending to real users?
- Why aren't users receiving emails?
- How do I capture all iPurchase emails for testing?
- Why are all emails going to the wrong address?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAILS_TO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAILS_TO'
```

### Related Settings

- [NO_EMAILS](NO_EMAILS.md) - Completely disable email sending
- [TEST_SYSTEM](TEST_SYSTEM.md) - Test mode indicator

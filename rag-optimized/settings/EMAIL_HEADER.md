# EMAIL_HEADER - iPurchase System Setting

**Category:** Email Configuration

Custom HTML header content included at the top of email templates for branding and styling.

### How It Works

This setting allows you to add consistent branding to all iPurchase emails. The HTML content is inserted at the top of email templates before the main message body.

**Common uses:**
- Company logo
- Branding colors and styling
- Standard header text or legal notices
- CSS styling for email formatting

**Example:**
```html
<div style="background:#003366; padding:10px; text-align:center;">
  <img src="https://company.com/logo.png" alt="Company Logo">
</div>
```

### Valid Values

HTML content string. Keep it simple - many email clients have limited HTML/CSS support.

### Common Questions

- How do I add a company logo to emails?
- Can I style iPurchase emails with CSS?
- How do I add branding to notification emails?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_HEADER |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_HEADER'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)

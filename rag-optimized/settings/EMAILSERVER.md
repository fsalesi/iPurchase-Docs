# EMAILSERVER - iPurchase System Setting

**Category:** Email Configuration

Specifies the SMTP server used by iPurchase to send all outgoing emails, including approval notifications, PO emails to suppliers, and system alerts.

### How It Works

iPurchase connects to this SMTP server to send all email communications. The server must be accessible from the iPurchase application server and configured to allow relay from that source.

### Valid Values

| Format | Example |
|--------|---------|
| IP Address | `192.168.1.100` |
| Hostname | `smtp.company.com` |
| With Port | `smtp.company.com:587` |
| IP with Port | `192.168.1.100:25` |

### Common Ports

- **25** - Standard SMTP (often blocked by ISPs)
- **587** - SMTP with STARTTLS (recommended)
- **465** - SMTP over SSL (legacy)

### Configuration Notes

- Ensure the SMTP server allows relay from the iPurchase server
- For cloud SMTP services (Office 365, Gmail, etc.), typically use port 587
- Test email delivery after configuration changes

### Common Questions

- What is EMAILSERVER?
- How do I configure email in iPurchase?
- Why are emails not being sent?
- How do I specify the SMTP port?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAILSERVER |
| **Category** | Email Configuration |
| **Owner** | IT |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAILSERVER'
```

### Related Settings

- [EMAILFROM](EMAILFROM.md) - Default sender email address
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md) - SMTP authentication username
- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md) - SMTP authentication password
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md) - Authentication method (PLAIN, LOGIN, etc.)

# EMAILSERVER - iPurchase System Setting

**Category:** Email Configuration

Specifies the SMTP server used by iPurchase to send all outgoing emails, including approval notifications, PO emails to suppliers, and system alerts.

### How It Works

iPurchase connects to this SMTP server to send all email communications. The server must be accessible from the iPurchase application server and configured to allow relay from that source.

### Valid Values

| Value | Description |
|-------|-------------|
| IP Address | Direct IP of SMTP server (e.g., "192.168.1.100") |
| Hostname | DNS name of SMTP server (e.g., "smtp.company.com") |

### Configuration Notes

- Ensure the SMTP server allows relay from the iPurchase server
- For cloud SMTP services (Office 365, Gmail, etc.), may require authentication settings
- Test email delivery after configuration changes

### Common Questions

- What is EMAILSERVER?
- How do I configure email in iPurchase?
- Why are emails not being sent?
- What SMTP server should I use?

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

- **EMAILFROM** - Default sender email address
- **EMAIL_AUTH_USER** - SMTP authentication username
- **EMAIL_AUTH_PASSWORD** - SMTP authentication password
- **EMAIL_AUTH_TYPE** - Authentication method (PLAIN, LOGIN, etc.)

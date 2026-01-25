# BASE_URL - iPurchase System Setting

**Category:** Email Configuration

Base URL/hostname used for generating links in email notifications and scheduled job communications.

### How It Works

This setting provides the base hostname for constructing URLs in outgoing emails. It works alongside APPLICATION_URL to ensure email links point to the correct server.

**Configuration:**
- Include protocol (https://)
- Use the externally accessible hostname
- Update when deploying to test/backup environments

**Example:**
```
BASE_URL = "https://server.company.com"
```

### Valid Values

Full base URL string with protocol.

### Common Questions

- What's the difference between BASE_URL and APPLICATION_URL?
- Why are my email links broken?
- How do I configure URLs for a test environment?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BASE_URL |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BASE_URL'
```

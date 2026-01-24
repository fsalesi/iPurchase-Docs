# ALLOWED_DOMAINS - iPurchase System Setting

**Category:** System Configuration

Defines which QAD domains (companies) are available in iPurchase. Users can only access domains listed here and in their user profile.

### How It Works

This setting defines the master list of domains available in the system. Individual users may be further restricted via their user profile (wus_domains field). A user can only access domains that appear in both this setting AND their profile.

### Valid Values

| Value | Example |
|-------|---------|
| Comma-separated domain codes | `QAD,DEMO,PROD` |
| Single domain | `QAD` |

### Common Questions

- What is ALLOWED_DOMAINS?
- How do I add a new domain to iPurchase?
- Why can't users see a specific domain?
- How do domain permissions work?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOWED_DOMAINS |
| **Category** | System Configuration |
| **Owner** | ISS |
| **Default Value** | QAD |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOWED_DOMAINS'
```

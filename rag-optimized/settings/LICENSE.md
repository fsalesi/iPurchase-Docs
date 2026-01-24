# LICENSE - iPurchase System Setting

**Category:** System Configuration

Software license key for the iPurchase application.

### How It Works

This setting contains the license key that enables iPurchase functionality. The license key:
- Validates your organization's right to use the software
- May control feature availability based on license tier
- Is provided by ISS during initial installation or renewal

**⚠️ Do not modify** this setting unless instructed by ISS. An invalid license key will prevent iPurchase from functioning.

### Valid Values

License key string provided by ISS.

### Common Questions

- Where do I find my iPurchase license key?
- How do I update my license key?
- What happens if my license expires?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LICENSE |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LICENSE'
```

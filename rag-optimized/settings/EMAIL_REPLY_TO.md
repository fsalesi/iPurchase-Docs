# EMAIL_REPLY_TO - iPurchase System Setting

**Category:** Email Configuration

Email address. Reply-to address used in system-generated emails. If blank, uses FROM address.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_REPLY_TO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_REPLY_TO'
```

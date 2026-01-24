# EMAIL_DEBUG_LEVEL - iPurchase System Setting

**Category:** Email Configuration

Numeric 0-3. Email system debug verbosity. 0=off, 1=basic, 2=detailed, 3=verbose. Used for troubleshooting email issues.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_DEBUG_LEVEL |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | 0 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_DEBUG_LEVEL'
```
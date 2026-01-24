# LOGIN_USE_AD_CMD - iPurchase System Setting

**Category:** Security & Authentication

Command for AD authentication validation.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_USE_AD_CMD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_USE_AD_CMD'
```

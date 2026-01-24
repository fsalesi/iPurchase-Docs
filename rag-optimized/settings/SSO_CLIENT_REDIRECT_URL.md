# SSO_CLIENT_REDIRECT_URL - iPurchase System Setting

**Category:** Security & Authentication

URL to redirect to after SSO authentication.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SSO_CLIENT_REDIRECT_URL |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SSO_CLIENT_REDIRECT_URL'
```
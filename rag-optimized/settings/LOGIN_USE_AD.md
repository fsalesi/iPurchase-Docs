# LOGIN_USE_AD - iPurchase System Setting

**Category:** Security & Authentication

Auto login user if using NTLM Active Directory security.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_USE_AD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_USE_AD'
```
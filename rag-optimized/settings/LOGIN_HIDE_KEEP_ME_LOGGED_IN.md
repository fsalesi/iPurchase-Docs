# LOGIN_HIDE_KEEP_ME_LOGGED_IN - iPurchase System Setting

**Category:** Security & Authentication

Hide the Keep me logged in link on the login screen

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_HIDE_KEEP_ME_LOGGED_IN |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_HIDE_KEEP_ME_LOGGED_IN'
```
# TEST_SETTINGS - iPurchase System Setting

**Category:** System Configuration

Comma-separated list of environment-specific settings that should be preserved when copying production database to dev/test. When production DB is copied down, these settings would be overwritten with prod values. Solution: On dev/test, these settings are exported to an XML dataset in the broker agent working directory. On agent startup (if TEST_SYSTEM env var is TRUE), the dataset is read and restores correct dev/test values. Default list includes: ALLOWED_DOMAINS, EMAILS_TO, SMS_TO, PO_PRINTER_OUTPUT_DIRECTORY, QAD_INTERFACE_USER, QAD_INTERFACE_PASSWORD, NO_QAD_AUTHENTICATION, LOGIN_USE_AD, LOGIN_USE_SSO, SSO_CHOICE, SSO_AUTHORIZATION_URL, SSO_CLIENT_ID, SSO_CLIENT_SECRET, SSO_LOGOFF_URL, SSO_TOKEN_URL, and AppSrvr Configuration records.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

### Valid Values

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone/all users |
| Blank/empty | No one/disabled |
| User/Group list | Only specified users/groups |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TEST_SETTINGS |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TEST_SETTINGS'
```

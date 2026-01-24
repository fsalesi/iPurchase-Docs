# IGNORE_PASSWORDS_ON_TEST - iPurchase System Setting

**Category:** Security & Authentication

TRUE | FALSE. When TRUE and the environment variable TEST_SYSTEM=TRUE, allows users to login with blank passwords. Used for dev/test environments to simplify testing without requiring password management. Only works when OS-level TEST_SYSTEM environment variable is also set to TRUE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IGNORE_PASSWORDS_ON_TEST |
| **Category** | Security & Authentication |
| **Owner** | IT |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IGNORE_PASSWORDS_ON_TEST'
```
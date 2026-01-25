# ALLOW_MULTIPLE_SESSIONS - iPurchase System Setting

**Category:** Security & Authentication

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | allows users to have multiple simultaneous login sessions |
| **FALSE** | Disables this feature |

### How It Works

This permission setting controls whether users can perform specific actions within the system.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_MULTIPLE_SESSIONS |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_MULTIPLE_SESSIONS'
```

### Related Settings

- [ALLOW_CHANGE_PASSWORD](ALLOW_CHANGE_PASSWORD.md)

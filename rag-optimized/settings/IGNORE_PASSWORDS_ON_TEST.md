# IGNORE_PASSWORDS_ON_TEST - iPurchase System Setting

**Category:** Security & Authentication

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This security setting affects user authentication and login behavior.

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

### Related Settings

- [IGNORE_IPADDR_SECURITY](IGNORE_IPADDR_SECURITY.md)

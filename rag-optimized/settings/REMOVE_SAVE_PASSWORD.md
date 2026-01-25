# REMOVE_SAVE_PASSWORD - iPurchase System Setting

**Category:** Security & Authentication

Removes the options of saving your password on the login screen.

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
| **Setting Name** | REMOVE_SAVE_PASSWORD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_SAVE_PASSWORD'
```
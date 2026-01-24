# REMOVE_SAVE_PASSWORD - iPurchase System Setting

**Category:** Security & Authentication

Removes the options of saving your password on the login screen. Users will need to enter their password every time.

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
| **Setting Name** | REMOVE_SAVE_PASSWORD |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_SAVE_PASSWORD'
```
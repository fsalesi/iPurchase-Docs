# ACCOUNT_SHOW_CUSTOMNOTE - iPurchase System Setting

**Category:** GL Accounts & Finance

Show the value CustomNote Field on the GL record - only for EE

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
| **Setting Name** | ACCOUNT_SHOW_CUSTOMNOTE |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_SHOW_CUSTOMNOTE'
```
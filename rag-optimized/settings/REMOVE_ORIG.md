# REMOVE_ORIG - iPurchase System Setting

**Category:** GL Accounts & Finance

This setting does not allow the originator to be an approver for their own requisitions if set to true.

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
| **Setting Name** | REMOVE_ORIG |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_ORIG'
```
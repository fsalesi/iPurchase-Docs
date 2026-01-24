# SUB_ACCOUNTS_USE_ORIG - iPurchase System Setting

**Category:** GL Accounts & Finance

TRUE | FALSE. If TRUE, uses originator's allowed sub-accounts instead of OBO's.

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
| **Setting Name** | SUB_ACCOUNTS_USE_ORIG |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUB_ACCOUNTS_USE_ORIG'
```
# TAX_USAGE_FIELD - iPurchase System Setting

**Category:** GL Accounts & Finance

[LEGACY/OBSOLETE] Field name for tax usage in data upgrades. Commented out in code.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TAX_USAGE_FIELD |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TAX_USAGE_FIELD'
```
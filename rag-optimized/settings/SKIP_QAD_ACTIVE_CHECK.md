# SKIP_QAD_ACTIVE_CHECK - iPurchase System Setting

**Category:** QAD Integration

True or False Do not check the QAD user's active flag.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures qad integration behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SKIP_QAD_ACTIVE_CHECK |
| **Category** | QAD Integration |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SKIP_QAD_ACTIVE_CHECK'
```

### Related Settings

- [SKIP_QAD_DOMAIN_CHECK](SKIP_QAD_DOMAIN_CHECK.md)

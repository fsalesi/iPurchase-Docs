# SKIP_QAD_DOMAIN_CHECK - iPurchase System Setting

**Category:** QAD Integration

TRUE | FALSE.

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
| **Setting Name** | SKIP_QAD_DOMAIN_CHECK |
| **Category** | QAD Integration |
| **Owner** | ISS |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SKIP_QAD_DOMAIN_CHECK'
```

### Related Settings

- [SKIP_QAD_ACTIVE_CHECK](SKIP_QAD_ACTIVE_CHECK.md)
# SKIP_QAD_DOMAIN_CHECK - iPurchase System Setting

**Category:** QAD Integration

TRUE | FALSE. Skip domain validation in QAD integration.

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
| **Setting Name** | SKIP_QAD_DOMAIN_CHECK |
| **Category** | QAD Integration |
| **Owner** | ISS |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SKIP_QAD_DOMAIN_CHECK'
```
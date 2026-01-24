# DEFAULT_CURRENCY - iPurchase System Setting

**Category:** System Configuration

The administrator can set a default currency for iPurchase.  Must be a valid currency.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_CURRENCY |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_CURRENCY'
```
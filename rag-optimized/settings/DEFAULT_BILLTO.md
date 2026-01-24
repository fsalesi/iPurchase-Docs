# DEFAULT_BILLTO - iPurchase System Setting

**Category:** System Configuration

The administrator can enter a default value for the "Bill To" field.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_BILLTO |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_BILLTO'
```

# DEFAULT_FREIGHTTERMS - iPurchase System Setting

**Category:** System Configuration

Administrator can set the default value for "Who's Paying Freight" field.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_FREIGHTTERMS |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_FREIGHTTERMS'
```

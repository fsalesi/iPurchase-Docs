# DEFAULT_CC - iPurchase System Setting

**Category:** System Configuration

Administrator can set the default Cost Center or Departments for Punchouts and Catalog orders.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_CC |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_CC'
```

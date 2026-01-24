# NO_EMAILS - iPurchase System Setting

**Category:** Email Configuration

A value of True will turn off email functionality. A value of False will turn on email functionality.

### How It Works

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Enabled |
| `FALSE` | Disabled |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_EMAILS |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_EMAILS'
```

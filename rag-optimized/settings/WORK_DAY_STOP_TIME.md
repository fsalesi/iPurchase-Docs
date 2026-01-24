# WORK_DAY_STOP_TIME - iPurchase System Setting

**Category:** System Configuration

Time (HH:MM). End of business day for escalations/notifications.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | WORK_DAY_STOP_TIME |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | 17:00 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'WORK_DAY_STOP_TIME'
```

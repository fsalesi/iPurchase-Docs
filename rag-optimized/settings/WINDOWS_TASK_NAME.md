# WINDOWS_TASK_NAME - iPurchase System Setting

**Category:** System Configuration

Windows Task Scheduler task name for iPurchase scheduled jobs.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | WINDOWS_TASK_NAME |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'WINDOWS_TASK_NAME'
```

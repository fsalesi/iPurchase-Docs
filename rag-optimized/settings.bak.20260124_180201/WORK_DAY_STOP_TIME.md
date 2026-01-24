# WORK_DAY_STOP_TIME - iPurchase System Setting

**Category:** System Configuration

Time (HH:MM). End of business day for escalations/notifications.

**Common questions this answers:**
- What is WORK_DAY_STOP_TIME?
- What does WORK_DAY_STOP_TIME do?
- What is the default value for WORK_DAY_STOP_TIME?
- How do I configure WORK_DAY_STOP_TIME?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | WORK_DAY_STOP_TIME |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | 17:00 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'WORK_DAY_STOP_TIME'
```

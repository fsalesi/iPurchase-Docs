# WORK_DAY_STOP_TIME - iPurchase System Setting

**Category:** System Configuration

Defines the end of the business day for escalation calculations and notification timing.

### How It Works

iPurchase uses business hours to calculate escalation timing and schedule notifications appropriately. This setting defines when the work day ends.

**Used for:**
- Escalation time calculations (e.g., "escalate after 2 business days")
- Notification scheduling (avoid sending emails outside business hours)
- SLA compliance tracking
- Approval aging calculations

**Example:**
If WORK_DAY_START_TIME = "08:00" and WORK_DAY_STOP_TIME = "17:00":
- Business day = 9 hours of working time
- Notifications after 5 PM may be held until next business day
- Weekend hours don't count toward escalation timers

### Valid Values

Time in HH:MM format (24-hour).

**Examples:**
- `17:00` - 5:00 PM (default)
- `18:00` - 6:00 PM
- `16:30` - 4:30 PM

### Common Questions

- How does iPurchase calculate escalation timing?
- When does the business day end for approvals?
- How do I configure business hours?

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

### Related Settings

- [WORK_DAY_START_TIME](WORK_DAY_START_TIME.md) - Start of business day
- [WINDOWS_TASK_NAME](WINDOWS_TASK_NAME.md) - Scheduled job configuration

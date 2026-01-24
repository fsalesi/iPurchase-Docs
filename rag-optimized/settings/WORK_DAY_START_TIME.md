# WORK_DAY_START_TIME - iPurchase System Setting

**Category:** System Configuration

Defines the start of the business day for escalation calculations and notification timing.

### How It Works

iPurchase uses business hours to calculate escalation timing and schedule notifications appropriately. This setting defines when the work day begins.

**Used for:**
- Escalation time calculations (e.g., "escalate after 2 business days")
- Notification scheduling (avoid sending emails outside business hours)
- SLA compliance tracking
- Approval aging calculations

**Example:**
If WORK_DAY_START_TIME = "08:00" and WORK_DAY_STOP_TIME = "17:00":
- A requisition submitted at 6:00 PM Monday starts aging at 8:00 AM Tuesday
- Escalation timers only count hours between 8 AM and 5 PM
- A "24 business hour" escalation = 3 calendar days (8 hours/day)

### Valid Values

Time in HH:MM format (24-hour).

**Examples:**
- `08:00` - 8:00 AM (default)
- `09:00` - 9:00 AM
- `07:30` - 7:30 AM

### Common Questions

- How does iPurchase calculate escalation timing?
- When does the business day start for approvals?
- How do I change business hours in iPurchase?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | WORK_DAY_START_TIME |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | 08:00 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'WORK_DAY_START_TIME'
```

### Related Settings

- [WORK_DAY_STOP_TIME](WORK_DAY_STOP_TIME.md) - End of business day
- [WINDOWS_TASK_NAME](WINDOWS_TASK_NAME.md) - Scheduled job configuration

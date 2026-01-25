# WINDOWS_TASK_NAME - iPurchase System Setting

**Category:** System Configuration

Specifies the Windows Task Scheduler task name used for iPurchase scheduled jobs.

### How It Works

iPurchase uses Windows Task Scheduler to run background jobs such as:
- Email queue processing
- PO creation batches
- Escalation notifications
- Data synchronization

This setting stores the name of the scheduled task so iPurchase can monitor and manage it.

**Typical setup:**
1. Windows Task Scheduler runs the iPurchase job processor on a schedule
2. This setting stores the task name for reference
3. iPurchase can check task status and trigger runs

### Valid Values

Windows Task Scheduler task name string.

**Example:**
```sql
WINDOWS_TASK_NAME = "iPurchase_JobProcessor"
```

### Common Questions

- What scheduled task does iPurchase use?
- How do I configure iPurchase background jobs?
- Where do I find the Windows Task Scheduler task for iPurchase?

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

# JOB_RETRY_EMAIL_LAST - iPurchase System Setting

**Category:** System Configuration

Controls whether failure notification emails are sent on every retry attempt or only on the final retry.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Send failure email only on the final retry attempt |
| **FALSE** | Send failure email on every retry attempt (DEFAULT) |

### How It Works

When scheduled jobs fail (email delivery, PO creation, etc.), iPurchase retries them automatically. This setting controls the notification behavior:

**FALSE (Default):**
- Admin gets email notification on EVERY failure
- Results in multiple emails if job fails repeatedly
- Better for urgent monitoring - immediate awareness of issues

**TRUE:**
- Admin gets email notification only on the FINAL retry
- Single notification after all retry attempts exhausted
- Better for reducing email noise on transient failures

**Example:**
Job fails 3 times before succeeding:
- FALSE: 3 failure emails sent
- TRUE: 0 failure emails sent (job eventually succeeded)

Job fails 3 times, max retries reached:
- FALSE: 3 failure emails sent
- TRUE: 1 failure email sent (on final attempt)

### Common Questions

- Why am I getting so many job failure emails?
- How do I reduce notification noise from retries?
- When should I get notified about job failures?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | JOB_RETRY_EMAIL_LAST |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'JOB_RETRY_EMAIL_LAST'
```

### Related Settings

- [EMAIL_PURGE_DAYS](EMAIL_PURGE_DAYS.md) - How long to keep failed email records

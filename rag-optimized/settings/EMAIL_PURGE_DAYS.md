# EMAIL_PURGE_DAYS - iPurchase System Setting

**Category:** Email Configuration

Controls how long failed email records are retained before being automatically purged from the system.

### How It Works

iPurchase maintains a queue of outgoing emails. When emails fail to send (due to server issues, invalid addresses, etc.), they remain in the queue for retry. This setting determines how many days those failed email records are kept before automatic deletion.

**Purge Process:**
1. Email fails to send → marked as error in queue
2. System retries based on retry settings
3. After EMAIL_PURGE_DAYS, failed records are deleted
4. Purge runs as part of scheduled maintenance jobs

**Considerations:**
- Higher values = more storage used, longer audit trail
- Lower values = cleaner queue, but less time to diagnose issues
- Set high enough to allow investigation of persistent failures

### Valid Values

Integer representing number of days. Default is **30**.

### Common Questions

- How long are failed emails kept in iPurchase?
- How do I clean up the email queue?
- Why is my email queue so large?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PURGE_DAYS |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | 30 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PURGE_DAYS'
```

### Related Settings

- [JOB_RETRY_EMAIL_LAST](JOB_RETRY_EMAIL_LAST.md) - Controls retry notification behavior
- [NO_EMAILS](NO_EMAILS.md) - Disable all email sending

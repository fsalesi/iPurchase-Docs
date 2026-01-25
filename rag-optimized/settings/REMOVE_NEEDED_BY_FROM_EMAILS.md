# REMOVE_NEEDED_BY_FROM_EMAILS - iPurchase System Setting

**Category:** Email Configuration

Show 'Needed By 99/99/9999' in the approval email subject.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This email-related setting controls how iPurchase communicates with users via email notifications.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_NEEDED_BY_FROM_EMAILS |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_NEEDED_BY_FROM_EMAILS'
```
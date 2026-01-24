# EMAIL_HELP_TAG - iPurchase System Setting

**Category:** Email Configuration

Include -- If questions, email the helpdesk link on all internal emails."

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_HELP_TAG |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | If questions, email the $HELPDESK, or contact the originator, or approver. |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_HELP_TAG'
```
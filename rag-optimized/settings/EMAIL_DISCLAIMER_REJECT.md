# EMAIL_DISCLAIMER_REJECT - iPurchase System Setting

**Category:** Email Configuration

If questions, please contact the approver that rejected the requisition

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_DISCLAIMER_REJECT |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | If questions, please contact the approver that rejected the requisition |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_DISCLAIMER_REJECT'
```
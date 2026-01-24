# IA_EMAIL_SUBJECT_APPEND - iPurchase System Setting

**Category:** iApprove Integration

Text appended to all iApprove email subject lines. Used for environment identification (e.g., [TEST]).

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IA_EMAIL_SUBJECT_APPEND |
| **Category** | iApprove Integration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IA_EMAIL_SUBJECT_APPEND'
```

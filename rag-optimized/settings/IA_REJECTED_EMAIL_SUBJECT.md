# IA_REJECTED_EMAIL_SUBJECT - iPurchase System Setting

**Category:** iApprove Integration

Email subject line when iApprove document is rejected.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IA_REJECTED_EMAIL_SUBJECT |
| **Category** | iApprove Integration |
| **Owner** | Admin |
| **Default Value** | Rejected |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IA_REJECTED_EMAIL_SUBJECT'
```

# COPY_ATTACHMENTS - iPurchase System Setting

**Category:** ACH Integration

This setting indicates whether or not attachments are copied when a requisition is copied

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | COPY_ATTACHMENTS |
| **Category** | ACH Integration |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'COPY_ATTACHMENTS'
```

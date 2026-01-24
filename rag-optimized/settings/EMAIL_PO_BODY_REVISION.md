# EMAIL_PO_BODY_REVISION - iPurchase System Setting

**Category:** Email Configuration

Allows the administrator to create a custom email body for PO revision emails.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_BODY_REVISION |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_BODY_REVISION'
```
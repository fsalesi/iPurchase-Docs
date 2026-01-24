# APPROVAL_EMAIL_REPLY_TO - iPurchase System Setting

**Category:** Approval Workflow

Replies to approval email should go to who? Leave blank for originator. Set to 'OBO' for On behalf of. Set to any single email address.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APPROVAL_EMAIL_REPLY_TO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APPROVAL_EMAIL_REPLY_TO'
```

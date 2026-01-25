# EMAIL_SUPPLIER_PO_SUBJECT_REVISION - iPurchase System Setting

**Category:** Email Configuration

This text will be used as the subject of the email going to the supplier.

### How It Works

This setting customizes the subject line for outgoing emails. Choose text that clearly identifies the email purpose to improve open rates and avoid spam filters.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO_SUBJECT_REVISION |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | Purchase Order Revision - $NBR |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO_SUBJECT_REVISION'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)
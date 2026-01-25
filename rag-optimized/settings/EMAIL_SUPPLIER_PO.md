# EMAIL_SUPPLIER_PO - iPurchase System Setting

**Category:** Email Configuration

Controls whether purchase order emails are automatically sent to suppliers when a requisition is fully approved and converted to a PO.

### How It Works

When a requisition completes the approval process and a PO is created, this setting determines whether an email containing the PO is automatically sent to the supplier's email address on file.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Automatically email PO to supplier (DEFAULT) |
| `FALSE` | Do not auto-email - manual send required |

### Requirements

For supplier email to work:
- Supplier must have an email address configured
- EMAILSERVER must be properly configured
- Supplier email address must be valid

### Common Questions

- What is EMAIL_SUPPLIER_PO?
- How do I enable automatic PO emails to suppliers?
- Why isn't the supplier receiving PO emails?
- Can I manually send PO emails?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO'
```

### Related Settings

- [EMAIL_AUTH_PASSWORD](EMAIL_AUTH_PASSWORD.md)
- [EMAIL_AUTH_TYPE](EMAIL_AUTH_TYPE.md)
- [EMAIL_AUTH_USER](EMAIL_AUTH_USER.md)

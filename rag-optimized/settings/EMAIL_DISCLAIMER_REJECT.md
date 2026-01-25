# EMAIL_DISCLAIMER_REJECT - iPurchase System Setting

**Category:** Email Configuration

Custom text displayed in rejection notification emails, typically providing guidance on next steps after a requisition is rejected.

### How It Works

When a requisition is rejected, the rejection email includes this disclaimer text. Use it to provide helpful guidance to users about what to do next.

**Default text:**
```
If questions, please contact the approver that rejected the requisition
```

**Customization options:**
- Include contact information for purchasing support
- Add instructions for resubmission
- Reference company policies on rejections

### Valid Values

Text string or HTML content for the rejection email disclaimer.

### Common Questions

- How do I customize the rejection email message?
- Can I include HTML in the rejection disclaimer?
- How do I add support contact information to rejection emails?

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

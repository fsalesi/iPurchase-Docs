# COPY_ATTACHMENTS - iPurchase System Setting

**Category:** ACH Integration

This setting indicates whether or not attachments are copied when a requisition is copied

**Common questions this answers:**
- What is COPY_ATTACHMENTS?
- What does COPY_ATTACHMENTS do?
- What is the default value for COPY_ATTACHMENTS?
- How do I configure COPY_ATTACHMENTS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | COPY_ATTACHMENTS |
| **Category** | ACH Integration |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'COPY_ATTACHMENTS'
```

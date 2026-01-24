# EMAIL_DISCLAIMER_REJECT - iPurchase System Setting

**Category:** Email Configuration

If questions, please contact the approver that rejected the requisition

**Common questions this answers:**
- What is EMAIL_DISCLAIMER_REJECT?
- What does EMAIL_DISCLAIMER_REJECT do?
- What is the default value for EMAIL_DISCLAIMER_REJECT?
- How do I configure EMAIL_DISCLAIMER_REJECT?
- How does EMAIL_DISCLAIMER_REJECT affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_DISCLAIMER_REJECT |
| **Category** | Email Configuration |
| **Owner** |  |
| **Default Value** | If questions, please contact the approver that rejected the requisition |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_DISCLAIMER_REJECT'
```

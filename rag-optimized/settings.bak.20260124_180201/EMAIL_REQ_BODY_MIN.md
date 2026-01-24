# EMAIL_REQ_BODY_MIN - iPurchase System Setting

**Category:** Email Configuration

When this is TRUE, only the supplier's number and name along with the cost of the requisition are embedded in the email. If the requisition is a change order, then the words "Change Order" will als...

**Common questions this answers:**
- What is EMAIL_REQ_BODY_MIN?
- What does EMAIL_REQ_BODY_MIN do?
- What is the default value for EMAIL_REQ_BODY_MIN?
- How do I configure EMAIL_REQ_BODY_MIN?
- How does EMAIL_REQ_BODY_MIN affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_REQ_BODY_MIN |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_REQ_BODY_MIN'
```

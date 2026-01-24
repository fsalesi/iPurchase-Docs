# NO_EMAIL_REQ_BODY - iPurchase System Setting

**Category:** Email Configuration

Do not include the requisition print in emails. Only includes the text.

**Common questions this answers:**
- What is NO_EMAIL_REQ_BODY?
- What does NO_EMAIL_REQ_BODY do?
- What is the default value for NO_EMAIL_REQ_BODY?
- How do I configure NO_EMAIL_REQ_BODY?
- How does NO_EMAIL_REQ_BODY affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_EMAIL_REQ_BODY |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_EMAIL_REQ_BODY'
```

# EMAIL_PO_INCLUDE_SIG - iPurchase System Setting

**Category:** Email Configuration

This setting includes the buyer's contact information for emails automatically sent to suppliers when PO is created. It also includes logged in user's contact information in emails which are manual...

**Common questions this answers:**
- What is EMAIL_PO_INCLUDE_SIG?
- What does EMAIL_PO_INCLUDE_SIG do?
- What is the default value for EMAIL_PO_INCLUDE_SIG?
- How do I configure EMAIL_PO_INCLUDE_SIG?
- How does EMAIL_PO_INCLUDE_SIG affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_PO_INCLUDE_SIG |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_INCLUDE_SIG'
```

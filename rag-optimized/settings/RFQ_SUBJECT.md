# RFQ_SUBJECT - iPurchase System Setting

**Category:** RFQ Management

Email subject for RFQ emails.

**Common questions this answers:**
- What is RFQ_SUBJECT?
- What does RFQ_SUBJECT do?
- What is the default value for RFQ_SUBJECT?
- How do I configure RFQ_SUBJECT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RFQ_SUBJECT |
| **Category** | RFQ Management |
| **Owner** | Purchasing |
| **Default Value** | Request for Quote |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RFQ_SUBJECT'
```

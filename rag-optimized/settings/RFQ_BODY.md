# RFQ_BODY - iPurchase System Setting

**Category:** RFQ Management

Email body template for RFQ emails.

**Common questions this answers:**
- What is RFQ_BODY?
- What does RFQ_BODY do?
- What is the default value for RFQ_BODY?
- How do I configure RFQ_BODY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RFQ_BODY |
| **Category** | RFQ Management |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RFQ_BODY'
```

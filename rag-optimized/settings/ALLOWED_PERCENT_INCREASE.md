# ALLOWED_PERCENT_INCREASE - iPurchase System Setting

**Category:** Approval Workflow

Specify the amount that an approver can increase the requisition by without having it re-routed. If the requisition amount is increased greater than the value specified here, then the requisition w...

**Common questions this answers:**
- What is ALLOWED_PERCENT_INCREASE?
- What does ALLOWED_PERCENT_INCREASE do?
- What is the default value for ALLOWED_PERCENT_INCREASE?
- How do I configure ALLOWED_PERCENT_INCREASE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOWED_PERCENT_INCREASE |
| **Category** | Approval Workflow |
| **Owner** | Finance |
| **Default Value** | 10 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOWED_PERCENT_INCREASE'
```

**Related settings:** ALLOWED_DOLLAR_INCREASE, CO_TOLERANCE_PERCENT
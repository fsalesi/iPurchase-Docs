# REQ_INQ_HIDDEN_ELEMENTS - iPurchase System Setting

**Category:** Requisitions

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is REQ_INQ_HIDDEN_ELEMENTS?
- What does REQ_INQ_HIDDEN_ELEMENTS do?
- What is the default value for REQ_INQ_HIDDEN_ELEMENTS?
- How do I configure REQ_INQ_HIDDEN_ELEMENTS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQ_INQ_HIDDEN_ELEMENTS |
| **Category** | Requisitions |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQ_INQ_HIDDEN_ELEMENTS'
```

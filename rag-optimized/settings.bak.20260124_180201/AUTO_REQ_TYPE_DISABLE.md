# AUTO_REQ_TYPE_DISABLE - iPurchase System Setting

**Category:** Requisitions

Disable the requisition type field when there is at least one line item on a requisition - DO NOT MODIFY

**Common questions this answers:**
- What is AUTO_REQ_TYPE_DISABLE?
- What does AUTO_REQ_TYPE_DISABLE do?
- What is the default value for AUTO_REQ_TYPE_DISABLE?
- How do I configure AUTO_REQ_TYPE_DISABLE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_REQ_TYPE_DISABLE |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_REQ_TYPE_DISABLE'
```

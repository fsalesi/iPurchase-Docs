# REQ_INQUIRY_FIELDS - iPurchase System Setting

**Category:** Requisitions

Comma separated list of fields that will be shown as columns in requisition inquiry.

**Common questions this answers:**
- What is REQ_INQUIRY_FIELDS?
- What does REQ_INQUIRY_FIELDS do?
- What is the default value for REQ_INQUIRY_FIELDS?
- How do I configure REQ_INQUIRY_FIELDS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQ_INQUIRY_FIELDS |
| **Category** | Requisitions |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQ_INQUIRY_FIELDS'
```

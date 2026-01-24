# PUNCHOUT_REQ_TYPE - iPurchase System Setting

**Category:** Catalog & Vendors

This setting allows the administrator to globally set a default requisition type for punchout requisitions.

**Common questions this answers:**
- What is PUNCHOUT_REQ_TYPE?
- What does PUNCHOUT_REQ_TYPE do?
- What is the default value for PUNCHOUT_REQ_TYPE?
- How do I configure PUNCHOUT_REQ_TYPE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_REQ_TYPE |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_REQ_TYPE'
```

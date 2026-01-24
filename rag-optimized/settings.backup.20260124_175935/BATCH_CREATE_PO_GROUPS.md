# BATCH_CREATE_PO_GROUPS - iPurchase System Setting

**Category:** Purchase Orders

Comma Separated list of User ID's or Group ID's that can convert an approved requisition into a PO (only when PO is not created automatically upon final approval) Thios setting also controls if a u...

**Common questions this answers:**
- What is BATCH_CREATE_PO_GROUPS?
- What does BATCH_CREATE_PO_GROUPS do?
- What is the default value for BATCH_CREATE_PO_GROUPS?
- How do I configure BATCH_CREATE_PO_GROUPS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BATCH_CREATE_PO_GROUPS |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | buyers |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BATCH_CREATE_PO_GROUPS'
```

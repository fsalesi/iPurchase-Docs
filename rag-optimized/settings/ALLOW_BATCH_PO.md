# ALLOW_BATCH_PO - iPurchase System Setting

**Category:** User Management

This setting allows the administrator to set how the PO will be created in iPurchase. The options for this setting are: 1) FALSE - Default is set to create PO now. The last approver will still have...

**Common questions this answers:**
- What is ALLOW_BATCH_PO?
- What does ALLOW_BATCH_PO do?
- What is the default value for ALLOW_BATCH_PO?
- How do I configure ALLOW_BATCH_PO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_BATCH_PO |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | FALSE-ALWAYS |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_BATCH_PO'
```

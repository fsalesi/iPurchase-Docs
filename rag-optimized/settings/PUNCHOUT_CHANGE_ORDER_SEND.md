# PUNCHOUT_CHANGE_ORDER_SEND - iPurchase System Setting

**Category:** Change Orders

Send PO revisions automatically to punchout suppliers via cXML. List of Vendor Numbers or * for all. CAN-DO functionality !staples,*

**Common questions this answers:**
- What is PUNCHOUT_CHANGE_ORDER_SEND?
- What does PUNCHOUT_CHANGE_ORDER_SEND do?
- What is the default value for PUNCHOUT_CHANGE_ORDER_SEND?
- How do I configure PUNCHOUT_CHANGE_ORDER_SEND?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_CHANGE_ORDER_SEND |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_CHANGE_ORDER_SEND'
```

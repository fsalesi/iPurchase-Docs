# PO_UPDATE_CHECK_REROUTE - iPurchase System Setting

**Category:** Change Orders

As part of the approval process, do you want the system to compare the approvers from the original requisition to the new requisition? If there are any changes then the new requisition will be re-r...

**Common questions this answers:**
- What is PO_UPDATE_CHECK_REROUTE?
- What does PO_UPDATE_CHECK_REROUTE do?
- What is the default value for PO_UPDATE_CHECK_REROUTE?
- How do I configure PO_UPDATE_CHECK_REROUTE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_UPDATE_CHECK_REROUTE |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_CHECK_REROUTE'
```

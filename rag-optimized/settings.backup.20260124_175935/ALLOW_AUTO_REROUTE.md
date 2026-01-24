# ALLOW_AUTO_REROUTE - iPurchase System Setting

**Category:** Change Orders

If an approver makes a change to a requisition, iPurchase will re-check who the approvers should be in order for the changes made. If the new approver set is different from the current approver set...

**Common questions this answers:**
- What is ALLOW_AUTO_REROUTE?
- What does ALLOW_AUTO_REROUTE do?
- What is the default value for ALLOW_AUTO_REROUTE?
- How do I configure ALLOW_AUTO_REROUTE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_AUTO_REROUTE |
| **Category** | Change Orders |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_AUTO_REROUTE'
```

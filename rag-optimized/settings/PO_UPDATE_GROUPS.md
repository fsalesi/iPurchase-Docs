# PO_UPDATE_GROUPS - iPurchase System Setting

**Category:** Purchase Orders

Comma separated list of User ID's or Group ID's that would be allowed to use the Copy or Update PO functionality (Change Order).  For buyer, set to "$xxreq_buyer".  Asterisk indicates everyone, a b...

**Common questions this answers:**
- What is PO_UPDATE_GROUPS?
- What does PO_UPDATE_GROUPS do?
- What is the default value for PO_UPDATE_GROUPS?
- How do I configure PO_UPDATE_GROUPS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_UPDATE_GROUPS |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | $xxreq_buyer |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_UPDATE_GROUPS'
```

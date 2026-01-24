# USE_CHAINED_DELEGATES - iPurchase System Setting

**Category:** Uncategorized

This setting will allow for unlimited levels of Out Of Office functionality. If user A delegates to user B, then user B also delegates to user C, can User C approve or reject a requisition on behal...

**Common questions this answers:**
- What is USE_CHAINED_DELEGATES?
- What does USE_CHAINED_DELEGATES do?
- What is the default value for USE_CHAINED_DELEGATES?
- How do I configure USE_CHAINED_DELEGATES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_CHAINED_DELEGATES |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_CHAINED_DELEGATES'
```

**Related settings:** OOF_LIMIT_TO_APPROVERS, ALLOW_SUPERVISORS_TO_APPROVE
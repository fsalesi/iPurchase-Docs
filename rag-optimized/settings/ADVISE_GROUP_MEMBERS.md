# ADVISE_GROUP_MEMBERS - iPurchase System Setting

**Category:** Uncategorized

This setting will send out emails to other users in a group when one of the group members approves a requisition when set to true.

**Common questions this answers:**
- What is ADVISE_GROUP_MEMBERS?
- What does ADVISE_GROUP_MEMBERS do?
- What is the default value for ADVISE_GROUP_MEMBERS?
- How do I configure ADVISE_GROUP_MEMBERS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ADVISE_GROUP_MEMBERS |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ADVISE_GROUP_MEMBERS'
```

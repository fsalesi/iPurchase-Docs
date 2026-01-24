# REMOVE_ORIG_RELEASE - iPurchase System Setting

**Category:** Uncategorized

If set to true, this setting will remove the originator from the approver list on blanket release requisitions.

**Common questions this answers:**
- What is REMOVE_ORIG_RELEASE?
- What does REMOVE_ORIG_RELEASE do?
- What is the default value for REMOVE_ORIG_RELEASE?
- How do I configure REMOVE_ORIG_RELEASE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_ORIG_RELEASE |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_ORIG_RELEASE'
```

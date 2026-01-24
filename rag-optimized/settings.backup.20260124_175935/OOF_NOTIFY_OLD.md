# OOF_NOTIFY_OLD - iPurchase System Setting

**Category:** Uncategorized

A setting of TRUE will email any existing pending requisitions to the newly assigned delegate. If the setting is FALSE, the delegate will not receive an email for any existing pending requisitions....

**Common questions this answers:**
- What is OOF_NOTIFY_OLD?
- What does OOF_NOTIFY_OLD do?
- What is the default value for OOF_NOTIFY_OLD?
- How do I configure OOF_NOTIFY_OLD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | OOF_NOTIFY_OLD |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'OOF_NOTIFY_OLD'
```

# MESSAGE_ERROR_TIMEOUT - iPurchase System Setting

**Category:** Uncategorized

This setting allows the administrator the ability to set the duration of how long the error message will stay on the screen. A value of 0 will indicate to keep the message on the screen indefinitel...

**Common questions this answers:**
- What is MESSAGE_ERROR_TIMEOUT?
- What does MESSAGE_ERROR_TIMEOUT do?
- What is the default value for MESSAGE_ERROR_TIMEOUT?
- How do I configure MESSAGE_ERROR_TIMEOUT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MESSAGE_ERROR_TIMEOUT |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | 0 |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MESSAGE_ERROR_TIMEOUT'
```

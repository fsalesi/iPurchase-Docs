# AUTO_RECEIVE_TIME - iPurchase System Setting

**Category:** Receiving

Time value. Timestamp used when AUTO_RECEIVE creates automatic receipt records. Must be configured correctly when AUTO_RECEIVE is enabled.

**Common questions this answers:**
- What is AUTO_RECEIVE_TIME?
- What does AUTO_RECEIVE_TIME do?
- What is the default value for AUTO_RECEIVE_TIME?
- How do I configure AUTO_RECEIVE_TIME?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_RECEIVE_TIME |
| **Category** | Receiving |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_RECEIVE_TIME'
```

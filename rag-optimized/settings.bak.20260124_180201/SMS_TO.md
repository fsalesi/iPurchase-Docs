# SMS_TO - iPurchase System Setting

**Category:** System Configuration

Phone numbers for SMS notifications.

**Common questions this answers:**
- What is SMS_TO?
- What does SMS_TO do?
- What is the default value for SMS_TO?
- How do I configure SMS_TO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SMS_TO |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SMS_TO'
```

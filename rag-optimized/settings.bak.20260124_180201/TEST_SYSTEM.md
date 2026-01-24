# TEST_SYSTEM - iPurchase System Setting

**Category:** System Configuration

⚠️ DEPRECATED - Use OS environment variable TEST_SYSTEM instead. This setting is no longer used. Set TEST_SYSTEM=TRUE as an environment variable on the broker/PASOE instance for dev/test environments.

**Common questions this answers:**
- What is TEST_SYSTEM?
- What does TEST_SYSTEM do?
- What is the default value for TEST_SYSTEM?
- How do I configure TEST_SYSTEM?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TEST_SYSTEM |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TEST_SYSTEM'
```

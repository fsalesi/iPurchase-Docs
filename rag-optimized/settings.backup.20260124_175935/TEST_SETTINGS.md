# TEST_SETTINGS - iPurchase System Setting

**Category:** System Configuration

Comma-separated list of environment-specific settings that should be preserved when copying production database to dev/test. When production DB is copied down, these settings would be overwritten w...

**Common questions this answers:**
- What is TEST_SETTINGS?
- What does TEST_SETTINGS do?
- What is the default value for TEST_SETTINGS?
- How do I configure TEST_SETTINGS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TEST_SETTINGS |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TEST_SETTINGS'
```

# ALLOWED_EXTENSIONS - iPurchase System Setting

**Category:** Uncategorized

This is a comma separated list of allowed or not-allowed file extensions which can be uploaded to iPurchase. This works using the Progress "can-do" function. See Progress Help if needed A default v...

**Common questions this answers:**
- What is ALLOWED_EXTENSIONS?
- What does ALLOWED_EXTENSIONS do?
- What is the default value for ALLOWED_EXTENSIONS?
- How do I configure ALLOWED_EXTENSIONS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOWED_EXTENSIONS |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | !exe,!dll,!js*,!com,!bat,!lnk,!ws*,!scr,!msi,* |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOWED_EXTENSIONS'
```

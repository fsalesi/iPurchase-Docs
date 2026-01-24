# LICENSE - iPurchase System Setting

**Category:** System Configuration

Software license key for iPurchase application.

**Common questions this answers:**
- What is LICENSE?
- What does LICENSE do?
- What is the default value for LICENSE?
- How do I configure LICENSE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LICENSE |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LICENSE'
```

# HELP_URL - iPurchase System Setting

**Category:** Uncategorized

If you've developed customized help, then enter the URL to that file here. ex. https://google.com

**Common questions this answers:**
- What is HELP_URL?
- What does HELP_URL do?
- What is the default value for HELP_URL?
- How do I configure HELP_URL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | HELP_URL |
| **Category** | Uncategorized |
| **Owner** |  |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'HELP_URL'
```

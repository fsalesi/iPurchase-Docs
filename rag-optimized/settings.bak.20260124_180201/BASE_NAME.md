# BASE_NAME - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is BASE_NAME?
- What does BASE_NAME do?
- What is the default value for BASE_NAME?
- How do I configure BASE_NAME?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BASE_NAME |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | /custom/ipurchase |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BASE_NAME'
```

# AUTO_COMMENTS_BUYER - iPurchase System Setting

**Category:** Purchase Orders

Use this setting to automatically attach comments to every Purchase Order when a particular buyer or bill to or ship to or site or line site is used. This is a pointer to the code_mstr field name (...

**Common questions this answers:**
- What is AUTO_COMMENTS_BUYER?
- What does AUTO_COMMENTS_BUYER do?
- What is the default value for AUTO_COMMENTS_BUYER?
- How do I configure AUTO_COMMENTS_BUYER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_COMMENTS_BUYER |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_COMMENTS_BUYER'
```

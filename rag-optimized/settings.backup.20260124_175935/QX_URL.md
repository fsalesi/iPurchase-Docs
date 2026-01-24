# QX_URL - iPurchase System Setting

**Category:** Qxtend Integration

Qxtend service URL.

**Common questions this answers:**
- What is QX_URL?
- What does QX_URL do?
- What is the default value for QX_URL?
- How do I configure QX_URL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QX_URL |
| **Category** | Qxtend Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QX_URL'
```

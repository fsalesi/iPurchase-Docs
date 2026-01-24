# QAD_INTERFACE_PASSWORD - iPurchase System Setting

**Category:** QAD Integration

⚠️ SENSITIVE. Password for QAD system integration user.

**Common questions this answers:**
- What is QAD_INTERFACE_PASSWORD?
- What does QAD_INTERFACE_PASSWORD do?
- What is the default value for QAD_INTERFACE_PASSWORD?
- How do I configure QAD_INTERFACE_PASSWORD?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QAD_INTERFACE_PASSWORD |
| **Category** | QAD Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QAD_INTERFACE_PASSWORD'
```

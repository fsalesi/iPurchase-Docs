# ALLOWED_DOMAINS - iPurchase System Setting

**Category:** Uncategorized

Enter a comma-separated list of domain codes to be allowed in iPurchase. This can be changed for a given user in User Maintenance

**Common questions this answers:**
- What is ALLOWED_DOMAINS?
- What does ALLOWED_DOMAINS do?
- What is the default value for ALLOWED_DOMAINS?
- How do I configure ALLOWED_DOMAINS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOWED_DOMAINS |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | QAD |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOWED_DOMAINS'
```

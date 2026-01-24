# AUDIT_TRAIL_DOMAIN_EXEMPTION - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is AUDIT_TRAIL_DOMAIN_EXEMPTION?
- What does AUDIT_TRAIL_DOMAIN_EXEMPTION do?
- What is the default value for AUDIT_TRAIL_DOMAIN_EXEMPTION?
- How do I configure AUDIT_TRAIL_DOMAIN_EXEMPTION?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TRAIL_DOMAIN_EXEMPTION |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | pf_mstr,wus_mstr,wgr_mstr,wugr_mstr |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TRAIL_DOMAIN_EXEMPTION'
```

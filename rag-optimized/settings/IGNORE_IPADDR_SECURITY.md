# IGNORE_IPADDR_SECURITY - iPurchase System Setting

**Category:** Security & Authentication



**Common questions this answers:**
- What is IGNORE_IPADDR_SECURITY?
- What does IGNORE_IPADDR_SECURITY do?
- What is the default value for IGNORE_IPADDR_SECURITY?
- How do I configure IGNORE_IPADDR_SECURITY?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IGNORE_IPADDR_SECURITY |
| **Category** | Security & Authentication |
| **Owner** | IT |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IGNORE_IPADDR_SECURITY'
```

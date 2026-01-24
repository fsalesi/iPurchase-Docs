# ADMIN_IP - iPurchase System Setting

**Category:** Security & Authentication

Comma-separated IP addresses. Restricts admin features to specific IP addresses. If blank, all IPs are allowed. Used for IP-based access control.

**Common questions this answers:**
- What is ADMIN_IP?
- What does ADMIN_IP do?
- What is the default value for ADMIN_IP?
- How do I configure ADMIN_IP?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ADMIN_IP |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ADMIN_IP'
```

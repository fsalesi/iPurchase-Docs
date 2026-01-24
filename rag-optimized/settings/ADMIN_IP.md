# ADMIN_IP - iPurchase System Setting

**Category:** Security & Authentication

Comma-separated IP addresses. Restricts admin features to specific IP addresses. If blank, all IPs are allowed. Used for IP-based access control.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ADMIN_IP |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ADMIN_IP'
```

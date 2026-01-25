# ADMIN_IP - iPurchase System Setting

**Category:** Security & Authentication

Comma-separated IP addresses.

### How It Works

This setting configures security & authentication behavior in iPurchase.

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
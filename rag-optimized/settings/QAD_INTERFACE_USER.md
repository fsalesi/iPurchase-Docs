# QAD_INTERFACE_USER - iPurchase System Setting

**Category:** User Management

Use this setting to set the User ID for integration to QAD.

### How It Works

This setting configures user management behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QAD_INTERFACE_USER |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QAD_INTERFACE_USER'
```
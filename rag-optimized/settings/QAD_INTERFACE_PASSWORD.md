# QAD_INTERFACE_PASSWORD - iPurchase System Setting

**Category:** QAD Integration

⚠️ **SENSITIVE** - This setting contains credentials for QAD system integration.

### Purpose

Stores the password used by iPurchase to authenticate with the QAD ERP system for creating purchase orders and other integration activities.

### Security Notes

- This value is stored encrypted in the database
- Access should be restricted to system administrators only
- Change this password if you suspect it has been compromised
- Coordinate with your QAD administrator when changing this value

### Common Questions

- What is QAD_INTERFACE_PASSWORD?
- How do I update the QAD integration password?
- Why is QAD integration failing?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QAD_INTERFACE_PASSWORD |
| **Category** | QAD Integration |
| **Owner** | ISS |
| **Default Value** | (none) |
| **Sensitivity** | ⚠️ SENSITIVE |

### How to Query

```sql
-- Note: This returns an encrypted value
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QAD_INTERFACE_PASSWORD'
```

### Related Settings

- **QAD_INTERFACE_USER** - Username for QAD integration

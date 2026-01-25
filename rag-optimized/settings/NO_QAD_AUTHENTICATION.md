# NO_QAD_AUTHENTICATION - iPurchase System Setting

**Category:** Security & Authentication

Do not use QAD passwords for users that are also in QAD.

### How It Works

This setting configures security & authentication behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_QAD_AUTHENTICATION |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | true |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_QAD_AUTHENTICATION'
```

### Related Settings

- [NO_PASSWORD_ON_APPROVE](NO_PASSWORD_ON_APPROVE.md)

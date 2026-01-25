# IGNORE_IPADDR_SECURITY - iPurchase System Setting

**Category:** Security & Authentication

Configuration setting for security & authentication.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IGNORE_IPADDR_SECURITY |
| **Category** | Security & Authentication |
| **Owner** | IT |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IGNORE_IPADDR_SECURITY'
```

### Related Settings

- [IGNORE_PASSWORDS_ON_TEST](IGNORE_PASSWORDS_ON_TEST.md)

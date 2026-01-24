# NO_QAD_AUTHENTICATION - iPurchase System Setting

**Category:** Security & Authentication

Do not use QAD passwords for users that are also in QAD. Let iPurchase manage those passwords.

### How It Works

See the description above for details on how this setting affects system behavior.

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
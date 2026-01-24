# LOGIN_BACK_IN_OFFICE - iPurchase System Setting

**Category:** Security & Authentication

If you currently have the Out-Of-Office setting on, this setting can automatically turn it off when you login. A setting of "ASK" will prompt the user if they want to turn off OOF, but only once every 12 hours.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_BACK_IN_OFFICE |
| **Category** | Security & Authentication |
| **Owner** | Power Users |
| **Default Value** | ASK |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_BACK_IN_OFFICE'
```
# LOCK_OUT_MINUTES - iPurchase System Setting

**Category:** Uncategorized

The number of minutes a user will be locked out after failing to login more than the value of setting FAILED_LOGIN_ATTEMPTS

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOCK_OUT_MINUTES |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | 10 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOCK_OUT_MINUTES'
```

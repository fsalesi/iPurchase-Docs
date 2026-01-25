# LOGOFF_MINUTES - iPurchase System Setting

**Category:** Uncategorized

Enter how many minutes of inactivity the system will wait until it logs a user off.

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGOFF_MINUTES |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | 0 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGOFF_MINUTES'
```
# DEPARTMENT_SORT_BY_NAME - iPurchase System Setting

**Category:** GL Accounts & Finance

A value of true will show the departments sorted by name.

### How It Works

This setting configures gl accounts & finance behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEPARTMENT_SORT_BY_NAME |
| **Category** | GL Accounts & Finance |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEPARTMENT_SORT_BY_NAME'
```
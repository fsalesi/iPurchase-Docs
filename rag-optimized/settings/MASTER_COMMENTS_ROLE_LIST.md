# MASTER_COMMENTS_ROLE_LIST - iPurchase System Setting

**Category:** Uncategorized

Comma-Separated list of group ID's or "*" for all.

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MASTER_COMMENTS_ROLE_LIST |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MASTER_COMMENTS_ROLE_LIST'
```
# PUNCHOUT_LEADTIME - iPurchase System Setting

**Category:** Catalog & Vendors

The number of days to add to today's date in order to calculate the Need Date for the requisition header.

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_LEADTIME |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | 3 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_LEADTIME'
```

### Related Settings

- [PUNCHOUT_DISABLE_USERS](PUNCHOUT_DISABLE_USERS.md)
- [PUNCHOUT_NOFRAMES](PUNCHOUT_NOFRAMES.md)
- [PUNCHOUT_NO_ITEM_DESC](PUNCHOUT_NO_ITEM_DESC.md)
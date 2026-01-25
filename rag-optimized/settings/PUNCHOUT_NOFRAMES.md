# PUNCHOUT_NOFRAMES - iPurchase System Setting

**Category:** Catalog & Vendors

iPurchase uses an HTML FRAMESET to display the Punchout website as well as the Return to iPurchase button at the top left.

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PUNCHOUT_NOFRAMES |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PUNCHOUT_NOFRAMES'
```

### Related Settings

- [PUNCHOUT_DISABLE_USERS](PUNCHOUT_DISABLE_USERS.md)
- [PUNCHOUT_LEADTIME](PUNCHOUT_LEADTIME.md)
- [PUNCHOUT_NO_ITEM_DESC](PUNCHOUT_NO_ITEM_DESC.md)

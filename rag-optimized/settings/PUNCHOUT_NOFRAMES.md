# PUNCHOUT_NOFRAMES - iPurchase System Setting

**Category:** Catalog & Vendors

iPurchase uses an HTML FRAMESET to display the Punchout website as well as the Return to iPurchase button at the top left. Some suppliers, like Amazon, will not allow the Return to iPurchase button on top. If the Punchout Supplier that you're working with does not allow the button, then add their Supplier Address Code in this setting as a comma-separated value.

### How It Works

See the description above for details on how this setting affects system behavior.

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
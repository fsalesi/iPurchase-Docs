# CAT_REJECT_TO_SUPPLIER - iPurchase System Setting

**Category:** Catalog & Vendors

If a catalog exception requisition is rejected, the supplier will receive an email if set to true.

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CAT_REJECT_TO_SUPPLIER |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | False  |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CAT_REJECT_TO_SUPPLIER'
```
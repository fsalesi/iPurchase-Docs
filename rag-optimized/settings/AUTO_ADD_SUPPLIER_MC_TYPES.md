# AUTO_ADD_SUPPLIER_MC_TYPES - iPurchase System Setting

**Category:** Catalog & Vendors

In QAD master comments, there is a reference number to identify a master comment, if this reference number equals the suppler then the master comment will be added to the requisition automatically if the corresponding type of master comment is entered into this system setting.

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_ADD_SUPPLIER_MC_TYPES |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | PO |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_ADD_SUPPLIER_MC_TYPES'
```
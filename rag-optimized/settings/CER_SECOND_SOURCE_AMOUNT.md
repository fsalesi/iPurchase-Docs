# CER_SECOND_SOURCE_AMOUNT - iPurchase System Setting

**Category:** Catalog & Vendors

Dollar amount.

### How It Works

This setting configures catalog & vendors behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CER_SECOND_SOURCE_AMOUNT |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CER_SECOND_SOURCE_AMOUNT'
```
# RT_PO_REQUIRED - iPurchase System Setting

**Category:** Purchase Orders

This setting is a list of requisition types that would set the PO Required field to True or Yes.

### How It Works

This setting affects purchase order processing and how POs are generated, formatted, or transmitted to suppliers.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_PO_REQUIRED |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_PO_REQUIRED'
```
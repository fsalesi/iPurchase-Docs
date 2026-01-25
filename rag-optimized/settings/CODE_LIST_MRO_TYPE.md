# CODE_LIST_MRO_TYPE - iPurchase System Setting

**Category:** Code Lists & Dropdowns

code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Line MRO Type selection list, and validation.

### How It Works

This setting configures code lists & dropdowns behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_MRO_TYPE |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_MRO_TYPE'
```

### Related Settings

- [CODE_LIST_H_BILLTO](CODE_LIST_H_BILLTO.md)
- [CODE_LIST_H_BLANKET_CYCLE](CODE_LIST_H_BLANKET_CYCLE.md)
- [CODE_LIST_H_CURRENCY](CODE_LIST_H_CURRENCY.md)
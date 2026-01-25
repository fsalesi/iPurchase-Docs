# CODE_LIST_H_SHIPTO - iPurchase System Setting

**Category:** Code Lists & Dropdowns

Configures the source for the Header Ship To dropdown list in requisitions.

### How It Works

This setting controls where iPurchase gets the list of valid values for the Header Ship To field. It can point to:
- A QAD table (like si_mstr)
- A code_mstr field name
- An inline LIST definition

### Valid Values

| Value | Behavior |
|-------|----------|
| Blank | Use default QAD table (si_mstr) |
| `code_fldname` | Use code_mstr where code_fldname matches |
| `LIST:val1,val2` | Inline list of values |
| `LIST:code1:name1,code2:name2` | Inline list with codes and descriptions |

### Example

```
LIST:EA,BX,PK
LIST:EA:Each,BX:Box,PK:Pack
```

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_SHIPTO |
| **Category** | Code Lists & Dropdowns |
| **Owner** | Admin |
| **Default Value** | (varies) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_SHIPTO'
```

### Related Settings

- [CODE_LIST_H_BILLTO](CODE_LIST_H_BILLTO.md)
- [CODE_LIST_H_BLANKET_CYCLE](CODE_LIST_H_BLANKET_CYCLE.md)
- [CODE_LIST_H_CURRENCY](CODE_LIST_H_CURRENCY.md)

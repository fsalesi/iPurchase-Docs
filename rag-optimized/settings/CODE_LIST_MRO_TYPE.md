# CODE_LIST_MRO_TYPE - iPurchase System Setting

**Category:** Code Lists & Dropdowns

code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Line MRO Type selection list, and validation. You can also use the prefix "LIST:" followed by a comma-separated list of values. This will tell iPurchase that the specified list is to be used. Example: LIST:EA,BX,PK   or Separate each entry with a colon to have both a code and name: LIST:EA:EACH,BX:Box,PK:Pack NOT USED

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

### Valid Values

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone/all users |
| Blank/empty | No one/disabled |
| User/Group list | Only specified users/groups |

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

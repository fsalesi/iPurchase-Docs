# PO_PRINT_OFFLINE - iPurchase System Setting

**Category:** Purchase Orders

This setting will control when the New PO Created email and original PO Print occur. A value of FALSE, the default, will print the PO and send the email as soon as the Purchase Order is created. Mo...

**Common questions this answers:**
- What is PO_PRINT_OFFLINE?
- What does PO_PRINT_OFFLINE do?
- What is the default value for PO_PRINT_OFFLINE?
- How do I configure PO_PRINT_OFFLINE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINT_OFFLINE |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_OFFLINE'
```

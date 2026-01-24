# PO_CONFIRMATION_RESPONSE - iPurchase System Setting

**Category:** Purchase Orders

Message to display to the supplier when the supplier confirms receipt of the PO by clicking on the Confirm Receipt link in their email message.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_CONFIRMATION_RESPONSE |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_CONFIRMATION_RESPONSE'
```

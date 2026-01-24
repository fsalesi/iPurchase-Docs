# RT_PO_REQUIRED - iPurchase System Setting

**Category:** Purchase Orders

This setting is a list of requisition types that would set the PO Required field to True or Yes.  For example if you do not require a PO for credit card purchases and CREDIT_CARD is a Requisition Type, then list all the other Requisition Types here. The default is TRUE unless an item appears in this list. The list should be in the format EXPENSE,CAPITAL,TOOLING

### How It Works

See the description above for valid values and usage.

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

# CODE_LIST_H_SHIPVIA_XREF_[VENDOR NUMBER] - iPurchase System Setting

**Category:** iApprove Integration

This setting defines a cross-reference between the selected iPurchase ship via, and the code or description that the vendor needs to see on their electronic purchase order. Only applies to Punchout Purchase Orders. The [Vendor Number] needs to be the actual vendor number that this cross reference is valid for. The format should be LIST:UPS:UPS Ground,Fedx,Fedex 3 day Where UPS is the value for this ship via in iPurchase or QAD, and UPS Ground is the value the vendor requires.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CODE_LIST_H_SHIPVIA_XREF_[VENDOR NUMBER] |
| **Category** | iApprove Integration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CODE_LIST_H_SHIPVIA_XREF_[VENDOR NUMBER]'
```
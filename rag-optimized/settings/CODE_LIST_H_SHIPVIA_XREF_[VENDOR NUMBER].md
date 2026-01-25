# CODE_LIST_H_SHIPVIA_XREF_[VENDOR NUMBER] - iPurchase System Setting

**Category:** iApprove Integration

This setting defines a cross-reference between the selected iPurchase ship via, and the code or description that the vendor needs to see on their electronic purchase order.

### How It Works

This setting configures iapprove integration behavior in iPurchase.

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

### Related Settings

- [CODE_LIST_H_SHIPVIA_XREF](CODE_LIST_H_SHIPVIA_XREF.md)

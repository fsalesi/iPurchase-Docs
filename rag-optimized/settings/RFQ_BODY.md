# RFQ_BODY - iPurchase System Setting

**Category:** RFQ Management

Email body template for RFQ emails.

### How It Works

This setting configures rfq management behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RFQ_BODY |
| **Category** | RFQ Management |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RFQ_BODY'
```

### Related Settings

- [RFQ_SUBJECT](RFQ_SUBJECT.md)
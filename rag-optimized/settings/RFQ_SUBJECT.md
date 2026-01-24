# RFQ_SUBJECT - iPurchase System Setting

**Category:** RFQ Management

Email subject for RFQ emails.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RFQ_SUBJECT |
| **Category** | RFQ Management |
| **Owner** | Purchasing |
| **Default Value** | Request for Quote |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RFQ_SUBJECT'
```

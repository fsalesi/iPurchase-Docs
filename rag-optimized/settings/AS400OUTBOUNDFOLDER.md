# AS400OUTBOUNDFOLDER - iPurchase System Setting

**Category:** QAD Integration

Directory path on application server.

### How It Works

This setting configures qad integration behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AS400OUTBOUNDFOLDER |
| **Category** | QAD Integration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AS400OUTBOUNDFOLDER'
```
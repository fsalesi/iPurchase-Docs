# IAEAMJE_MSTR_REQ_PREFIX - iPurchase System Setting

**Category:** iApprove Integration

Prefix for requisition numbers in iApprove EAM JE integration.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | IAEAMJE_MSTR_REQ_PREFIX |
| **Category** | iApprove Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'IAEAMJE_MSTR_REQ_PREFIX'
```

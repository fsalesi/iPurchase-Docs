# AS400OUTBOUNDFOLDER - iPurchase System Setting

**Category:** QAD Integration

Directory path on application server. Folder where AS400 catalog XML files are written. Files are named [req_nbr].xml. Used in catalog integration.

### How It Works

See the description above for details on how this setting affects system behavior.

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
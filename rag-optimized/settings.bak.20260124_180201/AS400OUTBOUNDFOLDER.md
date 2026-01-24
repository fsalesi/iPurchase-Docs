# AS400OUTBOUNDFOLDER - iPurchase System Setting

**Category:** QAD Integration

Directory path on application server. Folder where AS400 catalog XML files are written. Files are named [req_nbr].xml. Used in catalog integration.

**Common questions this answers:**
- What is AS400OUTBOUNDFOLDER?
- What does AS400OUTBOUNDFOLDER do?
- What is the default value for AS400OUTBOUNDFOLDER?
- How do I configure AS400OUTBOUNDFOLDER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AS400OUTBOUNDFOLDER |
| **Category** | QAD Integration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AS400OUTBOUNDFOLDER'
```

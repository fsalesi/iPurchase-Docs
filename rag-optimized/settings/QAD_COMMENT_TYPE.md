# QAD_COMMENT_TYPE - iPurchase System Setting

**Category:** QAD Integration

This is the comment type to be used when creating PO Header and PO Line comments.  Add IP To Generalized Codes if there are any generalized codes for field name cd_type

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QAD_COMMENT_TYPE |
| **Category** | QAD Integration |
| **Owner** | Admin |
| **Default Value** | IP |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QAD_COMMENT_TYPE'
```
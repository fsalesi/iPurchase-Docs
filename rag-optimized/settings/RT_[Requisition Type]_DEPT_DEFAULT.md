# RT_[Requisition Type]_DEPT_DEFAULT - iPurchase System Setting

**Category:** Requisitions

Substitute the requisition type for "[REQUISITION TYPE]". This is the default Department to be used for the specified requisition type. It will override the default department specified on the user profile. Set this value to "BLANK" if a blank department is required

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_DEPT_DEFAULT |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_DEPT_DEFAULT'
```
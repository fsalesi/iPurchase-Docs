# RT_[Requisition Type]_[Site]_DEPT_READONLY - iPurchase System Setting

**Category:** Requisitions

TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting determines whether the users can change the department during line entry and is specific to the requisition type and site combination specified.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_[Site]_DEPT_READONLY |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_[Site]_DEPT_READONLY'
```
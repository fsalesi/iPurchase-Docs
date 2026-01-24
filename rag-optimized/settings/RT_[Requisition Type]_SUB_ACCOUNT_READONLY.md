# RT_[Requisition Type]_SUB_ACCOUNT_READONLY - iPurchase System Setting

**Category:** Requisitions

TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]". This setting determines whether the users can change the sub account during line entry and is specific to the requisition type specified

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_SUB_ACCOUNT_READONLY |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_SUB_ACCOUNT_READONLY'
```
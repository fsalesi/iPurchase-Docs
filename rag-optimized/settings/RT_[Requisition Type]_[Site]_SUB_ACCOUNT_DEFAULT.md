# RT_[Requisition Type]_[Site]_SUB_ACCOUNT_DEFAULT - iPurchase System Setting

**Category:** Requisitions

Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This is the default Sub Account to be used for the specified requisition type and site combination.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_[Site]_SUB_ACCOUNT_DEFAULT |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_[Site]_SUB_ACCOUNT_DEFAULT'
```
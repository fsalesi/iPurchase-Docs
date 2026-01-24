# RT_[Requisition Type]_REQUIRE_PROJECT - iPurchase System Setting

**Category:** Requisitions

Comma separated list of requisition types which will require a project code listed.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_REQUIRE_PROJECT |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_REQUIRE_PROJECT'
```